---
theme: penguin
title: AI Agent 的道与术
author: Wei Wang (@onevcat)
colorSchema: light
transition: fade
fonts:
  sans: Space Grotesk
  serif: DM Sans
  mono: Fira Code
  provider: google
themeConfig:
  logoHeader: ''
  twitter: ''
  twitterUrl: ''
  eventLogo: ''
  eventUrl: ''
drawings:
  enabled: false
presenter: true
download: true
layout: default
---

# AI Agent 的道与术

Agentic Engineering 时代的工程师实践

<div class="abs-br mr-14 mb-10 flex flex-col items-end gap-2">
  <div class="text-sm opacity-60">2026.03 / Shanghai</div>
  <div class="text-xs opacity-40">Wei Wang · @onevcat</div>
</div>

<!--
开场标题页。不需要多说，直接亮出主题。
强调 Agentic Engineering 而不是 Vibe Coding —— 我们关注的是工程范式，不是工具横评。
-->

---
layout: default
---

# 从"正襟危坐"到"边炒菜边编程"

<div class="mt-8 flex items-center gap-6">
<div class="flex-1">

<v-clicks>

- 我的日常工作方式，已经发生了根本变化
- 背后不是姿势变化，而是 **agent 可达性**的跃迁
- 产出与效率出现了显著提升
- 但也带来了新的要求：**任务编排**与**验收能力**

</v-clicks>

</div>
<div class="w-60 flex items-center justify-center">
  <carbon-bot class="text-8xl text-blue-400 opacity-80" />
</div>
</div>

<!--
讲者切入，轻松趣味。

真实故事：我自己的工作方式已经从"正襟危坐写代码"变成了"边炒菜边编程"。
这背后不是在说我偷懒了，而是 agent 的可达性变了。
随时可以启动一个 agent 来帮你干活，你只需要在关键节点做验收。

但同时，对编排和验收能力的要求变高了——你得能把问题定义清楚，得能验证结果是否正确。
-->

---
layout: center
---

# 今天的输出

<div class="mt-6 text-xl text-center leading-relaxed">

**道** <carbon-arrow-right class="inline text-blue-400 mx-2" /> 约束变了什么 <span class="text-sm opacity-50">（时间点 / 资源 / 协作）</span>

<div class="my-4" />

**术** <carbon-arrow-right class="inline text-blue-400 mx-2" /> 怎么落地 <span class="text-sm opacity-50">（切分 / 上下文 / 质量 / 沉淀）</span>

</div>

<div class="mt-10 text-sm opacity-60 text-center">
  一套可执行的工程实践框架，不是工具横评
</div>

<!--
30 秒总主张。这场不是技术科普，不是产品 demo。

道：先回答约束变了什么——时间点、资源约束、协作约束。
术：再回答怎么落地——任务切分、上下文工程、质量循环、沉淀机制。

最重要的变化：开发者正在从"写实现"转向"编排系统与验收结果"。

避免工具横评；避免空泛预测。
-->

---
layout: new-section
---

# 时代判断

回顾过去不是怀旧，而是为今天的工程决策定坐标

<!--
过渡页。从开场进入第一个正式章节：时代判断。
回顾阶段不是怀旧，而是为了定位当前坐标并推断下一阶段。
-->

---
layout: default
---

# 从前、当下、将来

<div class="mt-4 flex gap-3">
  <TimelineStage label="Phase I" title="Tab 补全" v-click>
    AI 进入编码动作
  </TimelineStage>
  <TimelineStage label="Phase II" title="Chatbot" v-click>
    同步提示-响应回路
  </TimelineStage>
  <TimelineStage label="Phase III" title="AI Editor" v-click>
    仓内上下文协作
  </TimelineStage>
  <TimelineStage label="Phase IV" title="Code Agent" active v-click>
    长时任务 / 少指令 / 自主
  </TimelineStage>
</div>

<div class="mt-8 text-sm opacity-60 text-center" v-click>
  我们正处于 Phase III → IV 的转折点
</div>

<!--
四阶段统一演进图，同时涵盖机制和工具维度：

Phase I - Tab 自动补全：AI 第一次进入编码动作本身。Copilot 为代表。
Phase II - Chatbot（提示-响应）：开发者以同步回路指挥智能体。ChatGPT/Claude chat。
Phase III - AI Editor：智能体进入仓内上下文，开始参与局部执行闭环。Cursor/Windsurf。
Phase IV（进行中）- Code Agent：长时任务、少指令、人机协作跨度显著扩大。Claude Code/Codex。

三阶段机制视角同样成立：补全→同步回路→异步自主。
与智能体协作不是一次性学习，而是持续校准边界的过程。
-->

---
layout: default
---

# 当下：人开始成为瓶颈

<div class="mt-6 grid grid-cols-2 gap-8">
<div>

### 模型端 <carbon-machine-learning class="inline text-blue-500" />

<v-clicks>

- 2025 末到 2026 初：能力**台阶式**提升
- 局部场景中，模型执行速度已超过人类串行决策
- 代码生成的准确率持续攀升

</v-clicks>

</div>
<div>

### 工程师端 <carbon-user class="inline text-blue-500" />

<v-clicks>

- 价值重心正在迁移
- 写实现的成本在下降
- **定义问题 / 设边界 / 做取舍 / 做验收**<br/>成为更稀缺的能力

</v-clicks>

</div>
</div>

<!--
当下判断（2025/12 ~ 2026 初）：

模型能力台阶式提升后，局部场景里人的串行决策速度开始成为瓶颈。
这不是说人不重要了，恰恰相反——人在更高层次上变得更重要。

工程师价值重心迁移到：定义问题、设边界、做取舍、做验收。
写代码本身的成本在快速下降，但判断什么该写、怎么验证，变得更稀缺。
-->

---
layout: center
---

<div class="text-center">
  <div class="text-4xl font-bold mb-4">序章已经落下</div>
  <div class="text-lg opacity-70 max-w-lg mx-auto leading-relaxed">
    AI 能力增长超越摩尔定律，世界在加速变化
  </div>
  <div class="mt-8 text-sm opacity-50">
    不是"要不要用 AI"的问题，而是"如何用好"的问题
  </div>
</div>

<!--
整体判断：序章已经落下。

科技领域的 tick-tock 节奏在 AI 上被打破了——能力增长的速度超过了摩尔定律的预期。
世界在加速变化，这不再是"要不要用 AI"的讨论，而是"如何用好"的工程问题。

这意味着我们不能等着"AI 更好了再开始"，现在就需要建立工程化的方法。
-->

---
layout: new-section
---

# 现实证据

先证明变化确实发生，再谈方法论

