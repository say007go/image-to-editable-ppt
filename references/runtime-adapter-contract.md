# 运行环境适配契约

本技能只规定输入、对象、验收和交付，不绑定某个 AI 平台、编程语言、PPTX 库或办公软件。默认运行环境应由具备图像理解能力的多模态模型提供视觉输入，并根据自身工具实现以下接口。

核心提示词中的 Step 3 以 Python（python-pptx）作为可直接执行的实现基线；若当前环境使用等效的原生 PPTX 写入能力，可以在适配层替换实现，但不得降低核心提示词规定的对象独立性、文字可编辑性、渲染复核和交付要求。

## 能力分层

要宣称完成高保真转换，运行环境至少应具备以下能力：

```text
supports_visual_input() -> boolean
read_visual_source(source) -> page images or visual observations
extract_text_and_geometry(page) -> object observations
create_native_pptx(slide_spec) -> pptx file
render_pptx(pptx file) -> rendered page images
inspect_pptx(pptx file) -> object and editability report
compare_renders(source page, rendered page, options) -> overlay, difference, metrics
```

以下是按页面和运行环境启用的实现能力，不要求每个适配器全部具备；缺少某项时必须选择等效实现或在验收中披露：

```text
apply_geometry_patch(pptx file, object patches) -> pptx file
supports_preset_geometry(name) -> boolean
add_preset_shape(name, position, style, adjustments) -> native shape
fit_visual_geometry(observation, position, style) -> native shape | independent native shapes | unsupported
add_path_component(path_or_contours, position, style) -> native shape
add_local_component(geometry, position, style) -> native shape
add_composite_shape(components, position, style) -> independent native shapes
add_vector_icon(svg_bytes, position, style, metadata) -> independent vector object
convert_vector_icon_to_native(svg_bytes) -> native shapes | unsupported
convert_vector_path_to_native(svg_path, position, style) -> native custom geometry | unsupported
```

使用标准图标库且页面确实包含标准图标时，适配器还应提供或等效实现以下资源解析能力：

```text
probe_icon_source(library, version, cache) -> cached | reachable | unavailable
resolve_icon_asset(library, icon_id, version, cache) -> svg_bytes, metadata | unavailable
record_icon_provenance(library, icon_id, version, license_url, content_hash) -> manifest entry
```

资源解析顺序应为固定版本本地包/缓存 → 已确认可达的官方入口 → 下一套候选库。不得把官网实时可访问性当作 PPTX 编译的唯一前提；如果只能得到网页预览而不能获得可追溯的 SVG 与许可证信息，应停止使用该图标并在验收报告中说明。

其中 `render_pptx` 和 `inspect_pptx` 可以由自动化工具、办公软件、文件解析器或人工检查完成，但最终结果必须如实说明验证范围。

## 中间对象模型

如果运行环境适合先生成结构化数据，可使用如下抽象模型：

以下字段示例使用核心提示词的 16:9 默认画布；字号、颜色和几何值仅用于说明字段类型，实际值必须来自当前页面或用户明确指定的变换参数。

```json
{
  "canvas": {"width": 13.333, "height": 7.5, "unit": "in"},
  "texts": [
    {"id": "t1", "text": "...", "x": 0, "y": 0, "w": 1, "h": 0.4, "font": "...", "size_pt": "{{SIZE_PT}}", "color": "{{TEXT_COLOR}}", "weight": "regular"}
  ],
  "shapes": [
    {
      "id": "s1",
      "type": "visual-object",
      "geometry": {"kind": "closed-contour|open-path|composite|preset", "contours": [], "paths": [], "control_points": [], "local_components": []},
      "x": 0, "y": 0, "w": 1, "h": 1,
      "fill": "{{FILL_COLOR}}",
      "line": null,
      "z": 1
    }
  ],
  "images": [],
  "z_order": ["s1", "t1"]
}
```

字段名称可以调整，但不能丢失文字、几何、样式、层级和图片例外信息。

## 完整交付的硬前提

完整交付必须同时具备：视觉输入与局部查看、原生 PPTX 写入、PPTX 渲染、对象结构检查，以及源图与渲染图的叠加/差异比对。矢量路径转换用于复杂图形优化，不是每次转换的硬前提。

缺少任何一个硬前提时，停止在缺失环节，不得把对象清单、未渲染文件或未检查的 PPTX 宣称为高保真成品，并明确说明缺失能力和未完成的验证项目。

## 图形形态与图标能力声明

适配器必须在开始编译前声明标准预设形状、路径拟合和矢量图标的能力：

- `supports_preset_geometry` 返回真时，先以目标参数做渲染探针；探针通过才使用预设，探针失败时允许登记原因并切换到已验证的原生 Custom Geometry 回退；
- `add_vector_icon` 至少要保持每个图标为独立矢量对象，并保留图标元数据；
- `convert_vector_icon_to_native` 是可选能力，只有转换结果经过渲染检查后，才可宣称达到路径级可编辑；
- `convert_vector_path_to_native` 是可选能力，只有转换结果经过渲染检查后，才可宣称达到路径级可编辑；
- `compare_renders` 应保留归一化画布尺寸、缩放因子、偏移量、阈值和差异统计；颜色变换场景应支持边缘或轮廓比对，避免把换色误判为位移；
- `apply_geometry_patch` 只接受已定位对象的 X/Y/宽高/旋转/路径或局部构件/内边距补丁，不能在没有对象映射的情况下按像素差异盲目平移整页；
- 如果适配器无法嵌入 SVG，应优先使用可用的同源原生图标路径或另一套许可证清晰的矢量图标资源，不得静默降级为低分辨率 PNG；
- 能力缺口必须进入验收报告，区分“可渲染”“对象级可编辑”和“路径级可编辑”。
