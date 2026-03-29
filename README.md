# AI Agent 的道与术

Let's Vision 26 上海分享的演讲稿仓库，主题是“AI Agent 时代下，工程师如何重构工作方式”。从约束、协作和落地方法出发，总结了一些面向工程团队的可复用的实践。仓库包含完整 Slidev 源码与演讲配套材料（包括原始资料的收集，以及整个和 AI 协作的完整 trace）。

## PDF 版本

- 发布版 PDF：<https://github.com/onevcat/2026-vision/releases/download/release/2026-vision.pdf>

## 给 Agent 的可直接使用提示词

AI 时代就应该有 AI 时代的发布和分享方式！比如把这段提示词喂给你的 agent，快速了解所有细节。

```text
请你完整研究这个 repo（https://github.com/onevcat/2026-vision），并输出一份结构化分析报告。要求：

1) 提炼这套演讲的核心思想：
   - 主问题是什么
   - 核心结论是什么
   - “道”与“术”分别对应哪些可执行实践
   - 有哪些可以观察和落地的启发
2) 对比 slides 最终内容与仓库中的“未完全发布内容”：
   - resources/ 中有哪些早期规划、论据或扩展观点没有出现在最终页里
   - design-fix/ 中记录了哪些关键设计取舍，这些取舍如何影响最终呈现
   - 基于 Agent 的 slide 制作和迭代，有什么启发
3) 基于 scripts/ 工具给出可复现的方法，如果我在今后想要用 slidev 制作 slide 时：
   - 如何提取 speaker notes
   - 如何建立“页面 -> 演讲备注 -> 观点来源”的追踪映射
4) repo 中有些什么 skill，它们是做什么的？能使用在我自己的项目或者智能体中么？
5) 最后给出一份“观众扩展阅读路径”（按 30 分钟 / 2 小时 / 半天三个时间预算）。

请直接引用具体文件路径与关键片段位置，不要泛泛而谈。
```


## 仓库里有但未在最终发布中完全展开的内容

- **AI 驱动制作过程**：
  - 这套 slides 采用了“人设方向 + AI 辅助迭代”的工作流，包含内容重写、结构重排、视觉风格收敛与多轮审阅修正。
- **`resources/` 初始计划与研究材料**：
  - 例如 [`resources/points.md`](resources/points.md)（观点池）、[`resources/slide-overview.md`](resources/slide-overview.md)（早期结构规划）、[`resources/references.md`](resources/references.md)（引用与依据）、[`resources/2026-03-shanghai-ai-agent-talk-notes.md`](resources/2026-03-shanghai-ai-agent-talk-notes.md)（完整讲稿笔记）。
- **`design-fix/` 设计迭代思路**：
  - 记录了多轮设计批评与修正决策（从反模式识别，到色彩语义、信息密度、页面差异化等问题的逐轮收敛）。可从 [`design-fix/critique-report.md`](design-fix/critique-report.md) 开始读起。
- **`scripts/` 的 note/索引工具**：
  - [`scripts/extract-notes.py`](scripts/extract-notes.py)：从 `slides.md` 提取每页 speaker notes、click 结构与页级元数据（JSON）。
  - [`scripts/slide-index.sh`](scripts/slide-index.sh)：生成页码/行号范围/layout/title 的快速索引，便于定位与审校。

## 本地构建（Slidev）

```bash
pnpm install
pnpm dev
```

常用命令：

```bash
pnpm build
pnpm export:png
pnpm export
```