<!--
过渡页。从时代判断进入现实证据。
谈方法论前要先证明"变化已发生"，否则一切都是空中楼阁。
-->

---
layout: default
---

# 规模背景

<div class="mt-8 grid grid-cols-4 gap-5">
  <StatCard value="Swift + ObjC" label="Implementation" v-click />
  <StatCard value="~235 万" label="Lines of Code" v-click />
  <StatCard value="~650" label="Modules" v-click />
  <StatCard value="~25,000" label="Files" v-click />
</div>

<div class="mt-8 text-sm opacity-60 text-center" v-click>
  这个规模决定了单 agent 很难稳定覆盖全局，需要系统化的工程方法
</div>

<!--
规模背景（脱敏数据）。

用来建立"问题难度感"：
- 实现语言：Swift + Objective-C
- 代码行数：约 235 万
- 模块数：约 650
- 文件数：约 25,000

这个规模下，任何一次改动都可能影响多个模块。
单个 agent 很难稳定覆盖全局，需要系统化的工程方法。

注意：只展示趋势，不给绝对值。完全脱敏，不可回推。
-->

---
layout: default
---

# PR 趋势 <carbon-chart-line class="inline text-blue-500" />

<div class="mt-6 flex items-center gap-8">
<div class="flex-1">

<v-clicks>

- 产出速度明显加快
- 但 review / 验收 / 质量控制形态也在**同步重构**
- 不是简单的"多了"，而是生产模式在变

</v-clicks>

</div>
<div class="w-80 h-48 rounded-xl bg-gradient-to-br from-blue-50 to-indigo-50 border border-blue-100 flex items-center justify-center">
  <div class="text-sm opacity-40">[PR Trend Chart]</div>
</div>
</div>

<!--
PR 趋势图（第一张趋势图）。

核心信息：产出变快了，但不只是数量变化。
review 方式、验收标准、质量控制的形态都在同步重构。
以前一个人写完提 PR 等 review。
现在可能是 agent 写完，人来 review，但 review 的内容和方式都不一样了。

只展示趋势线，不标绝对值。
-->

---
layout: default
---

# Backlog 与 AI 使用趋势

<div class="mt-4 grid grid-cols-2 gap-8">
<div>

### Issue / Backlog <carbon-task-complete class="inline text-green-500" />

<v-clicks>

- 启动成本下降
- 但**不等于**自动清空 backlog
- 问题定义质量决定消化速度

</v-clicks>

</div>
<div>

### AI 高使用占比 <carbon-growth class="inline text-orange-500" />

<v-clicks>

- 先出现**高手飞轮**效应
- 少数人的效率提升 10x 甚至 100x
- 关键问题：能否组织化扩散？

</v-clicks>

</div>
</div>

<!--
两张趋势图合并讲。

Issue/backlog 趋势：启动成本下降了（因为可以更快地开始做一个任务），
但不等于 backlog 自动减少——如果问题定义不清楚，agent 也帮不上忙。

AI 高使用占比趋势：先出现"高手飞轮"——
少数善于使用 AI 的工程师效率飙升（10x 甚至 100x）。
关键问题是，这种能力能否从个人扩散为组织能力。
如果不能扩散，就会形成 AI 格差。

所有数据：只讲趋势不讲绝对值；不展示可回推信息。
-->

---
layout: new-section
---

# 道

新世界的底层约束

<!--
过渡页。证据层成立后，进入"道"——底层约束。
道负责回答：约束变了什么，判断框架是什么。
-->

---
layout: default
---

# 三个约束，一个方向

<div class="mt-6 grid grid-cols-2 gap-6">

<div>

<KeyPoint title="Context = 内存" v-click>
  <template #icon><carbon-chip class="text-2xl" /></template>
  有限、紧张、需要预算
</KeyPoint>

<div class="h-4" />

<KeyPoint title="Memory + Skill = 复利" v-click>
  <template #icon><carbon-save class="text-2xl" /></template>
  没有记忆，成功经验无法复用
</KeyPoint>

<div class="h-4" />

<KeyPoint title="协作范式在变" v-click>
  <template #icon><carbon-collaborate class="text-2xl" /></template>
  从人指挥 agent 到 agent 自协作
</KeyPoint>

</div>

<div class="flex items-center justify-center" v-click>
<div class="text-center p-8 rounded-2xl bg-gradient-to-br from-blue-50 to-indigo-50 border border-blue-100">
  <div class="text-sm opacity-60 mb-2">方向</div>
  <div class="text-xl font-bold text-blue-700">to-Human → to-Agent</div>
  <div class="text-xs opacity-50 mt-2">Agent 正在成为软件的新用户</div>
</div>
</div>

</div>

<!--
道的总览：三个约束 + 一个方向。

三个约束：
1. context = 内存：有限、紧张、需要预算
2. memory + skill = 复利：没有记忆系统，成功经验无法跨任务复用
3. 协作范式在变：从人指挥多 agent 到多 agent 自协作

一个方向：2A（Develop for Agent）—— Agent 正在成为软件的新用户。
人类要的是结果，不是软件操作过程。
-->

---
layout: center
---

<div class="text-center">
  <carbon-user-favorite class="text-5xl text-blue-500 mb-4 mx-auto" />
  <div class="text-3xl font-bold mb-4">人类要的是结果</div>
  <div class="text-3xl font-bold opacity-40 line-through mb-6">不是软件操作过程</div>
  <div class="text-base opacity-60 max-w-md mx-auto leading-relaxed">
    软件设计正在从 to-Human 走向 to-Agent，<br/>
    平台能力与权限审计成为新的竞争关键
  </div>
</div>

<!--
目标定义页。

核心观点：人类要的是结果，不是软件操作过程。
这是 2A (Develop for Agent) 的底层逻辑。

Agent 正在成为软件的新用户。
当 agent 可以代替人来操作软件时，
软件的设计目标就需要从"让人用着方便"转向"让 agent 能高效执行"。

平台能力、权限审计、可观测性、流程自动化会成为企业竞争关键。
-->

---
layout: default
---

# 约束一：Context = 内存

<div class="mt-6 flex items-center gap-8">
<div class="flex-1">

<v-clicks>

- 上下文不是免费的聊天历史
- 而是**有限、紧张、需要预算**的内存
- 关键问题不是"喂多少"，而是"**喂什么、按什么顺序**"

</v-clicks>

<div class="mt-6 p-4 rounded-lg bg-amber-50 border border-amber-200" v-click>
  <div class="text-sm font-semibold text-amber-800">
    <carbon-warning class="inline mr-1" /> 瓶颈迁移
  </div>
  <div class="text-xs text-amber-700 mt-1">
    从"代码/文档同步"迁移到"上下文窗口 + 跨 session 连续性"
  </div>
