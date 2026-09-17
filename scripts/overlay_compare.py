#!/usr/bin/env python3
"""Create visual QA artifacts for a source page and a rendered PPT page.

This helper is intentionally independent of any PPTX writer. The caller may
render with PowerPoint, LibreOffice, a browser engine, or another adapter.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageChops, ImageEnhance, ImageOps


def fit_to_canvas(image: Image.Image, size: tuple[int, int]) -> tuple[Image.Image, dict]:
    """Keep aspect ratio and add white letterbox margins when needed."""
    source = image.convert("RGBA")
    target_w, target_h = size
    scale = min(target_w / source.width, target_h / source.height)
    resized = source.resize(
        (max(1, round(source.width * scale)), max(1, round(source.height * scale))),
        Image.Resampling.LANCZOS,
    )
    canvas = Image.new("RGBA", size, (255, 255, 255, 255))
    offset = ((target_w - resized.width) // 2, (target_h - resized.height) // 2)
    canvas.alpha_composite(resized, dest=offset)
    return canvas, {
        "original_size": [source.width, source.height],
        "scale": scale,
        "offset": list(offset),
        "content_size": [resized.width, resized.height],
    }


def histogram_metrics(gray: Image.Image, threshold: int) -> dict:
    histogram = gray.histogram()
    total = sum(histogram)
    weighted = sum(index * count for index, count in enumerate(histogram))
    cumulative = 0
    p95 = 0
    target = total * 0.95
    for index, count in enumerate(histogram):
        cumulative += count
        if cumulative >= target:
            p95 = index
            break

    pixels = gray.load()
    min_x, min_y = gray.width, gray.height
    max_x, max_y = -1, -1
    changed = 0
    for y in range(gray.height):
        for x in range(gray.width):
            value = pixels[x, y]
            if value < threshold:
                continue
            changed += 1
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

    return {
        "mean_absolute_difference": round(weighted / total, 4) if total else 0,
        "p95_absolute_difference": p95,
        "threshold": threshold,
        "changed_pixel_ratio": round(changed / total, 6) if total else 0,
        "changed_bbox": None if max_x < 0 else [min_x, min_y, max_x, max_y],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Blend and compare a source page with a rendered PPT page.")
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--render", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--threshold", type=int, default=24)
    parser.add_argument("--contrast", type=float, default=2.5)
    args = parser.parse_args()

    source_raw = Image.open(args.source)
    render_raw = Image.open(args.render)
    target_size = source_raw.size
    source, source_transform = fit_to_canvas(source_raw, target_size)
    render, render_transform = fit_to_canvas(render_raw, target_size)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    overlay = Image.blend(source, render, 0.5)
    difference_rgb = ImageChops.difference(source, render).convert("RGB")
    difference = ImageEnhance.Contrast(difference_rgb).enhance(args.contrast)
    gray = ImageOps.grayscale(difference_rgb)
    heatmap = ImageOps.colorize(gray, black="#101010", white="#FF3B30")

    overlay_path = args.output_dir / "overlay.png"
    difference_path = args.output_dir / "difference.png"
    heatmap_path = args.output_dir / "difference-heatmap.png"
    metrics_path = args.output_dir / "metrics.json"
    overlay.save(overlay_path)
    difference.save(difference_path)
    heatmap.save(heatmap_path)

    metrics = {
        "source": str(args.source.resolve()),
        "render": str(args.render.resolve()),
        "canvas_size": list(target_size),
        "source_transform": source_transform,
        "render_transform": render_transform,
        "artifacts": {
            "overlay": str(overlay_path.resolve()),
            "difference": str(difference_path.resolve()),
            "difference_heatmap": str(heatmap_path.resolve()),
        },
        **histogram_metrics(gray, max(0, min(255, args.threshold))),
    }
    metrics_path.write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(metrics, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
