# Image to Editable PowerPoint

**图片转可编辑 PPT · High-Fidelity Reconstruction Skill**

> 将幻灯片截图、PNG、JPG 或 PDF 页面，重构为视觉高度还原、对象独立、可持续编辑的原生 PowerPoint 文件。  
> Reconstruct slide screenshots, PNG/JPG images, or PDF pages into high-fidelity, natively editable PowerPoint files with independently adjustable objects.

![Version](https://img.shields.io/badge/version-1.0.0-1f6feb)
![Format](https://img.shields.io/badge/output-editable%20PPTX-f2cc60)
![Workflow](https://img.shields.io/badge/workflow-visual%20evidence%20%2B%20QA-2da44e)

**Skill name:** <code>image-to-editable-ppt</code>  
**中文名称：** 图片转可编辑 PPT  
**作者 / Author：** 圣婴

### 语言选择 / Language Selection

- [中文文档 / Chinese Documentation](#zh)
- [English Documentation / 英文文档](#en)

---

<a id="zh"></a>

## 中文

### 1. 项目概述

<code>image-to-editable-ppt</code> 是一个面向多模态 AI Agent 的 PowerPoint 逆向重构 skill。

它解决的不是“把图片放进 PPT”，而是把一页已经存在的视觉稿拆解成一组可理解、可定位、可修改、可验收的 PowerPoint 对象：

- 文字还原为可双击编辑的 TextBox 或 Text Run；
- 色块、卡片、边框、分割线和容器还原为独立 Shape；
- 路径性、方向性和复合图形按可见轮廓与局部构件拆分；
- 表格和数据使用可编辑的文本、表格和图形对象表达；
- 标准图标优先使用具有许可证追溯信息的独立矢量对象；
- 只有真正不可拆解的照片、产品渲染图或复杂三维视觉，才允许作为局部图片保留。

核心目标是：在保持输入页面视觉关系的同时，让最终 PPTX 真正成为可以继续工作的源文件。

### 2. 它的价值

#### 2.1 把“参考图”变成“可持续编辑的工作文件”

传统的图片转 PPT 通常只得到一张不可编辑的整页图片。这个 skill 以对象拆解为基础，使使用者可以继续修改：

- 文案、数字、单位和标点；
- 字号、字重、字体、颜色和对齐方式；
- 卡片、色块、边框、路径和图标；
- 局部布局、间距、层级和品牌配色。

这意味着参考页不再只是展示材料，而可以沉淀为后续方案、汇报、投标和培训项目中的可复用资产。

#### 2.2 同时关注视觉保真与编辑能力

可编辑不等于粗略重画，视觉相似也不等于真正可编辑。本 skill 将两者作为同等重要的交付目标：

1. 先通过视觉证据识别页面中的文字、坐标、颜色、层级、轮廓和负空间；
2. 再为每个对象选择最合适的原生 PowerPoint 表达方式；
3. 最后将渲染结果与输入页面进行叠加比对，并把偏差定位回具体对象。

因此，页面不是依赖模板名称或历史经验机械套用，而是由当前输入页面的实际形态驱动。

#### 2.3 让复杂图形也具备可控的编辑边界

路径、箭头、弧线、异形边界、缺口、尖点和局部构件，经常是图片重构中最容易失真的部分。skill 会区分：

- 主体轮廓；
- 开放路径或中心线；
- 端部、尖点、阴影、标记等局部构件；
- 填充、描边、透明度和层级；
- 对象级编辑与路径级编辑。

这种拆分可以避免用一个大图片或一个不可控的整体 SVG 掩盖结构问题，也便于后续精确调整。

#### 2.4 支持有授权边界的画布与品牌变换

在完成基础保真重构后，可以根据用户明确要求：

- 将页面适配为 16:9、4:3 或其他目标比例；
- 将指定颜色角色映射为企业品牌色；
- 保留照片、复杂视觉和用户明确要求保留的语义色；
- 保持文字内容、层级和相对关系不被未经授权地改变。

变换过程是可追溯的，不把“换色”误当成“重新设计”，也不把“改比例”处理成简单拉伸。

#### 2.5 交付结果可检查、可解释、可复盘

每个关键判断都可以回到对象清单、渲染结果、叠加图、差异图和验收规则。对于无法从输入页面确认的细节，skill 要求披露近似替代，而不是凭经验捏造。

这使交付结果更适合企业协作、方案复用和正式项目归档。

### 3. 核心特点

| 特点 | 具体能力 | 对使用者的价值 |
| --- | --- | --- |
| 原生对象重构 | 文字、容器、线条、图形、表格和图标按独立对象生成 | 后续可以直接修改，而不是重新描图 |
| 视觉证据优先 | 以当前输入页面的可见轮廓、颜色、层级和负空间为判断依据 | 降低模板误套和形态误判 |
| 高保真校准 | 渲染、透明叠加、差异图、热图和局部 ROI 检查 | 能发现错位、遮挡、溢出和文字截断 |
| 复杂形态拆分 | 支持预设形状、原生组合、Custom Geometry 和独立矢量对象的分层回退 | 在编辑能力与几何准确度之间取得平衡 |
| 文字逐字保真 | 保留大小写、标点、空格、数字单位和显式换行 | 适合正式方案、投标和管理汇报材料 |
| 受控变换 | 支持品牌配色、画布比例和留白适配 | 方便在不破坏结构的前提下适配新场景 |
| 图标可追溯 | 记录图标库、图标 ID、版本、许可证和编辑级别 | 便于公开发布和企业资产管理 |
| 能力边界透明 | 区分可渲染、对象级可编辑和路径级可编辑 | 避免把“看起来像”误称为“完全可编辑” |
| 受控修复 | 每轮只修复已定位的对象，最多进行三轮有效校准 | 避免无止境微调和无依据地移动整页 |

### 4. 标准工作流程

~~~mermaid
flowchart LR
    A[输入页面<br/>Image / PDF] --> B[锚定<br/>Anchor]
    B --> C[装配<br/>Assemble]
    C --> D[校准<br/>Calibrate]
    D --> E[验收交付<br/>Deliver]
    D -. 定向修复 .-> C
~~~

#### 第一步：锚定——识别输入与视觉结构

- 确认页数、尺寸、清晰度和长宽比；
- 实际查看页面以及必要的局部放大区域；
- 建立对象清单或等效场景图；
- 逐项记录对象类型、内容、边界框、样式、层级、父组、编辑级别和不确定项；
- 对文字记录标点、空格、大小写、数字单位和显式换行；
- 对图形记录轮廓、路径、端点、控制点、填充、描边和局部构件。

#### 第二步：装配——编译为原生 PowerPoint 对象

对象表达方式按以下顺序选择：

1. 通过目标尺寸渲染探针的原生预设形状；
2. 稳定的原生基础形状组合；
3. PowerPoint Custom Geometry；
4. 独立矢量对象；
5. 仅对真正不可拆解的复杂局部视觉使用图片。

文字、容器、主要结构和表格不应被降级为整页图片或承载主要文字的 SVG。

#### 第三步：校准——渲染、叠加与定向修复

- 将输入页面与 PPTX 渲染页统一到同一画布；
- 生成透明叠加图、差异图、热图和机器可读统计结果；
- 先检查画布、容器和主图形，再检查高风险局部 ROI；
- 把偏差映射回具体对象，而不是凭像素差异盲目平移整页；
- 依次处理大结构、局部几何、图标、文字内边距和仍影响使用的硬伤；
- 单页最多进行三轮有效修复；连续两轮无实质改善时停止重复尝试并披露限制。

#### 第四步：交付——结构验收与边界披露

交付前检查：

- 文件可以打开；
- 页数和画布尺寸正确；
- 主要文字可以单独选中和修改；
- 主要形状、边框、路径、表格和图标处于正确层级；
- 页面没有明显错位、遮挡、溢出、截断、遗漏和比例变形；
- 变换模块没有改变未经授权的文字、结构或图片内容；
- 清楚说明对象级可编辑和路径级可编辑的实际边界；
- 无法确认的细节已经在交付说明中披露。

### 5. 可编辑性模型

| 编辑级别 | 说明 |
| --- | --- |
| 文字级可编辑 | 文字作为 TextBox 或 Text Run，可以双击修改内容、字体、字号、颜色和对齐方式 |
| 对象级可编辑 | 色块、卡片、边框、线条、路径主体、图标和局部构件可以独立选中、移动、缩放或替换样式 |
| 路径级可编辑 | 只有在矢量路径可靠转换并通过渲染检查时，才宣称可以进一步编辑路径节点 |
| 局部图片例外 | 真人照片、复杂产品渲染图或三维插画可以作为局部图片，但不能携带可重建的文字、表格或主要结构 |

“独立 SVG 图标”表示图标对象可以独立选中和调整，不自动等同于 SVG 内部每条路径都能单独编辑。

### 6. 适用场景

- 将 PPT 截图、PNG、JPG 或 PDF 页面转换为可编辑 PPTX；
- 让图片中的标题、正文、数字和标签重新可修改；
- 复用高质量参考页的版式和图形结构；
- 将参考页适配为企业品牌色或新的画布比例；
- 重建培训方案、技术标书、管理汇报和企业宣传页中的复杂单页；
- 对已有 PPTX 做文字保真、对象独立性和视觉一致性检查；
- 将静态视觉资产沉淀为可持续维护的 PowerPoint 源文件。

### 7. 使用方式

#### 在 Codex 中使用

将 skill 文件夹放入 Codex skills 目录：

~~~text
%USERPROFILE%\.codex\skills\image-to-editable-ppt\
~~~

然后提供一张幻灯片图片或 PDF 页面，并说明目标。例如：

~~~text
请将这张幻灯片图片重构为高保真的原生可编辑 PPTX。
保持原图的文字、版式、颜色、层级和图形关系。
文字必须可以双击修改，色块、边框、路径和图标必须可以独立选中。
请完成渲染叠加校准，并在交付时说明无法完全确认的细节。
~~~

如果需要变换，可额外指定：

~~~text
在完成基础保真重构后，将画布适配为 16:9，并把主色映射为 #0B5CAD。
除明确授权的颜色和画布比例外，不改变文字、结构和图片内容。
~~~

#### 使用 QA 辅助脚本

仓库中的 <code>scripts/overlay_compare.py</code> 可以将源页面与 PPTX 渲染页统一到同一画布，并生成叠加图、差异图、差异热图和统计文件。

~~~bash
python scripts/overlay_compare.py --source path/to/source.png --render path/to/render.png --output-dir output/qa
~~~

输出内容包括：

- <code>overlay.png</code>：50% 透明叠加图；
- <code>difference.png</code>：差异图；
- <code>difference-heatmap.png</code>：差异热图；
- <code>metrics.json</code>：画布、缩放、偏移和差异统计。

该脚本只负责视觉比对，不替代 PPTX 写入器、渲染器或结构验收流程。

### 8. 仓库结构

~~~text
image-to-editable-ppt/
├── README.md
├── SKILL.md
├── references/
│   ├── core-reconstruction-protocol.md
│   ├── editability-contract.md
│   ├── overlay-calibration-protocol.md
│   ├── repair-registry.md
│   ├── runtime-adapter-contract.md
│   ├── shape-and-icon-protocol.md
│   ├── transformation-modules.md
│   └── verification-and-acceptance.md
└── scripts/
    └── overlay_compare.py
~~~

- <code>SKILL.md</code>：Agent 的主流程、触发范围和核心规则；
- <code>references/</code>：按任务分支加载的重构、可编辑性、图形、变换、修复、运行环境和验收协议；
- <code>scripts/overlay_compare.py</code>：与具体 PPTX 生成环境解耦的视觉 QA 辅助脚本；
- <code>README.md</code>：面向使用者、协作者和公开仓库访客的项目说明。

### 9. 质量标准

一个合格的输出应同时满足以下条件：

1. 文件可打开，页面数量和画布规格正确；
2. 主要文字逐字一致，并且可以独立编辑；
3. 主要容器、边框、路径、图标和表格不是一张合并图片；
4. 复合图形的主体与需要独立调整的局部构件保持分离；
5. 渲染结果没有影响使用的错位、遮挡、溢出、截断或遗漏；
6. 中西文字体属性、字号、字重、颜色、透明度和对齐关系经过检查；
7. 源图与渲染图完成同画布叠加比对；
8. 图标资源的来源、版本、许可证和编辑级别可以追溯；
9. 所有变换都符合用户的明确授权；
10. 不确定的细节和能力缺口已经如实披露。

### 10. 范围与边界

本 skill 的默认任务是**保真重构**，不是从零创作、内容改写或重新设计。

以下任务建议使用其他设计或内容架构 skill：

- 从零创作完整演示文稿；
- 对输入页面进行内容重写、逻辑重组或策略改稿；
- 只要求把一张图片作为 PPT 背景放置；
- 只要求生成新的视觉风格而不保留输入页面的结构关系。

运行环境必须具备图像查看、原生 PPTX 写入、PPTX 渲染和基本结构检查能力。若缺少其中关键环节，应明确说明验证缺口，不能将“已生成文件”直接等同于“已完成高保真转换”。

### 11. 已知限制

- 输入图片清晰度、压缩、遮挡和字体缺失会影响文字与几何识别；
- 未安装的字体可能发生替代，需要重新检查字宽、行距和换行；
- 路径级编辑能力取决于运行环境是否支持可靠的路径转换；
- 复杂照片、产品渲染图和三维插画通常保留为局部图片；
- 图标资源的实际可用性受本地缓存、网络和许可证条件影响；
- “对象级可编辑”与“路径级可编辑”是不同能力，交付时应分别说明；
- 无法从输入页面确认的隐蔽细节只能采用近似替代，并在交付说明中披露。

### 12. 资源与许可证

标准图标默认从 IconPark、Remix Icon 或 Lucide 等候选库中选择，并根据页面风格、资源可达性和许可证可追溯性确定具体来源。使用任何第三方图标时，应保留图标库、图标 ID、版本、许可证和内容哈希等元数据。

本仓库当前未声明统一的开源许可证。公开发布前，请根据你的授权意图补充 <code>LICENSE</code> 文件，并确认随 skill 分发的第三方资源符合相应许可证要求。

### 13. 作者

**圣婴**

如果你发现重构规则、编辑性判断或视觉校准流程存在可改进之处，欢迎通过 Issue 或 Pull Request 提交具体案例、输入页面、渲染结果和改进建议。

---

<a id="en"></a>

## English

### 1. Overview

<code>image-to-editable-ppt</code> is a PowerPoint reverse-reconstruction skill for multimodal AI agents.

It is designed to turn an existing slide screenshot, PNG/JPG image, or PDF page into a structured, editable, and verifiable PowerPoint source file. The goal is not to place a picture on a slide. The goal is to decompose the page into objects that can be understood, selected, edited, and reviewed:

- Text becomes editable PowerPoint text boxes or text runs;
- Color blocks, cards, borders, dividers, and containers become independent shapes;
- Directional, path-based, and compound graphics are decomposed from visible contours and local components;
- Tables and data are represented with editable tables, text, and shapes;
- Standard icons are preferably kept as independent vector objects with traceable licensing information;
- Only genuinely indivisible photos, product renders, or complex 3D visuals may remain as local image assets.

The result is intended to be a working PowerPoint source file, not a static screenshot wrapped in a <code>.pptx</code> container.

### 2. Why It Matters

#### 2.1 Turn visual references into reusable working assets

Many image-to-PPT conversions produce a single, uneditable picture. This skill preserves editability for:

- Copy, numbers, units, punctuation, and labels;
- Fonts, sizes, weights, colors, and alignment;
- Cards, blocks, borders, paths, and icons;
- Local layout, spacing, z-order, and authorized brand changes.

Reference pages can therefore be reused in proposals, bids, management reports, training programs, and other presentation workflows.

#### 2.2 Treat fidelity and editability as equal requirements

An editable file is not automatically a faithful reconstruction, and a visually similar slide is not automatically editable. The skill uses a three-part logic:

1. Inspect the actual page as visual evidence;
2. Compile each visible element into the most appropriate native PowerPoint representation;
3. Render the result, compare it with the source, and map visible differences back to specific objects.

The page is driven by its observed geometry, hierarchy, colors, contours, and negative space—not by a template name or an unverified historical implementation.

#### 2.3 Give complex graphics a controlled editing boundary

Paths, arrows, arcs, irregular boundaries, cut-outs, tips, and local components are common sources of reconstruction error. The skill distinguishes:

- Main contours;
- Open paths and centerlines;
- Tips, endpoints, shadows, markers, and other local components;
- Fill, stroke, opacity, and z-order;
- Object-level editability versus path-level editability.

This makes complex graphics easier to review and adjust without hiding structural errors inside a single image or an opaque full-page SVG.

#### 2.4 Support authorized canvas and brand transformations

After the baseline reconstruction, the skill can apply explicitly requested transformations such as:

- Adapting a page to 16:9, 4:3, or another target ratio;
- Mapping selected color roles to a corporate brand palette;
- Preserving photos, complex visuals, and explicitly protected semantic colors;
- Keeping text, hierarchy, and relative relationships unchanged unless the user authorizes a change.

Canvas adaptation is handled through spacing and layout recalculation rather than blind stretching. Color replacement is treated as a traceable mapping rather than an excuse to redesign the page.

#### 2.5 Produce results that can be checked and explained

Key decisions can be traced to an object inventory, rendered output, overlay comparison, difference artifacts, and acceptance rules. When a detail cannot be confirmed from the source page, the skill requires an explicit approximation note instead of an invented answer.

### 3. Key Features

| Feature | What it does | Practical value |
| --- | --- | --- |
| Native object reconstruction | Builds text, containers, lines, graphics, tables, and icons as separate objects | Enables direct editing and reuse |
| Visual-evidence-first analysis | Uses visible contours, colors, hierarchy, and negative space from the current page | Reduces template bias and shape misclassification |
| High-fidelity calibration | Uses rendering, transparent overlays, difference images, heatmaps, and local ROI checks | Finds misalignment, overlap, overflow, clipping, and omissions |
| Complex-shape decomposition | Falls back from preset geometry to native combinations, Custom Geometry, or independent vectors | Balances editability and geometric accuracy |
| Verbatim text preservation | Preserves case, punctuation, spaces, units, and explicit line breaks | Suitable for formal business materials |
| Controlled transformations | Supports brand color mapping, canvas-ratio changes, and adaptive whitespace | Adapts a reference without silently changing its content |
| Traceable icon sourcing | Records library, icon ID, version, license, and editability level | Supports public release and asset governance |
| Transparent capability boundaries | Separates renderability, object-level editability, and path-level editability | Prevents overclaiming |
| Bounded repair loop | Repairs only located objects and allows at most three effective rounds per page | Keeps calibration focused and repeatable |

### 4. Standard Workflow

~~~mermaid
flowchart LR
    A[Source page<br/>Image / PDF] --> B[Anchor<br/>Visual decomposition]
    B --> C[Assemble<br/>Native PPT objects]
    C --> D[Calibrate<br/>Render and compare]
    D --> E[Accept and deliver]
    D -. targeted repair .-> C
~~~

#### Step 1: Anchor — inspect the input and visual structure

- Identify page count, dimensions, clarity, and aspect ratio;
- Inspect the page and any necessary local crops;
- Create an object inventory or equivalent scene graph;
- Record each object’s type, content, bounding box, style, z-order, parent group, editability level, and uncertainty;
- Transcribe text character by character, including punctuation, spaces, units, and explicit line breaks;
- Record contours, paths, endpoints, control points, fills, strokes, and local components for graphics.

#### Step 2: Assemble — compile native PowerPoint objects

Choose the representation in this order:

1. Native preset geometry that passes a target-size rendering probe;
2. Stable combinations of native shapes;
3. PowerPoint Custom Geometry;
4. Independent vector objects;
5. Local images only for genuinely indivisible complex visuals.

Text, containers, primary structures, and tables should remain editable objects rather than full-page images or SVGs that carry the main text.

#### Step 3: Calibrate — render, overlay, and repair

- Normalize the source and the rendered PPTX to the same canvas;
- Generate a transparent overlay, a difference image, a heatmap, and machine-readable metrics;
- Inspect the canvas, containers, and primary graphics before high-risk local ROIs;
- Map differences back to specific objects instead of blindly shifting the whole page;
- Repair large structure first, then local geometry, icons, text padding, and remaining usability defects;
- Use no more than three effective repair rounds per page; stop repeating a fix when two consecutive rounds produce no meaningful improvement.

#### Step 4: Deliver — verify structure and disclose boundaries

Before delivery, verify that:

- The file opens successfully;
- Page count and canvas dimensions are correct;
- Main text can be selected and edited independently;
- Main shapes, borders, paths, tables, and icons have the correct layer relationships;
- The render has no material misalignment, overlap, overflow, clipping, omission, or distortion;
- Transformations did not alter unauthorized text, structure, or image content;
- Object-level and path-level editability are clearly distinguished;
- Uncertain details and capability gaps are disclosed.

### 5. Editability Model

| Level | Meaning |
| --- | --- |
| Text-level editability | Text is represented by a TextBox or Text Run and can be edited, restyled, or realigned |
| Object-level editability | Blocks, cards, borders, paths, icons, and local components can be selected, moved, resized, or restyled independently |
| Path-level editability | Claimed only when vector paths are reliably converted and pass rendering checks |
| Local-image exception | A photo, complex product render, or 3D illustration may remain a local image, but it must not carry reconstructable text, tables, or primary structure |

An independent SVG icon means that the icon object can be selected and adjusted independently. It does not automatically mean that every path inside the SVG can be edited separately.

### 6. Typical Use Cases

- Convert a slide screenshot, PNG, JPG, or PDF page into an editable PPTX;
- Recover editable titles, body copy, numbers, and labels from a static reference;
- Reuse the layout and graphic structure of a high-quality reference page;
- Adapt a reference to a corporate palette or a new canvas ratio;
- Reconstruct complex pages for training proposals, technical bids, management reports, and enterprise communications;
- Audit an existing PPTX for text fidelity, object independence, and visual consistency;
- Turn a static visual reference into a maintainable PowerPoint source asset.

### 7. Usage

#### In Codex

Place the skill folder in the Codex skills directory:

~~~text
%USERPROFILE%\.codex\skills\image-to-editable-ppt\
~~~

Then attach a slide image or PDF page and use a request such as:

~~~text
Reconstruct this slide image as a high-fidelity, natively editable PPTX.
Preserve the text, layout, colors, hierarchy, and graphic relationships.
Text must be editable, and blocks, borders, paths, and icons must be independently selectable.
Perform rendered overlay calibration and disclose any details that cannot be confirmed.
~~~

For a controlled transformation:

~~~text
After the baseline reconstruction, adapt the canvas to 16:9 and map the primary color to #0B5CAD.
Do not change text, structure, or image content beyond these explicitly authorized transformations.
~~~

#### Optional QA helper

The included <code>scripts/overlay_compare.py</code> helper normalizes a source page and a rendered PPTX page to the same canvas and creates overlay, difference, heatmap, and metric artifacts.

~~~bash
python scripts/overlay_compare.py --source path/to/source.png --render path/to/render.png --output-dir output/qa
~~~

It produces:

- <code>overlay.png</code> — 50% transparent overlay;
- <code>difference.png</code> — difference image;
- <code>difference-heatmap.png</code> — enhanced difference heatmap;
- <code>metrics.json</code> — canvas, scale, offset, and difference metrics.

The helper is a visual QA utility. It does not replace a PPTX writer, renderer, or structural acceptance check.

### 8. Repository Structure

~~~text
image-to-editable-ppt/
├── README.md
├── SKILL.md
├── references/
│   ├── core-reconstruction-protocol.md
│   ├── editability-contract.md
│   ├── overlay-calibration-protocol.md
│   ├── repair-registry.md
│   ├── runtime-adapter-contract.md
│   ├── shape-and-icon-protocol.md
│   ├── transformation-modules.md
│   └── verification-and-acceptance.md
└── scripts/
    └── overlay_compare.py
~~~

- <code>SKILL.md</code> contains the main agent workflow, trigger scope, and core rules;
- <code>references/</code> contains branch-specific protocols for reconstruction, editability, graphics, transformations, repairs, runtime adapters, and acceptance;
- <code>scripts/overlay_compare.py</code> provides runtime-independent visual QA support;
- <code>README.md</code> explains the project to users, collaborators, and public repository visitors.

### 9. Quality Standard

A successful output should satisfy all of the following:

1. The file opens, and page count and canvas dimensions are correct;
2. Main text matches the source and remains independently editable;
3. Main containers, borders, paths, icons, and tables are not a single flattened picture;
4. A compound graphic keeps its independently adjustable local components separate;
5. The render has no material misalignment, overlap, overflow, clipping, or omission;
6. Font attributes, size, weight, color, opacity, and alignment have been checked;
7. Source and render have been compared on a normalized canvas;
8. Icon library, ID, version, license, and editability level are traceable;
9. Every transformation is explicitly authorized;
10. Uncertain details and capability gaps are disclosed.

### 10. Scope and Boundaries

The default task is **faithful reconstruction**, not original presentation design, content rewriting, or strategic redesign.

Use a content-architecture or slide-design workflow for:

- Creating a complete presentation from scratch;
- Rewriting, restructuring, or strategically redesigning the source page;
- Placing a single image as a slide background;
- Creating a new visual style without preserving the source page’s structural relationships.

The host runtime must be able to inspect images, write native PPTX objects, render PPTX output, and perform basic structural checks. If a critical capability is missing, the result must state the verification gap rather than equating “a file was generated” with “high-fidelity conversion is complete.”

### 11. Known Limitations

- Low resolution, compression, occlusion, and missing fonts can affect text and geometry recognition;
- Font substitution may change text width, line spacing, and wrapping;
- Path-level editability depends on reliable path-conversion support in the host runtime;
- Complex photos, product renders, and 3D illustrations usually remain local image assets;
- Icon availability depends on local resources, network conditions, and licensing constraints;
- Object-level editability and path-level editability are different capabilities and should be reported separately;
- Details that cannot be confirmed from the source must be marked as approximations.

### 12. Assets and Licensing

Standard icons may be selected from candidates such as IconPark, Remix Icon, and Lucide according to visual fit, resource availability, and license traceability. For every third-party icon, retain the library, icon ID, version, license, and content hash in the task metadata.

This repository does not currently declare a single open-source license. Before public distribution, add a <code>LICENSE</code> file that matches your intended terms and verify that all bundled third-party assets comply with their licenses.

### 13. Author

**圣婴**

Suggestions are welcome through Issues or Pull Requests. When reporting a reconstruction issue, include the source page, rendered result, the affected object or region, and the proposed improvement when possible.