</div>

</div>
<div class="w-44 flex items-center justify-center">
  <carbon-chip class="text-8xl text-blue-300 opacity-60" />
</div>
</div>

<!--
约束一深入。

在 agent 开发里，上下文是最贵的资源，不是免费的聊天历史。
context 是有限、紧张、需要预算的内存。

关键问题不是"喂多少"，而是"喂什么、按什么顺序喂"。
如何让 Agent 每次拿到正确上下文，处理正确尺寸的问题。

软件工程瓶颈从"代码/文档同步"迁移到"上下文窗口 + 跨 session 连续性"。
-->

---
layout: default
---

# 上下文的三个风险

<div class="mt-8 grid grid-cols-3 gap-6">

<div class="text-center p-6 rounded-xl bg-red-50 border border-red-100" v-click>
  <carbon-misuse class="text-3xl text-red-400 mb-3" />
  <div class="font-bold text-red-800 mb-2">上下文漂移</div>
  <div class="text-xs text-red-600 leading-relaxed">
    对话过长后，模型注意力偏移，丢失早期关键信息
  </div>
</div>

<div class="text-center p-6 rounded-xl bg-orange-50 border border-orange-100" v-click>
  <carbon-unlink class="text-3xl text-orange-400 mb-3" />
  <div class="font-bold text-orange-800 mb-2">跨 Session 断裂</div>
  <div class="text-xs text-orange-600 leading-relaxed">
    新会话无法继承上一次的上下文与决策链路
  </div>
</div>

<div class="text-center p-6 rounded-xl bg-yellow-50 border border-yellow-100" v-click>
  <carbon-close-outline class="text-3xl text-yellow-500 mb-3" />
  <div class="font-bold text-yellow-800 mb-2">关键决策丢失</div>
  <div class="text-xs text-yellow-600 leading-relaxed">
    "为什么这样做"的理由没有持久化，导致重复踩坑
  </div>
</div>

</div>

<!--
约束一延伸：上下文的三个风险。

1. 上下文漂移：对话太长后，模型注意力偏移，早期的关键信息可能被忽略。
2. 跨 session 断裂：新的会话无法继承上一次的上下文与决策链路。每次重新解释太浪费。
3. 关键决策丢失："为什么这样做"的理由没有被持久化，导致团队重复踩坑。

这三个风险共同指向一个需求：需要体系化的 memory 机制。
-->

---
layout: default
---

# 约束二：Memory + Skill = 复利

<div class="mt-6 grid grid-cols-2 gap-6">
<div>

### 个人 Memory <carbon-user class="inline text-blue-500" />

<v-clicks>

- 偏好、约束、踩坑、决策理由
- 减少重复沟通与重复踩坑
- 让 agent 越来越"懂你"

</v-clicks>

</div>
<div>

### 团队 Memory <carbon-group class="inline text-blue-500" />

<v-clicks>

- 把个人技巧沉淀为**可复用资产**
- Skill 化：一次成功 → 模板 / runbook / 脚手架
- **渐进式披露**：在不同阶段给 agent 恰当信息

</v-clicks>

</div>
</div>

<div class="mt-6 text-center text-sm opacity-60" v-click>
  没有记忆系统，就没有 AI 协作的长期复利
</div>

<!--
约束二：Memory + Skill 决定复利。

个人 memory：记住偏好、约束、踩过的坑、关键决策理由。
减少重复沟通与重复踩坑，让 agent 越来越"懂你"。

团队 memory：把个人经验变成组织资产。
skill 化目标：把一次成功转为模板、runbook、脚手架。

本质都是"渐进式披露（progressive disclosure）"的实践：
在不同阶段给 agent 恰当粒度的信息与能力。
-->

---
layout: default
---

# 组织挑战：高手飞轮 vs 团队断层

<div class="mt-6 flex items-center gap-8">
<div class="flex-1">

<v-clicks>

- 少数人的 AI 使用能力极强，效率提升显著
- 但 **AI 使用能力高度个体化**
- 个人强 ≠ 组织强

</v-clicks>

<div class="mt-6" v-click>

### 关键观察

- 实践推广大多是**自下而上**的
- 个体高手经验 → 团队共识
- 传统自上而下路径在这个周期里偏慢

</div>

</div>
<div class="w-48 flex flex-col items-center gap-3">
  <div class="px-4 py-2 rounded-lg bg-blue-100 text-blue-800 text-sm font-bold">
    <carbon-events class="inline mr-1" /> 少数高手
  </div>
  <carbon-arrow-down class="text-xl text-gray-400" />
  <div class="px-4 py-2 rounded-lg bg-green-100 text-green-800 text-sm font-bold">
    <carbon-group class="inline mr-1" /> 团队共识
  </div>
  <carbon-arrow-down class="text-xl text-gray-400" />
  <div class="px-4 py-2 rounded-lg bg-purple-100 text-purple-800 text-sm font-bold">
    <carbon-enterprise class="inline mr-1" /> 组织能力
  </div>
</div>
</div>

<!--
公司观察：高手飞轮 vs 团队断层。

AI 时代常见组织问题是"少数人飞起、多数人观望"的效率断层。
AI 使用能力高度个体化，个人强不等于组织强。
个性化 AI 可能提高个人效率，但会加剧团队共识碎片化风险。

关键观察：这类实践推广大多是自下而上的（个体高手经验 -> 团队共识）。
传统自上而下路径在这个周期里通常偏慢。
团队实践最重要的是如何让少数人带动多数人。
-->

---
layout: default
---

# 约束三：协作范式在变

<div class="mt-6">

<div class="grid grid-cols-2 gap-8">
<div class="p-6 rounded-xl bg-gray-50 border border-gray-200 text-center" v-click>
  <div class="text-sm opacity-60 mb-2">当前</div>
  <div class="text-lg font-bold mb-3">人 → 多 Agent</div>
  <carbon-user class="text-2xl text-blue-500 mx-1" />
  <carbon-arrow-right class="text-xl text-gray-400 mx-1" />
  <carbon-bot class="text-2xl text-gray-500 mx-1" />
  <carbon-bot class="text-2xl text-gray-500 mx-1" />
  <carbon-bot class="text-2xl text-gray-500 mx-1" />
  <div class="text-xs opacity-50 mt-3">人工编排，注意力是瓶颈</div>
</div>

