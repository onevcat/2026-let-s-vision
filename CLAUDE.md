# CLAUDE.md

本文件为 Claude Code (claude.ai/code) 在此仓库中工作时提供指导。

## 项目概述

基于 Slidev 的演讲幻灯片项目，主题为「AI Agent 的道与术」（2026.03 上海）。内容涵盖 Agentic Engineering 实践——上下文工程、memory/skill 体系、以及与 AI Agent 的任务编排协作。

## 常用命令

```bash
pnpm dev        # 启动开发服务器，支持热更新（slidev --open）
pnpm build      # 构建静态站点到 .slidev-dist/
pnpm export     # 导出幻灯片为 PDF
```

## 定位 Slide

`slides.md` 约 1600 行，包含全部幻灯片。修改前可以使用索引脚本定位目标页码和行号，以加速具体页面的定位：

```bash
./scripts/slide-index.sh            # 默认读取 slides.md
```

输出为表格，包含页码（S01、S02…）、行范围、layout 和标题。

```bash
./scripts/slide-index.sh | grep S02

// 输出
// S02    78-101       default             Geek 的未来和龙虾
```

据此可快速用 `Read` 工具跳转到对应行进行编辑。

## 项目结构

- **`slides.md`** — 单文件演示文稿。每页 slide 可含独立 frontmatter、行内 `<style>`、Vue 模板语法（`v-click`、`v-if`、`:class`）及 `<!-- -->` 演讲备注。这是主要编辑对象。
- **`components/`** — 在 slide 中直接使用的 Vue 组件：
  - `TimelineStage.vue` — 时间线阶段可视化（圆点 + 标签 + 描述）
  - `StatCard.vue` — 数字统计卡片
  - `KeyPoint.vue` — 图标 + 标题 + 描述块，左侧蓝色边框强调
  - `CompareColumn.vue` — 左右对比列（`fading`/`rising`/`neutral` 三种风格）
- **`resources/`** — 参考资料（演讲笔记、观点池、slide 总览与时间分配）。不被 Slidev 直接消费，仅用于规划。
- **`public/`** — 静态资源，部署后位于根路径（如 `/avatar.jpg`）。
- **`vite.config.ts`** — 添加 `vite-svg-loader` 插件以支持内联 SVG 导入。

## 关键约定

- **主题**：`slidev-theme-penguin`，浅色模式。
- **图标**：使用 Iconify 图标集——已安装 `carbon` 和 `logos`（如 `<carbon-bot />`、`<logos-swift />`）。
- **字体**：Space Grotesk（sans）、DM Sans（serif）、Fira Code（mono），通过 Google Fonts 加载。
- **Slide 分隔**：`slides.md` 中以 `---` 分隔页面。每页的 frontmatter（layout、class、clicks、transition 等）写在 `---` 围栏之间。
- **演讲备注**：写在每页末尾的 `<!-- -->` 块中，使用中文，包含演讲节奏提示。
- **内容语言**：幻灯片可见内容中英文混用；演讲备注为中文。
- **包管理器**：pnpm。

## 能力扩展

- 推荐使用 `slidev` skill 操作和修改，特别是在 layout 和动画时，使用推荐的方式确保符合slidev最佳实践
- 在遇到排版等设计选择时，可以询问 `ui-ux-pro-max` 的意见
- 可以自行扩展 components，使用 Vue 组件呈现精致且让人惊叹的演示效果

## Design Context

### Users
技术会议（2026.03 上海）的开发者听众，多为有经验的工程师，对 AI/Agent 话题有实践兴趣。他们期望从演讲中获得可落地的 Agentic Engineering 方法论，而非概念科普。

### Brand Personality
**务实 · 前沿 · 精致**（Pragmatic · Cutting-edge · Refined）

情绪目标：理性克制的专业感打底，同时传递技术前沿的探索兴奋。不贩卖焦虑，用数据和实践说话。

### Aesthetic Direction
- **视觉基调**：简洁精致的浅色主题，注重排版细节、间距考究、层级分明
- **主色**：Teal (#14b8a6) 作为全局主题色贯穿始终；Amber 用于警示/规范/对比；Violet 用于知识/记忆相关内容
- **字体**：Space Grotesk (sans) + DM Sans (serif) + Fira Code (mono)，权重对比制造层级
- **动效**：克制有目的，用于揭示信息节奏（v-click 逐步展示），拒绝装饰性动画
- **参考方向**：Apple Keynote 的留白与节奏感，Stripe 文档的排版精度
- **反面参考**：企业蓝色渐变 PPT、彩虹配色炫技风、学术论文密排文字

### Design Principles
1. **Less but better** — 每页只传递一个核心信息，用留白而非填充来制造重点
2. **Color is intentional** — Teal 是主题色，可自由用于强调和层级；Amber/Violet 等辅助色承载语义（警示/知识），不做纯装饰用色
3. **Typography drives hierarchy** — 通过字重（600–900）和尺寸对比建立视觉层级，而非依赖色彩或边框
4. **Motion reveals, not decorates** — 动画服务于信息揭示节奏，每个动效都应有叙事目的
5. **Refined details, not complexity** — 追求间距、对齐、阴影等细节的精致，但拒绝过度设计