<div class="p-6 rounded-xl bg-blue-50 border border-blue-200 text-center" v-click>
  <div class="text-sm text-blue-600 mb-2">下一阶段</div>
  <div class="text-lg font-bold text-blue-800 mb-3">Agent ↔ Agent</div>
  <carbon-bot class="text-2xl text-blue-500 mx-1" />
  <carbon-connect class="text-xl text-blue-400 mx-1" />
  <carbon-bot class="text-2xl text-blue-500 mx-1" />
  <carbon-connect class="text-xl text-blue-400 mx-1" />
  <carbon-bot class="text-2xl text-blue-500 mx-1" />
  <div class="text-xs text-blue-600 mt-3">自协作，人做策略与兜底</div>
</div>
</div>

<div class="mt-6 text-center text-sm opacity-60" v-click>
  直接驱动因子：开发者注意力稀缺
</div>

</div>

<!--
约束三：协作范式在变。

当前在卷"人指挥多 agent"——因为开发者注意力是稀缺资源。
典型场景：你同时开几个 agent，一个查代码，一个写实现，一个跑测试。
但这种手动编排多个 agent 是过渡态。

下一阶段会走向"多个智能体自行协作工作"——
人类更多做策略设定与异常兜底。
10x 开发者是人指挥多 agent，但"人均 10x"需要 agent 自协作。
-->

---
layout: default
---

# 跨越点：人工监督 → 无人职守

<div class="mt-6">

<div class="flex items-center justify-center gap-4 mb-6">
  <div class="px-5 py-3 rounded-xl bg-gray-100 font-bold">
    <carbon-view class="inline mr-1 text-gray-600" /> 人工监督
  </div>
  <div class="flex flex-col items-center">
    <carbon-arrow-right class="text-3xl text-blue-500" />
    <div class="text-xs text-blue-600 font-semibold mt-1">关键跨越</div>
  </div>
  <div class="px-5 py-3 rounded-xl bg-blue-600 text-white font-bold">
    <carbon-workflow-automation class="inline mr-1" /> 无人职守
  </div>
</div>

<div class="grid grid-cols-3 gap-4" v-click>
<div class="p-4 rounded-lg bg-gray-50 border border-gray-200 text-center">
  <carbon-webhook class="text-2xl text-purple-500 mb-2" />
  <div class="text-sm font-semibold">Webhook</div>
  <div class="text-xs opacity-50">事件触发</div>
</div>
<div class="p-4 rounded-lg bg-gray-50 border border-gray-200 text-center">
  <carbon-time class="text-2xl text-green-500 mb-2" />
  <div class="text-sm font-semibold">Cron</div>
  <div class="text-xs opacity-50">定时触发</div>
</div>
<div class="p-4 rounded-lg bg-gray-50 border border-gray-200 text-center">
  <carbon-flow class="text-2xl text-orange-500 mb-2" />
  <div class="text-sm font-semibold">Event Pipeline</div>
  <div class="text-xs opacity-50">流水线触发</div>
</div>
</div>

<div class="mt-6 p-3 rounded-lg bg-amber-50 border border-amber-200 text-xs text-amber-800" v-click>
  <carbon-warning class="inline mr-1" /> 风险提示：在极端自动化闭环里，人可能被挤出执行环节，只保留责任承担角色。跨过这条线，就回不了头了。
</div>

</div>

<!--
跨越点：从人工监督到无人职守。

这是智能体工程化最关键的一次跨越。跨过这条线，就回不了头了。

典型触发方式：
- Webhook：事件驱动，PR 提交后自动 review
- Cron：定时触发，每天自动清理 backlog
- Event Pipeline：流水线触发，CI 失败后自动修复

风险提示：在极端自动化闭环里，人可能被挤出执行环节，只保留责任承担角色。
主力 agent 逐步从 local 迁移到云端持续运行环境。

趋势判断：agent 云端化与"随时随地可达"的形态。
-->

---
layout: default
---

# 战略落点

<div class="mt-8 grid grid-cols-2 gap-5">

<KeyPoint title="平台能力" v-click>
  <template #icon><carbon-cloud-services class="text-2xl" /></template>
  构建 agent 可调用的服务层
</KeyPoint>

<KeyPoint title="权限审计" v-click>
  <template #icon><carbon-locked class="text-2xl" /></template>
  Agent 代理人类执行时的权限边界与审计
</KeyPoint>

<KeyPoint title="可观测性" v-click>
  <template #icon><carbon-dashboard class="text-2xl" /></template>
  Agent 行为的监控、日志与回溯
</KeyPoint>

<KeyPoint title="流程自动化" v-click>
  <template #icon><carbon-flow-modeler class="text-2xl" /></template>
  从手动触发到事件驱动的全链路
</KeyPoint>

</div>

<div class="mt-6 text-center text-sm opacity-60" v-click>
  这些将成为企业级 AI 工程化的竞争关键
</div>

<!--
战略落点。

如果约束判断成立，那企业需要在四个方面构建能力：
1. 平台能力：构建 agent 可调用的服务层，而不是只给人用的 UI
2. 权限审计：Agent 代理人类执行时的权限边界与审计链路
3. 可观测性：Agent 行为的监控、日志与回溯能力
4. 流程自动化：从手动触发到事件驱动的全链路自动化

这些不是"未来的事"，而是现在就需要开始投入的基础设施。
-->

---
layout: new-section
---

# 术

企业可落地的实践框架

<!--
过渡页。约束明确后，进入"术"——如何把系统搭起来。
术负责回答：怎么落地、怎么复用。
-->

---
layout: default
---

# 三个支柱

<div class="mt-8 flex items-center justify-center gap-6">

<div class="text-center p-6 rounded-2xl bg-gradient-to-b from-blue-50 to-blue-100 border border-blue-200 w-56" v-click>
  <carbon-task class="text-4xl text-blue-600 mb-3" />
  <div class="text-lg font-bold text-blue-800">任务切分</div>
  <div class="text-xs opacity-60 mt-2">可验收的交付单元</div>
</div>

<div class="text-center p-6 rounded-2xl bg-gradient-to-b from-indigo-50 to-indigo-100 border border-indigo-200 w-56" v-click>
  <carbon-data-structured class="text-4xl text-indigo-600 mb-3" />
  <div class="text-lg font-bold text-indigo-800">上下文工程</div>
  <div class="text-xs opacity-60 mt-2">喂对信息，不喂多信息</div>
</div>

<div class="text-center p-6 rounded-2xl bg-gradient-to-b from-purple-50 to-purple-100 border border-purple-200 w-56" v-click>
  <carbon-renew class="text-4xl text-purple-600 mb-3" />
  <div class="text-lg font-bold text-purple-800">质量循环</div>
  <div class="text-xs opacity-60 mt-2">变更 → 证据 → 回归 → 沉淀</div>
</div>

</div>

<!--
术的总览：三个支柱。

1. 任务切分：让 agent 接受"可验收交付单元"，不是模糊需求
2. 上下文工程：喂对信息，不喂多信息
3. 质量循环：变更 → 证据 → 回归 → 沉淀

这三个支柱构成一个闭环：
切分好任务 → 给对上下文 → 执行后验证 → 沉淀经验。
-->

---
layout: default
---

# 任务切分：可验收交付单元

<div class="mt-6">

<div class="text-base mb-6">让 agent 接受的不是模糊需求，而是<strong>可验收的工作单元</strong></div>

<div class="grid grid-cols-4 gap-4" v-click>
<div class="p-4 rounded-xl bg-gray-50 border border-gray-200 text-center">
  <carbon-pull-request class="text-2xl text-blue-500 mb-2" />
  <div class="text-sm font-bold">PR</div>
</div>
<div class="p-4 rounded-xl bg-gray-50 border border-gray-200 text-center">
  <carbon-code class="text-2xl text-green-500 mb-2" />
  <div class="text-sm font-bold">Patch</div>
</div>
<div class="p-4 rounded-xl bg-gray-50 border border-gray-200 text-center">
  <carbon-application class="text-2xl text-purple-500 mb-2" />
  <div class="text-sm font-bold">Demo</div>
</div>
<div class="p-4 rounded-xl bg-gray-50 border border-gray-200 text-center">
  <carbon-document class="text-2xl text-orange-500 mb-2" />
  <div class="text-sm font-bold">Reply Draft</div>
</div>
</div>

<div class="mt-6 p-4 rounded-lg bg-blue-50 border border-blue-100" v-click>
  <div class="text-sm font-semibold text-blue-800 mb-1">
    <carbon-transform-instructions class="inline mr-1" /> 角色转变
  </div>
  <div class="text-xs text-blue-700">
    工程师从"亲自实现者"转向"任务编排 + 质量守门"
  </div>
</div>

</div>

<!--
任务切分：可验收交付单元。

先定义交付物：PR / patch / demo / 回复草稿。
每种交付物都有明确的"完成"标准。

关键是让 agent 接受的不是"帮我改一下这个功能"这种模糊需求，
而是"生成一个 PR，包含这些改动，通过这些测试"。

工程师角色转变：从"亲自实现"转向"任务编排 + 质量守门"。
-->

---
layout: default
---

# 验收前置

<div class="mt-6">

<div class="text-base mb-4">先定义"怎么算做完"，再开始做</div>

<div class="grid grid-cols-4 gap-4">

<div class="p-4 rounded-xl border border-green-200 bg-green-50" v-click>
  <carbon-checkmark-filled class="text-xl text-green-600 mb-2" />
  <div class="text-sm font-bold text-green-800">测试</div>
  <div class="text-xs text-green-600 mt-1">单元 / 集成 / UI</div>
</div>

<div class="p-4 rounded-xl border border-blue-200 bg-blue-50" v-click>
  <carbon-catalog class="text-xl text-blue-600 mb-2" />
  <div class="text-sm font-bold text-blue-800">日志</div>
  <div class="text-xs text-blue-600 mt-1">行为链路可追溯</div>
</div>

<div class="p-4 rounded-xl border border-orange-200 bg-orange-50" v-click>
  <carbon-undo class="text-xl text-orange-600 mb-2" />
  <div class="text-sm font-bold text-orange-800">回滚</div>
  <div class="text-xs text-orange-600 mt-1">可逆性保障</div>
</div>

<div class="p-4 rounded-xl border border-red-200 bg-red-50" v-click>
  <carbon-warning-alt class="text-xl text-red-600 mb-2" />
  <div class="text-sm font-bold text-red-800">风险列表</div>
  <div class="text-xs text-red-600 mt-1">已知风险前置声明</div>
</div>

</div>

<div class="mt-8 text-center text-sm opacity-60" v-click>
  验收标准前置 = 减少返工 + 提高 agent 产出可信度
</div>

</div>

<!--
验收前置：先定义"怎么算做完"，再开始做。

验收标准要前置定义：
- 测试：单元/集成/UI 测试覆盖
- 日志：行为链路可追溯
- 回滚：可逆性保障，出问题能回退
- 风险列表：已知风险前置声明

验收标准前置的好处：减少返工 + 提高 agent 产出的可信度。
如果你不告诉 agent 怎么验证，它就不会自验。
-->

---
layout: default
---

# 上下文工程

<div class="mt-4 text-base mb-6">效果差异来自上下文与执行容器，不来自提示词技巧</div>

<div class="grid grid-cols-2 gap-6">
<div>

### 可控注入源 <carbon-document-import class="inline text-blue-500" />

<v-clicks>

- README / 架构图
- 关键文件清单
- 约束清单（CLAUDE.md / AGENTS.md）
- 保持**精确精简**，只提项目领域知识

</v-clicks>

</div>
<div>

### 注意事项 <carbon-warning class="inline text-orange-500" />

<v-clicks>

- 无关历史会**污染**模型注意力
- 模型注意力分布：开头 + 最近 > 中段
- 工程上下文与聊天历史要隔离
- 过度省成本选低质量模型 → **错误学习**

</v-clicks>

</div>
</div>

<!--
上下文工程。

核心观点：效果差异主要来自上下文与执行容器，不来自提示词技巧。

可控注入源优先：
- README、架构图、关键文件、约束清单
- CLAUDE.md / AGENTS.md 等保持精确精简，只提项目领域知识而不要提通识

注意事项：
- 无关聊天历史会污染上下文，应与工程上下文隔离
- 模型注意力常见分布：开头部分和最近部分较强，中间部分是衰减区
- 过度为省钱选择低质量模型，常会导致"学到错误教训"，长期更贵
-->

---
layout: center
---

<div class="text-center">
  <div class="text-lg opacity-60 mb-4">模型注意力分布</div>
  <div class="flex items-end justify-center gap-1 h-32">
    <div class="w-8 bg-blue-500 rounded-t" style="height: 90%"></div>
    <div class="w-8 bg-blue-400 rounded-t" style="height: 75%"></div>
    <div class="w-8 bg-blue-300 rounded-t" style="height: 50%"></div>
    <div class="w-8 bg-blue-200 rounded-t" style="height: 35%"></div>
    <div class="w-8 bg-gray-200 rounded-t" style="height: 25%"></div>
    <div class="w-8 bg-gray-200 rounded-t" style="height: 20%"></div>
    <div class="w-8 bg-gray-200 rounded-t" style="height: 18%"></div>
    <div class="w-8 bg-gray-200 rounded-t" style="height: 20%"></div>
    <div class="w-8 bg-gray-200 rounded-t" style="height: 25%"></div>
    <div class="w-8 bg-blue-200 rounded-t" style="height: 35%"></div>
    <div class="w-8 bg-blue-300 rounded-t" style="height: 55%"></div>
    <div class="w-8 bg-blue-400 rounded-t" style="height: 70%"></div>
    <div class="w-8 bg-blue-500 rounded-t" style="height: 85%"></div>
  </div>
  <div class="flex justify-between text-xs opacity-50 mt-2 px-4 max-w-sm mx-auto">
    <span>开头（强）</span>
    <span>中段（弱）</span>
    <span>最近（强）</span>
  </div>
  <div class="mt-6 text-sm opacity-60">
    把关键信息放在<strong>开头和最近位置</strong>，避免埋在中段
  </div>
</div>

<!--
注意力与污染。

模型注意力常见分布：开头和最近的内容获得更强注意力，中段容易衰减。
这意味着：
- 关键约束和规则应该放在上下文的开头
- 当前任务描述放在最近的位置
- 避免把重要信息埋在长对话的中间

实际操作：定期清理上下文，把核心信息重新注入。
-->

---
layout: default
---

# Harness 策略

<div class="mt-6 flex items-center gap-8">
<div class="flex-1">

<v-clicks>

- **不绑定**单一 harness
- 允许并鼓励多 harness 并存
- 必要时打造适合自身团队的 harness

</v-clicks>

<div class="mt-6 grid grid-cols-3 gap-3" v-click>
<div class="p-3 rounded-lg bg-gray-50 border text-center text-xs">
  <div class="font-bold mb-1">IDE 集成</div>
  <span class="opacity-60">日常开发</span>
</div>
<div class="p-3 rounded-lg bg-gray-50 border text-center text-xs">
  <div class="font-bold mb-1">CLI Agent</div>
  <span class="opacity-60">批量/自动化</span>
</div>
<div class="p-3 rounded-lg bg-gray-50 border text-center text-xs">
  <div class="font-bold mb-1">Custom Harness</div>
  <span class="opacity-60">团队特化</span>
</div>
</div>

</div>
<div class="w-40 flex items-center justify-center">
  <carbon-settings-adjust class="text-7xl text-indigo-300 opacity-60" />
</div>
</div>

<!--
Harness 策略。

不宜与单一 harness 绑定；应习惯并容许多 harness 并存，必要时打造适合自身团队的 harness。

不同场景适合不同 harness：
- IDE 集成（如 Cursor）：日常开发，快速迭代
- CLI Agent（如 Claude Code）：批量任务，自动化流程
- Custom Harness：团队特化，针对特定工作流定制

关键是 harness 要适配团队的工作流程，而不是反过来。
-->

---
layout: default
---

# Skill 沉淀

<div class="mt-6">

<div class="text-base mb-6">每次成功都可以沉淀为可复用路径</div>

<div class="flex items-center justify-center gap-4 mb-8" v-click>
  <div class="px-4 py-2 rounded-lg bg-blue-100 text-blue-800 text-sm font-semibold">
    一次成功
  </div>
  <carbon-arrow-right class="text-xl text-gray-400" />
  <div class="px-4 py-2 rounded-lg bg-indigo-100 text-indigo-800 text-sm font-semibold">
    Skill 化
  </div>
  <carbon-arrow-right class="text-xl text-gray-400" />
  <div class="px-4 py-2 rounded-lg bg-purple-100 text-purple-800 text-sm font-semibold">
    团队复用
  </div>
  <carbon-arrow-right class="text-xl text-gray-400" />
  <div class="px-4 py-2 rounded-lg bg-green-100 text-green-800 text-sm font-semibold">
    节省 Token
  </div>
</div>

<div class="grid grid-cols-4 gap-3" v-click>
<div class="p-3 rounded-lg bg-gray-50 border text-center text-xs">
  <carbon-template class="text-xl text-blue-500 mb-1" />
  <div class="font-bold">模板</div>
</div>
<div class="p-3 rounded-lg bg-gray-50 border text-center text-xs">
  <carbon-notebook class="text-xl text-green-500 mb-1" />
  <div class="font-bold">Runbook</div>
</div>
<div class="p-3 rounded-lg bg-gray-50 border text-center text-xs">
  <carbon-document class="text-xl text-purple-500 mb-1" />
  <div class="font-bold">FAQ</div>
</div>
<div class="p-3 rounded-lg bg-gray-50 border text-center text-xs">
  <carbon-build-tool class="text-xl text-orange-500 mb-1" />
  <div class="font-bold">脚手架</div>
</div>
</div>

</div>

<!--
Skill 沉淀收益。

流程 skill 化可节省 token 与重复试错成本。
每次成功都可以沉淀为 skill：

- 模板：标准化的任务描述模板
- Runbook：标准化的操作手册
- FAQ：常见问题的标准解答
- 脚手架：快速启动新项目/新任务的起点

一次成功 → skill 化 → 团队复用 → 节省 token 和试错成本。
这是从个人能力到组织能力的桥梁。
-->

---
layout: two-cols-header
---

# 工程价值重排

::left::

<CompareColumn title="正在弱化" variant="fading">
  <template #icon><carbon-arrow-down class="text-red-500" /></template>
  <v-clicks>

  - **DRY** 的边际价值下降<br/><span class="text-xs opacity-60">局部重复换取可理解性有时更优</span>
  - 手写代码的**稀缺性**下降<br/><span class="text-xs opacity-60">代码本身不再是核心壁垒</span>
  - 传统 code review 形态需要**重构**<br/><span class="text-xs opacity-60">从逐行审阅到意图+结果验证</span>

  </v-clicks>
</CompareColumn>

::right::

<CompareColumn title="正在增强" variant="rising">
  <template #icon><carbon-arrow-up class="text-green-500" /></template>
  <v-clicks>

  - **提早优化**在部分场景反而更重要<br/><span class="text-xs opacity-60">Agent 执行时不会"先跑通再优化"</span>
  - Feature / UI 测试的维护成本**显著下降**<br/><span class="text-xs opacity-60">自动化回归边界大幅扩大</span>
  - **TDD** 缩短试错回路<br/><span class="text-xs opacity-60">提高可验证性</span>

  </v-clicks>
</CompareColumn>

<!--
工程价值重排（旧观点变化 vs 既有实践增强）。

正在弱化：
- DRY 边际价值下降：局部重复换取可理解性有时更优
- 手写代码的稀缺性下降：代码本身不再是核心壁垒
- 传统 code review 形态需要重构：从逐行审阅到意图+结果验证

正在增强：
- 过去被视为不经济的"提早优化"，在部分场景反而更重要
- Feature/UI 测试的维护成本下降，自动化回归边界扩大
- TDD 缩短试错回路，提高可验证性

AI 变强后，不是"少做工程"，而是"重排工程优先级"。
-->

---
layout: default
---

# 既有实践的新价值

<div class="mt-6 grid grid-cols-2 gap-5">

<KeyPoint title="可观测性" v-click>
  <template #icon><carbon-dashboard class="text-2xl" /></template>
  测试覆盖、数量与质量指标，让产出可度量
</KeyPoint>

<KeyPoint title="TDD" v-click>
  <template #icon><carbon-checkmark-outline class="text-2xl" /></template>
  缩短试错回路，为 agent 提供即时反馈
</KeyPoint>

<KeyPoint title="Benchmark" v-click>
  <template #icon><carbon-meter class="text-2xl" /></template>
  把性能与成本讨论从"感觉"变成"数据"
</KeyPoint>

<KeyPoint title="可验证循环" v-click>
  <template #icon><carbon-renew class="text-2xl" /></template>
  变更 → 证据 → 回归 → 沉淀
</KeyPoint>

</div>

<div class="mt-6 text-center text-sm opacity-60" v-click>
  AI 变强后，不是"少做工程"，而是"重排工程优先级"
</div>

<!--
既有实践的新价值。

可观测性（测试覆盖、数量与质量指标）：让产出可度量。
TDD：缩短试错回路，为 agent 提供即时反馈信号。
Benchmark：把性能与成本讨论从"感觉"变成"数据"。
可验证循环：变更 → 证据 → 回归 → 沉淀。

这些不是新概念，但在 AI 时代它们的价值被放大了。
因为 agent 需要明确的验证信号才能自我修正。
-->

---
layout: new-section
---

# 案例

不是"AI 很神"，而是"流程如何标准化和沉淀"

<!--
过渡页。讲完术，不靠口号，直接看两个案例。
案例不该只讲"AI 很神"，而应讲"流程如何被标准化和沉淀"。
-->

---
layout: default
---

# 大规模代码库中的 Subagent 协作

<div class="mt-4 text-sm opacity-70 mb-6">多语言、多模块、超大仓库 —— 单 agent 很难稳定覆盖</div>

<div class="flex items-center justify-center gap-3 mt-4" v-click>
  <div class="p-4 rounded-xl bg-blue-50 border border-blue-200 text-center w-36">
    <carbon-search class="text-2xl text-blue-600 mb-2" />
    <div class="text-sm font-bold">检索 Agent</div>
    <div class="text-xs opacity-60">定位相关代码</div>
  </div>
  <carbon-arrow-right class="text-xl text-gray-400" />
  <div class="p-4 rounded-xl bg-green-50 border border-green-200 text-center w-36">
    <carbon-edit class="text-2xl text-green-600 mb-2" />
    <div class="text-sm font-bold">改动 Agent</div>
    <div class="text-xs opacity-60">执行代码修改</div>
  </div>
  <carbon-arrow-right class="text-xl text-gray-400" />
  <div class="p-4 rounded-xl bg-purple-50 border border-purple-200 text-center w-36">
    <carbon-checkmark-filled class="text-2xl text-purple-600 mb-2" />
    <div class="text-sm font-bold">验证 Agent</div>
    <div class="text-xs opacity-60">测试与回归</div>
  </div>
</div>

<div class="flex items-center justify-center mt-4" v-click>
  <div class="p-3 rounded-xl bg-indigo-50 border border-indigo-200 text-center w-52">
    <carbon-center-to-fit class="text-2xl text-indigo-600 mb-1" />
    <div class="text-sm font-bold">主 Agent 汇总决策</div>
  </div>
</div>

<!--
高层案例 - 场景与方案。

场景：多语言、多模块、超大仓库，单 agent 很难稳定覆盖。
方案：按模块/职责拆分 subagent。

分工：
- 检索 Agent：定位相关代码和上下文
- 改动 Agent：执行具体的代码修改
- 验证 Agent：运行测试、做回归检查
- 主 Agent：汇总各 subagent 的结果，做最终决策

价值：并行度提升、责任边界清晰、协作模板可复制。
这是"注意力稀缺 + context 有限"下的工程化解法。
-->

---
layout: default
---

# Subagent 协作价值

<div class="mt-6 grid grid-cols-3 gap-5">

<div class="p-5 rounded-xl bg-blue-50 border border-blue-100 text-center" v-click>
  <carbon-increase-level class="text-3xl text-blue-600 mb-3" />
  <div class="font-bold text-blue-800 mb-2">并行度提升</div>
  <div class="text-xs opacity-60 leading-relaxed">
    多个 agent 并行工作，突破单 agent 的上下文瓶颈
  </div>
</div>

<div class="p-5 rounded-xl bg-green-50 border border-green-100 text-center" v-click>
  <carbon-security class="text-3xl text-green-600 mb-3" />
  <div class="font-bold text-green-800 mb-2">责任边界清晰</div>
  <div class="text-xs opacity-60 leading-relaxed">
    每个 agent 职责明确，出错可定位
  </div>
</div>

<div class="p-5 rounded-xl bg-purple-50 border border-purple-100 text-center" v-click>
  <carbon-copy class="text-3xl text-purple-600 mb-3" />
  <div class="font-bold text-purple-800 mb-2">协作模板可复制</div>
  <div class="text-xs opacity-60 leading-relaxed">
    一次编排模式可在不同场景复用
  </div>
</div>

</div>

<div class="mt-6 text-center text-sm opacity-60" v-click>
  连接道术：这是"注意力稀缺 + context 有限"下的工程化解法
</div>

<!--
高层案例 - 方案价值。

1. 并行度提升：多个 agent 并行工作，突破单 agent 的上下文瓶颈
2. 责任边界清晰：每个 agent 职责明确，出错可以快速定位到哪个环节
3. 协作模板可复制：一次成功的编排模式可以在不同场景复用

这不只是"用了多个 agent"——
而是把前面讲的约束（注意力稀缺 + context 有限）转化为工程方案。
-->

---
layout: default
---

# iOS 18 NavigationStack 假死排障

<div class="mt-4">

<div class="flex items-start gap-6">
<div class="flex-1">

<div class="mb-4 text-sm opacity-70">
  2~3 层 NavigationStack + 状态刷新 → UI 假死
</div>

<div class="space-y-2">
  <div class="flex items-center gap-3 p-3 rounded-lg bg-gray-50 border" v-click>
    <div class="w-6 h-6 rounded-full bg-red-100 text-red-600 flex items-center justify-center text-xs font-bold">1</div>
    <div class="text-sm"><strong>现象</strong>：特定层级下 UI 无响应</div>
  </div>
  <div class="flex items-center gap-3 p-3 rounded-lg bg-gray-50 border" v-click>
    <div class="w-6 h-6 rounded-full bg-orange-100 text-orange-600 flex items-center justify-center text-xs font-bold">2</div>
    <div class="text-sm"><strong>最小复现</strong>：构建隔离环境复现问题</div>
  </div>
  <div class="flex items-center gap-3 p-3 rounded-lg bg-gray-50 border" v-click>
    <div class="w-6 h-6 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center text-xs font-bold">3</div>
    <div class="text-sm"><strong>Agent 介入</strong>：定位 / 复现 / 验证</div>
  </div>
  <div class="flex items-center gap-3 p-3 rounded-lg bg-gray-50 border" v-click>
    <div class="w-6 h-6 rounded-full bg-green-100 text-green-600 flex items-center justify-center text-xs font-bold">4</div>
    <div class="text-sm"><strong>Workaround</strong>：规避策略 + 团队 Memory 记录</div>
  </div>
</div>

</div>
<div class="w-32 flex items-center justify-center">
  <carbon-mobile class="text-7xl text-gray-300 opacity-60" />
</div>
</div>

</div>

<!--
具体案例：SwiftUI / iOS 18 NavigationStack 假死。

现象：2~3 层 NavigationStack + 状态刷新，可能触发 UI 假死。
这是一个真实的、我们在生产中遇到的问题。

闭环流程：
1. 现象：特定层级下 UI 无响应
2. 最小复现：构建隔离环境，排除其他因素
3. Agent 介入：帮助定位问题根因，构建复现工程，验证修复
4. Workaround：规避策略 + 写入团队 memory 记录

重点不是"AI 修了个 bug"，而是"排障流程被标准化并可复用"。
产出：最小复现工程、规避策略、团队 memory 记录。
-->

---
layout: default
---

# 案例总结：流程 → 资产 → 模板

<div class="mt-8 flex items-center justify-center gap-6">

<div class="text-center p-6 rounded-2xl bg-gradient-to-b from-gray-50 to-gray-100 border border-gray-200 w-48" v-click>
  <carbon-flow class="text-3xl text-gray-600 mb-3" />
  <div class="font-bold">标准化流程</div>
  <div class="text-xs opacity-60 mt-2">现象 → 复现 → 定位 → 修复 → 沉淀</div>
</div>

<carbon-arrow-right class="text-2xl text-gray-400" v-click />

<div class="text-center p-6 rounded-2xl bg-gradient-to-b from-blue-50 to-blue-100 border border-blue-200 w-48" v-click>
  <carbon-save class="text-3xl text-blue-600 mb-3" />
  <div class="font-bold text-blue-800">资产沉淀</div>
  <div class="text-xs opacity-60 mt-2">复现工程 / 规避策略 / 团队记录</div>
</div>

<carbon-arrow-right class="text-2xl text-gray-400" v-click />

<div class="text-center p-6 rounded-2xl bg-gradient-to-b from-green-50 to-green-100 border border-green-200 w-48" v-click>
  <carbon-copy class="text-3xl text-green-600 mb-3" />
  <div class="font-bold text-green-800">可复用模板</div>
  <div class="text-xs opacity-60 mt-2">类似问题直接套用</div>
</div>

</div>

<div class="mt-8 text-center text-sm opacity-60" v-click>
  案例的价值不在于"AI 帮你修了 bug"，而在于"流程可复制"
</div>

<!--
案例总结：标准化流程 → 资产沉淀 → 可复用模板。

两个案例的共同点：
- 都不是在展示"AI 很厉害"
- 而是在展示"流程如何被标准化和沉淀"

一次成功的排障/协作经验，变成了：
- 可复用的标准化流程
- 沉淀下来的资产（代码/文档/记录）
- 下次遇到类似问题可以直接套用的模板

案例目的不是炫技，而是展示"流程可复制"。
-->

---
layout: default
---

# 工程师的新手艺

<div class="mt-8 grid gap-4 max-w-2xl mx-auto">

<div v-click class="flex items-center gap-4 p-4 rounded-xl bg-blue-50 border border-blue-100">
<carbon-data-definition class="text-2xl text-blue-600 flex-shrink-0" />
<div>
<div class="font-bold text-blue-800">把问题讲清楚</div>
<div class="text-xs opacity-60">定义、约束、验收</div>
</div>
</div>

<div v-click class="flex items-center gap-4 p-4 rounded-xl bg-indigo-50 border border-indigo-100">
<carbon-build-tool class="text-2xl text-indigo-600 flex-shrink-0" />
<div>
<div class="font-bold text-indigo-800">把系统搭到 agent 能发挥</div>
<div class="text-xs opacity-60">上下文、可观测、自动化</div>
</div>
</div>

<div v-click class="flex items-center gap-4 p-4 rounded-xl bg-purple-50 border border-purple-100">
<carbon-data-enrichment class="text-2xl text-purple-600 flex-shrink-0" />
<div>
<div class="font-bold text-purple-800">把成功路径变成团队资产</div>
<div class="text-xs opacity-60">Memory + Skill + 模板</div>
</div>
</div>

</div>

<div v-click class="mt-6 text-center text-sm opacity-60">
明天最小落地：<strong>1 个模板 + 1 个验证循环</strong>
</div>

<!--
收束。三句话：

1. 把问题讲清楚（定义、约束、验收）
2. 把系统搭到 agent 能发挥（上下文、可观测、自动化）
3. 把成功路径变成团队资产（memory + skill + 模板）

收束补句：
- 软件开发与产品设计将持续从 to-human 走向 to-agent
- Memory/skill 的构建本质是"渐进式披露（progressive disclosure）"实践

行动号召：明天最小落地——1 个模板 + 1 个验证循环。
不需要一步到位，从最小的闭环开始。
-->

---
layout: end
---

<div class="text-center">
  <div class="text-2xl font-bold mb-6">Thank You</div>
  <div class="text-base opacity-70 mb-2">Wei Wang</div>
  <div class="flex items-center justify-center gap-4 text-sm opacity-50">
    <span><carbon-logo-x class="inline mr-1" />@onevcat</span>
    <span><carbon-logo-github class="inline mr-1" />onevcat</span>
  </div>
</div>

<!--
尾页，Q&A 期间常驻。

Q&A 采用现场互动，不做预置问题 slide。

建议可接的问题方向：
1. 企业权限与安全如何落地？
2. 模型与成本如何分层治理？
3. 如何从人工监督平稳过渡到无人职守？
4. 团队 memory/skill 最小可行版本怎么搭？
5. 如何避免个体飞轮与团队断层？

视现场问题决定是否口头补充"云端 agent 架构细节"。
-->
