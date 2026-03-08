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
layout: intro
class: text-center
---

# AI Agent 的道与术

<div class="text-2xl opacity-80">
  <span class="strike-anim transition-opacity duration-700" :class="$clicks >= 1 ? 'struck opacity-40' : ''">Agentic Engineering 时代的工程师实践</span>
</div>

<div v-click class="mt-4 text-lg opacity-70">
  —— 团队和个人的 Agent 使用心得分享
</div>

<div class="abs-bl ml-14 mb-10 flex items-center gap-4">
  <div class="w-14 h-14 rounded-full overflow-hidden flex-shrink-0">
    <img src="/avatar.jpg" class="w-full h-full object-cover" />
  </div>
  <div class="flex flex-col gap-0.5 text-left">
    <div class="text-base opacity-80 font-semibold">王巍 · @onevcat</div>
    <div class="text-sm opacity-60">https://onev.cat</div>
  </div>
</div>

<div class="abs-br mr-14 mb-10 text-sm opacity-50">
  2026.03 / Shanghai
</div>

<style>
.strike-anim {
  position: relative;
  display: inline-block;
}
.strike-anim::after {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  width: 0;
  height: 3px;
  background: currentColor;
  transition: width 0.8s ease;
}
.strike-anim.struck::after {
  width: 100%;
}
</style>

<!--
- 感谢组委会邀请，感谢大周末来的各位
- 题目来由：组委会怂恿"做大一点，好卖票"
- Agentic Engineering → 组织管理 agent、高效协作，话题太大且高速变化
- [click] 划掉大副标题 → 所以没那么玄乎
- 真实定位：团队和个人这段时间用 AI agent 写代码的心得 & 最佳实践
-->

---
layout: default
clicks: 2
---

# 龙虾 🦞，智能体 🤖，Geek 的未来

<div class="mt-2 flex justify-center items-center relative h-100">
  <img v-click="[1,2]" src="/geek-future.jpg" class="max-h-full rounded-lg shadow-lg absolute transition-opacity duration-500" />
  <img v-click="2" src="/cooking.jpg" class="max-h-full rounded-lg shadow-lg absolute transition-opacity duration-500" />
</div>

<!--

- OpenClaw，龙虾火出圈。它的意义和启发是什么
- Peter 在社媒上的发布，理想中的 Geek 的样子
- 但理想和现实的差距，我实际的使用方式
- 不论具体的使用方式是什么，AI的渗透和对工程师的改变
- Geek 的未来，在 AI agent 从办公桌渗透到厨房时，如何共存
-->

---
layout: new-section
---

# 身在此山中

<div class="flex justify-center">
<div class="text-left space-y-3">
<p class="!opacity-80 !text-3xl flex items-center"><carbon-map class="text-teal-400 mr-2 text-3xl flex-shrink-0" />我们是怎么走到今天这一步的？</p>
<p class="!opacity-80 !text-3xl flex items-center"><carbon-compass class="text-teal-400 mr-2 text-3xl flex-shrink-0" />为今后的工程决策定坐标</p>
</div>
</div>

<!--
- 想要讨论未来，我们必须搞清楚我们是怎么一路走到现在的
- “不识庐山真面目，只缘身在此山中。”
- 定位当前坐标，猜测和判断我们所处的位置，并推断下一阶段。
-->

---
layout: default
---

# 从前、当下、将来

<div class="mt-6 flex gap-4">
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
    长任务 / 少指令 / 自主
  </TimelineStage>
</div>

<div class="mt-10 relative h-16">
  <div v-click="[1,2]" class="absolute inset-0 flex items-center justify-center gap-5 transition-opacity duration-300">
    <span class="text-base opacity-50">2018 – 2022</span>
    <span class="px-4 py-1.5 bg-gray-100 rounded-md text-base">TabNine</span>
    <span class="px-4 py-1.5 bg-gray-100 rounded-md text-base">Kite</span>
  </div>
  <div v-click="[2,3]" class="absolute inset-0 flex items-center justify-center gap-5 transition-opacity duration-300">
    <span class="text-base opacity-50">2022 – 2024</span>
    <span class="px-4 py-1.5 bg-gray-100 rounded-md text-base">ChatGPT</span>
    <span class="px-4 py-1.5 bg-gray-100 rounded-md text-base">Claude</span>
  </div>
  <div v-click="[3,4]" class="absolute inset-0 flex items-center justify-center gap-5 transition-opacity duration-300">
    <span class="text-base opacity-50">2024 – 2025</span>
    <span class="px-4 py-1.5 bg-gray-100 rounded-md text-base">Cursor</span>
    <span class="px-4 py-1.5 bg-gray-100 rounded-md text-base">Windsurf</span>
  </div>
  <div v-click="4" class="absolute inset-0 flex items-center justify-center gap-5 transition-opacity duration-300">
    <span class="text-base opacity-50">2025 –</span>
    <span class="px-4 py-1.5 bg-teal-50 rounded-md text-base text-teal-600 font-medium">Claude Code</span>
    <span class="px-4 py-1.5 bg-teal-50 rounded-md text-base text-teal-600 font-medium">Codex</span>
  </div>
</div>

<!--
[节奏] 每个 Phase 停 5-8 秒，让观众消化

- Phase I：最早的 AI 编码体验，补全当前行。「AI 第一次摸到了你的代码」
- Phase II：ChatGPT chatbox 时代，问题甩给聊天窗口。强大但割裂——复制粘贴来回搬运，缺乏整体认知（Stack overflow 的替代）
- Phase III：Cursor/Windsurf 把 AI 拉进编辑器，能读整个仓库，生成大段代码，进行预测
- Phase IV：Claude Code/Codex 更强大的工具调用（agent loop），自主运行、调试、提交。

- 人逐渐从编码的主题，退到辅助位和验收位

[关键句] 回顾不是怀旧，是为了给今天的工程决策定坐标。
[过渡] 如果这个演进成立，下一个问题就是：当前阶段，人的瓶颈在哪？
-->

---
layout: default
clicks: 4
---

# PHASE IV - 人开始成为瓶颈

<div class="flex-1 mt-1">
  <CapabilityChart :step="$clicks" />
</div>

<!--
[节奏] 三步递进，每步停 5 秒

- Click 1（人类线）：工程师能力一直在涨——持续学习、掌握新工具、积累经验。但这是线性的。
- Click 2（模型线）：模型能力也在涨，而且是指数型的。几个代表性的事件：2025 前半 Claude
 Code 出现，2025 年底 Opus 4.5 和 Codex 5.2 发布后，出现明显的感知。大家会觉得突然
- Click 3（差距高亮）：这个橙色区域就是"瓶颈"——不是人不行了，而是模型太快了，人类决策的速度跟不上模型的速度。

[关键句] 开发者的工作往更高层次上移动了：定义问题、设边界、做验收。
-->

---
layout: new-section
---

# <carbon-chart-line-smooth class="inline text-teal-400 mr-2" /> 趋势汇报

<div class="mt-4 text-3xl opacity-70">
一个大型 iOS 开发团队的变化实例
</div>

<!--
- 这个变化和认知，是有佐证的
- 举一下我在的公司作为例子
- 今天是个人身份过来，在已公开范围内进行介绍
- 我们之后的内容，大家也可以有一个基准参照，实践是在什么规模下发生的
-->

---
layout: default
---

# 规模背景

<div class="mt-6 grid grid-cols-4 gap-6">
  <StatCard value="Swift + ObjC" label="实现语言" v-click>
    <template #icon><logos-swift class="inline" /> <span class="opacity-30 mx-1">/</span> <span class="text-purple-700 text-2xl font-extrabold leading-none" style="font-family: 'Fira Code', monospace">.m</span></template>
  </StatCard>
  <StatCard value="~250 万" label="代码行数" v-click>
    <template #icon><carbon-code class="inline" /></template>
  </StatCard>
  <StatCard value="~650" label="模块" v-click>
    <template #icon><carbon-assembly-cluster class="inline" /></template>
  </StatCard>
  <StatCard value="~25,000" label="文件" v-click>
    <template #icon><carbon-document class="inline" /></template>
  </StatCard>
</div>

<div class="mt-6 text-lg opacity-60 text-center" v-click>
  覆盖全局困难，很多小项目和个人项目中不存在的挑战，需要系统化的工程方法
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

# PR 趋势 <carbon-chart-line class="inline text-teal-500" />

<div class="mt-6 flex items-center gap-8">
<div class="flex-1">

<v-clicks>

- 产出速度明显加快
- 但 review / 验收 / 质量控制形态也在**同步重构**
- 不是简单的"多了"，而是生产模式在变

</v-clicks>

</div>
<div class="w-80 h-48 rounded-xl bg-gradient-to-br from-teal-50 to-teal-50 border border-teal-100 flex items-center justify-center">
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
layout: center
---

<div class="flex flex-col items-center justify-center h-full">
  <div class="text-6xl font-bold tracking-tight">序章已经落下</div>
  <div class="w-24 h-1 bg-teal-500 rounded-full mt-6 mb-8"></div>

  <div class="flex gap-2 w-full max-w-2xl" style="transform: scale(0.7); transform-origin: center;">
    <TimelineStage label="Phase I" title="Tab 补全">AI 进入编码动作</TimelineStage>
    <TimelineStage label="Phase II" title="Chatbot">同步提示-响应回路</TimelineStage>
    <TimelineStage label="Phase III" title="AI Editor">仓内上下文协作</TimelineStage>
    <TimelineStage label="Phase IV" title="Code Agent">长任务 / 少指令 / 自主</TimelineStage>
  </div>

  <v-click>
    <div class="mt-8 flex gap-8 text-base tracking-wide">
      <div class="flex items-start gap-2 opacity-60">
        <carbon-view class="text-teal-500 mt-0.5 flex-shrink-0" />
        <span>我们观察到的现象</span>
      </div>
      <div class="flex items-start gap-2 opacity-60">
        <carbon-roadmap class="text-teal-500 mt-0.5 flex-shrink-0" />
        <span>推进中遇到的阻力与对策</span>
      </div>
    </div>
  </v-click>
</div>

<!--
从 Tab 补全到 Chatbot，到 AI Editor，再到 Code Agent——这四个阶段是人类在尝试和 AI 共同编程时的阶段性成果。

到今天，大方向已经确定下来了：大家基本认同 Code Agent 这种方式是比较理想的协作形态。围绕它，工具链、工作流、最佳实践都在快速成型。可以说，人类在这条科技树上已经点下去了。

所以我说"序章已经落下"——不是结束，而是地基打好了。后面的章节，都将以这个序章为基础继续演化。

（点击）接下来想跟大家分享两件事：
一是我们在这个阶段观察到的一些现象——趋势数据背后的规律；
二是团队和我个人在推进 AI 落地时遇到的真实阻力，以及我们尝试的对策。
-->

---
layout: center
---

# 今天的话题

<img src="/topic-overview.png" class="w-full mt-4" />

<div class="mt-2 grid grid-cols-3 text-center text-2xl font-bold">
  <div>上下文工程</div>
  <div class="translate-x-2">团队化积累</div>
  <div class="-translate-x-6">协作新范式</div>
</div>

<div class="mt-4 text-base opacity-50 text-center">每组话题：先看约束，再聊实践</div>

<!--
我们在实践中遇到了非常非常多的课题。今天时间肯定是不够的，所以大概只能聊我认为最最重要的三组话题：

1. 上下文工程——高效且正确地去管理和使用。把信息喂对、喂好，是第一个要解决的问题。
2. 然后是团队化积累。把团队里大神和高手的做法推广沉淀。
3. 最后是协作新范式——从人指挥一个 Agent，指挥多个 Agent，到最后理想中的 Agent 自协作的话题。

每组话题，我们先看约束在哪，再聊我们的实践和对策。
-->

---
layout: default
clicks: 1
---

# 约束一：有限的 Context vs 膨胀的任务

<div :class="[$clicks >= 1 ? 'mt-6' : 'mt-32', 'flex items-center gap-6 transition-all duration-700 ease-out']">

<div class="flex-1 text-center p-5 rounded-xl border border-teal-200 bg-teal-50">
  <carbon-chip class="text-3xl text-teal-500 mb-2" />
  <div class="font-bold text-lg">模型 Context</div>
  <div class="text-sm opacity-60 mt-1">SOTA Model - 200~400k</div>
  <div class="text-2xl font-bold mt-2 text-teal-800">始终有限</div>
</div>

<carbon-arrows-horizontal class="text-3xl opacity-30 flex-shrink-0" />

<div class="flex-1 text-center p-5 rounded-xl border border-gray-200 bg-gray-50">
  <carbon-task class="text-3xl text-gray-500 mb-2" />
  <div class="font-bold text-lg">实际任务</div>
  <div class="text-sm opacity-60 mt-1">代码库、需求、约定、历史决策…</div>
  <div class="text-2xl font-bold mt-2 text-gray-800">不断膨胀</div>
</div>

</div>

<div :class="[$clicks >= 1 ? 'opacity-100' : 'opacity-0', 'transition-opacity duration-700 ease-out delay-300']">

<div class="mt-5 text-sm opacity-50 text-center">1M 上下文不是万灵丹——塞得越多，问题越明显</div>

<div class="mt-3 grid grid-cols-3 gap-4">
  <div class="p-3 rounded-lg bg-red-50 border border-red-100 text-center">
    <carbon-finance class="text-xl text-red-400 mb-1" />
    <div class="text-sm font-bold text-red-800">推理成本飙升</div>
    <div class="text-sm text-red-700 mt-1">Context 越长，耗时和费用急剧增长</div>
  </div>
  <div class="p-3 rounded-lg bg-orange-50 border border-orange-100 text-center">
    <carbon-search-locate class="text-xl text-orange-400 mb-1" />
    <div class="text-sm font-bold text-orange-800">Recall 成功率下降</div>
    <div class="text-sm text-orange-700 mt-1">信息越多，关键内容越容易被淹没</div>
  </div>
  <div class="p-3 rounded-lg bg-yellow-50 border border-yellow-100 text-center">
    <carbon-view-off class="text-xl text-yellow-600 mb-1" />
    <div class="text-sm font-bold text-yellow-900">注意力涣散</div>
    <div class="text-sm text-yellow-800 mt-1">模型难以聚焦，输出质量不稳定</div>
  </div>
</div>

</div>

<!--
模型的 Context 是有限的。目前主流 SOTA 模型的上下文窗口大概在 200K 到 400K token。
而我们的实际任务呢？在一个大型项目里，往往牵扯多个模块和复杂的决策链路，要解决的问题只会越来越复杂。代码库在膨胀、需求在增加、历史决策在积累。

有人会说，不是有 1M 上下文的模型吗？但百万 token 并不是万灵丹。在我们的实际尝试中，往里面塞的东西越多，问题就越明显——

[click]
1. 推理成本飙升——上下文越长，延迟和费用急剧增长，attention 计算是二次方的。
2. Recall 成功率下降——信息太多，关键内容反而被淹没。研究表明中间位置的信息 recall 可以下降超过 30%。
3. 注意力涣散——模型的注意力被稀释，输出质量变得不稳定。Anthropic 自己都说过："往窗口里塞十万 token 的历史会削弱模型对真正重要内容的推理能力"。
-->

---
layout: center
---

<div class="absolute inset-0 bg-white text-gray-900 overflow-hidden">

<!-- Diagonal teal stripes background -->
<div class="absolute inset-0 opacity-[0.04]" style="background: repeating-linear-gradient(-45deg, transparent, transparent 40px, #14b8a6 40px, #14b8a6 42px);"></div>

<!-- Title -->
<div class="absolute top-8 left-10 z-10">
  <div class="text-xl font-black text-teal-600 tracking-widest" style="transform: skewX(-12deg);">CONTEXT PROBLEM</div>
</div>
<div class="absolute top-16 left-8 z-10">
  <div class="text-4xl font-black leading-none" style="transform: skewX(-6deg);">
    <span class="bg-teal-600 text-white px-4 py-1 inline-block">遇到这些</span>
    <span class="text-gray-900 ml-2">你就知道</span>
    <span class="bg-gray-900 text-white px-3 py-1 inline-block ml-1" style="transform: skewX(-5deg);">糟糕了</span>
  </div>
</div>

<!-- Cards -->
<div class="absolute top-40 left-6 right-6 space-y-4 z-10" style="perspective: 800px;">

<div v-click class="slam-card">
  <div class="relative" style="transform: skewX(-5deg) rotate(1.8deg);">
    <div class="bg-teal-600 text-white px-5 py-4 text-xl font-black flex items-center gap-3" style="clip-path: polygon(0 0, 100% 0, 98% 100%, 2% 100%);">
      <span class="text-teal-200 text-3xl">///</span>
      <span>代码生成到一半，突然跳</span>
      <span class="bg-white text-teal-700 px-2 py-0.5 text-lg font-mono inline-block" style="transform: skewX(8deg);">context compaction</span>
    </div>
  </div>
</div>

<div v-click class="slam-card">
  <div class="relative" style="transform: skewX(-7deg) rotate(-1.2deg); margin-left: 2rem;">
    <div class="bg-gray-900 text-white px-5 py-4 text-xl font-black flex items-center gap-3" style="clip-path: polygon(2% 0, 98% 0, 100% 100%, 0 100%);">
      <span class="text-teal-400 text-3xl">///</span>
      <span>你开始不停地说</span>
      <span class="bg-white text-gray-900 px-2 py-0.5 text-lg inline-block" style="transform: skewX(8deg);">"这里不对，修一下"</span>
    </div>
  </div>
</div>

<div v-click class="slam-card">
  <div class="relative" style="transform: skewX(-4deg) rotate(2.5deg); margin-left: 0.5rem;">
    <div class="bg-teal-700 text-white px-5 py-4 text-xl font-black flex items-center gap-3" style="clip-path: polygon(0 0, 100% 0, 98% 100%, 2% 100%);">
      <span class="text-teal-300 text-3xl">///</span>
      <span>"求求你了别再动那个文件了，它和这次的问题不相关"</span>
    </div>
  </div>
</div>

<div v-click class="slam-card">
  <div class="relative" style="transform: skewX(-8deg) rotate(-1.8deg); margin-left: 3rem;">
    <div class="bg-gray-800 text-white px-5 py-4 text-2xl font-black flex items-center gap-3" style="clip-path: polygon(2% 0, 98% 0, 100% 100%, 0 100%);">
      <span class="text-teal-400 text-4xl">!!!</span>
      <span>"我们不是一开始就约好了么，你怎么又</span>
      <span class="bg-teal-600 text-white px-2 py-0.5 inline-block" style="transform: skewX(12deg) rotate(-4deg);">...</span>
    </div>
  </div>
</div>

</div>

</div>

<style>
.slam-card {
  transform-origin: center top;
  transform: perspective(800px) rotateX(-90deg) translateY(-60px);
  opacity: 0;
  transition: none !important;
}
.slam-card:not(.slidev-vclick-hidden) {
  animation: slamDown 0.4s cubic-bezier(0.22, 1, 0.36, 1) forwards;
}
@keyframes slamDown {
  0% {
    transform: perspective(800px) rotateX(-90deg) translateY(-60px);
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
  70% {
    transform: perspective(800px) rotateX(6deg) translateY(4px);
    opacity: 1;
  }
  85% {
    transform: perspective(800px) rotateX(-2deg) translateY(-2px);
  }
  100% {
    transform: perspective(800px) rotateX(0) translateY(0);
    opacity: 1;
  }
}
</style>

<!--
这些都是我们在现场看到的、工程师们在使用 Agent 编码时非常常见的问题。
很多人来找我们求助的时候，症状几乎一模一样。遇到这些，你就知道——上下文管理出了问题。

（逐条点击）
1. 比如说，哎，代码生成到一半，上下文满了，开始压缩。那跳这个基本意味着这次白干了，准备重新来过吧。
2. 开始反复说"啊，这里不对修一下；那里不对修一下；还是不对修一下"——我们一般把这个叫做模型鬼打墙，出不去了。模型输出开始偏离预期，你不停地纠正，这就是 recall 下降和注意力涣散的直接体现。
3. 你开始说"求求你了别再动那个文件"，或者你开始一些“针对代码的微操”——那基本上就是模型已经忘了哪些文件和当前任务无关，边界信息在上下文里丢了。
4. "我们不是一开始就约好了么"..这种可能经常出现在言情剧里的台词——定义的架构约定、编码规范，到后面被模型"忘掉"了

这些不是偶发的，而是上下文有限这个根本约束带来的必然结果，也是阻碍我们的工程师日常使用的最大的几个问题。
知道了问题在哪，接下来看怎么应对。
-->

---
layout: default
---

# 上下文工程：精简注入 <carbon-clean class="inline text-teal-500" />

<div class="mt-2 text-base text-gray-500 mb-6">只给模型它真正需要的</div>

<div class="grid grid-cols-3 gap-5 mt-4">
<div class="p-5 rounded-lg bg-teal-50 border border-teal-100" v-click>
  <carbon-document class="text-3xl text-teal-500 mb-3" />
  <div class="font-bold text-lg">AGENTS.md 极简化</div>
  <div class="text-sm text-gray-500 mt-2">≤ 100 行，只写领域知识</div>
  <div class="text-sm text-gray-500 mt-1">行为式引用 · 渐进式披露</div>
</div>
<div class="p-5 rounded-lg bg-teal-50 border border-teal-100" v-click>
  <carbon-terminal class="text-3xl text-teal-500 mb-3" />
  <div class="font-bold text-lg">辅助脚本和工具</div>
  <div class="text-sm text-gray-500 mt-2">模块和架构查找</div>
  <div class="text-sm text-gray-500 mt-1">简化输出，如 xcsift</div>
</div>
<div class="p-5 rounded-lg bg-teal-50 border border-teal-100" v-click>
  <carbon-machine-learning-model class="text-3xl text-teal-500 mb-3" />
  <div class="font-bold text-lg">选择顶级模型</div>
  <div class="text-sm text-gray-500 mt-2">推理密集 ≠ 省 token 的地方</div>
  <div class="text-sm text-gray-500 mt-1">弱模型 → 错误积累 → 返工</div>
</div>
</div>

<!--
知道了问题在哪，来看怎么应对。首先是"精简注入"——只给模型必要的信息。

（点击卡片 1）
AGENTS.md 或者 CLAUDE.md，很多人恨不得往里塞成百上千行。但实际上，这些只是辅助，很可能你发现庞大的指导文件还不如没有指导文件。所以我们的实践是：
- 控制在 100 行左右，只写领域知识——就是你项目里独有的东西，而不是"请写好代码"或者源码在“Source文件夹”这类通识
- 关键文件清单和命令不要单纯列出来，要用行为式引用："如果你要改认证模块，必须先读 auth/README.md"
- 渐进式披露，让模型按需去找更详细的信息，而不是一次全塞进去

（点击卡片 2）
第二个是辅助脚本。Agent 在大型项目里最浪费上下文的操作就是"找东西"和“读东西”。它会 grep、会 find、会反复读文件，这些全都消耗上下文。所以我们会准备专门的脚本——模块查找、架构信息速查，让 agent 一步到位，不要盲目搜索。另外，对于输出，寻找专门为 agent 优化的工具。

（点击卡片 3）
第三个，选模型别省钱。Agent 编码需要高度的智能，弱模型会产生的错误需要你要花时间纠正，纠正本身又消耗上下文，上下文不足叠加模型能力，导致更多错误，形成恶性循环。省下的费用远不如省下的人力成本。
-->

---
layout: default
clicks: 2
---

# 上下文工程：控制边界 <carbon-cut class="inline text-teal-500" />

<div class="mt-2 text-base text-gray-500 mb-6">隔离、拆分、保持上下文干净</div>

<div class="mt-4 flex items-center gap-4" v-click="1">

<div class="w-28 text-center p-4 rounded-lg border border-red-200 bg-red-50">
  <carbon-task-asset-view class="text-3xl text-red-400 mb-2" />
  <div class="font-bold">大型任务</div>
  <div class="text-sm text-gray-500">跨模块 · 多文件</div>
</div>

<carbon-arrow-right class="text-3xl text-teal-400 flex-shrink-0" />

<div class="flex-1 text-center p-5 rounded-lg border-2 border-teal-300 bg-teal-50">
  <carbon-cut class="text-3xl text-teal-500 mb-2" />
  <div class="font-bold text-lg">拆分为中等任务</div>
  <div class="text-sm text-gray-500">每个 ≤ 1 context window</div>
</div>

<carbon-arrow-right class="text-3xl text-teal-400 flex-shrink-0" />

<div class="w-28 text-center p-4 rounded-lg border border-teal-200 bg-teal-50">
  <carbon-checkmark-outline class="text-3xl text-teal-500 mb-2" />
  <div class="font-bold">逐个交付</div>
  <div class="text-sm text-gray-500">合并验收</div>
</div>

</div>

<div :class="[$clicks >= 2 ? 'opacity-100' : 'opacity-0', 'transition-opacity duration-500']">
<div class="mt-6 grid grid-cols-2 gap-4">
<div class="p-4 rounded-lg bg-teal-50 border border-teal-100 text-center">
  <div class="font-bold"><carbon-bot class="inline text-teal-500 mr-1" />Sub-agent 协作</div>
  <div class="text-sm text-gray-500 mt-1">有帮助，但合理拆分 > 堆 agent</div>
</div>
<div class="p-4 rounded-lg bg-teal-50 border border-teal-100 text-center">
  <div class="font-bold"><carbon-renew class="inline text-teal-500 mr-1" />新开 Thread</div>
  <div class="text-sm text-gray-500 mt-1">一个任务一个线程，避免历史污染</div>
</div>
</div>
</div>

<!--
第二组实践：控制边界。

LLM 擅长中小型任务。

（点击流程图）
最重要的一条：任务拆分，上下文压缩几乎是致命的，不要指望在压缩后还能完美解决问题。我给一个非常简单的判断标准——如果一个任务超过一个 context window 还搞不定，那它就是"大型任务"，必须拆。

拆成什么样？每个子任务应该在一个 context window 内能完成。明确边界和依赖关系，分别执行，最后合并。你可以使用一些 loop 的手段，然后把调查系的任务的结论当作提示词的一部分注入给负责实现的 agent。

[click]

（Sub-agent）
很多人会问 sub-agent 或者 agent team 有没有用？有用。但是使用它们一方面依赖工具链的能力，你难以完全控制。二是它们的前提是你先把agent定义好，把任务拆好了。如果任务本身边界不清，丢给再多 agent 也是乱的。关键还是在于合理的拆分。

（新开 Thread）
最后一个很容易被忽略的实践：多多新开 thread。很多人习惯在一个对话里连续做好几个任务，但前面任务的历史会污染后面任务的注意力。完成一个任务，开一个新线程，保持干净的上下文。成本很低，效果很好，避免很多问题。
-->

---
layout: center
---

<div class="text-center">
  <div class="text-2xl text-gray-500 mb-8">模型注意力分布</div>
  <div class="flex items-end justify-center gap-2 h-52">
    <div class="w-12 bg-teal-500 rounded-t" style="height: 90%"></div>
    <div class="w-12 bg-teal-400 rounded-t" style="height: 75%"></div>
    <div class="w-12 bg-teal-300 rounded-t" style="height: 50%"></div>
    <div class="w-12 bg-teal-200 rounded-t" style="height: 35%"></div>
    <div class="w-12 bg-gray-200 rounded-t" style="height: 25%"></div>
    <div class="w-12 bg-gray-200 rounded-t" style="height: 20%"></div>
    <div class="w-12 bg-gray-200 rounded-t" style="height: 18%"></div>
    <div class="w-12 bg-gray-200 rounded-t" style="height: 20%"></div>
    <div class="w-12 bg-gray-200 rounded-t" style="height: 25%"></div>
    <div class="w-12 bg-teal-200 rounded-t" style="height: 35%"></div>
    <div class="w-12 bg-teal-300 rounded-t" style="height: 55%"></div>
    <div class="w-12 bg-teal-400 rounded-t" style="height: 70%"></div>
    <div class="w-12 bg-teal-500 rounded-t" style="height: 85%"></div>
  </div>
  <div class="flex justify-between text-base text-gray-500 mt-4 px-2 max-w-lg mx-auto">
    <span>开头（强）</span>
    <span>中段（弱）</span>
    <span>最近（强）</span>
  </div>
  <div class="mt-8 text-xl">
    精简注入 + 控制边界 → 关键信息始终在<strong class="text-teal-600">注意力高位</strong>
  </div>
  <div class="mt-4 text-base text-gray-400">
    像管理早期移动设备的内存一样，去管理你的 Context
  </div>
</div>

<!--
为什么前面两页的实践有效？其实原因还是模型的注意力分布，
是呈现一个很典型的 U 型曲线：和人很像，
开头和最近的内容获得强注意力，中段是衰减区。

所以我们前面做的所有事情，本质上就是：
- 精简注入：AGENTS.md 里的规则放在开头，模型一开始就能看到
- 控制边界：保持上下文短而干净，避免关键信息被挤到中段的衰减区
- 新开 thread：每次都让任务描述处于"最近"的高注意力位置

这就是上下文工程的核心——不是写更好的提示词，而是管理好信息在上下文中的位置和密度。

作为移动开发者，我们对这件事其实并不陌生。管理 context 就要像开发早期移动 App 那样去珍惜它，就像在管理移动设备上的内存一样。每一个 byte 都很宝贵，你不会把无关的东西加载到内存里；同样的，也不要把无关的信息塞进上下文。

好，上下文的道和术讲完了，接下来进入第二组：AI 使用的两极分化。
-->

---
layout: default
---

# 约束二：Agent 的天花板是人

<div class="mt-1 text-base opacity-60">Agent 不会自动变强——能力上限由驾驭者决定</div>

<div class="mt-5">
<div class="text-sm font-semibold mb-3 text-gray-500 tracking-wide">SAME AGENT · DIFFERENT HUMANS</div>

<div v-click class="bar-container">

<div>
  <div class="flex items-center justify-between mb-2">
    <span class="text-base font-bold text-teal-700"><carbon-user class="inline" /> 高手</span>
    <span class="text-sm text-teal-600">指挥多个 Agents · 丰富 Memory + Skill</span>
  </div>
  <div class="h-12 rounded-lg bg-gray-100 overflow-hidden">
    <div class="bar-fill h-full rounded-lg bg-gradient-to-r from-teal-400 to-teal-600" style="--bar-width: 90%"></div>
  </div>
</div>

<div class="my-2 flex items-center justify-center gap-2 text-orange-400">
  <div class="flex-1 border-t border-dashed border-orange-200"></div>
  <span class="text-sm font-bold px-2"><carbon-arrows-vertical class="inline text-xs" /> 差距数十倍</span>
  <div class="flex-1 border-t border-dashed border-orange-200"></div>
</div>

<div>
  <div class="flex items-center justify-between mb-2">
    <span class="text-base font-bold text-gray-500"><carbon-user class="inline" /> 入门</span>
    <span class="text-sm text-gray-500">零积累 · 还在摸索阶段或当成 Chatbot</span>
  </div>
  <div class="h-12 rounded-lg bg-gray-100 overflow-hidden">
    <div class="bar-fill h-full rounded-lg bg-gradient-to-r from-gray-200 to-gray-300" style="--bar-width: 10%"></div>
  </div>
</div>

</div>
</div>

<div v-click class="mt-5 p-4 rounded-xl border border-orange-100 bg-gradient-to-br from-orange-50 to-white flex items-start gap-4">
  <carbon-warning-alt class="text-2xl text-orange-500 flex-shrink-0 mt-0.5" />
  <div>
    <div class="font-bold text-lg">同一模型，效能差距巨大</div>
    <div class="text-base mt-1 opacity-70">员工差距远超 Agent 前时代——AI 使用能力高度个体化，个人强 ≠ 组织强</div>
  </div>
</div>

<style>
.bar-fill {
  width: 0%;
  transition: width 1s cubic-bezier(0.22, 1, 0.36, 1) 0.15s;
}
.bar-container:not(.slidev-vclick-hidden) .bar-fill {
  width: var(--bar-width);
}
</style>

<!--
约束二：Agent 的天花板是人。
我们观察到不同的人在使用AI时的效率差距非常大。
Agent 不会自动变强，能力上限取决于驾驭它的人。
同一个 Claude Code 或 Codex，高手和入门者用出来的效果天差地别。

[click] 直观看：高手有丰富的 Memory 和 Skill 积累，入门者零积累。
有的员工能一天解决十多个 issue，同时高质量完成 PR 和各种 spec 评审；
有的员工还在古法编程，差距可能有数十倍。
这不是模型的问题，是人的问题。

[click] 而且这个差距远超 Agent 前时代。以前大家效率差个两三倍顶天了，
现在 AI 使用能力高度个体化，拉开的差距是数量级的。
个人强不等于组织强，这个差距如果不主动治理，会变成团队断层。
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
- 对齐关键：让高手的 Memory/Skill **可沉淀、可分享**

</div>

</div>
<div class="w-48 flex flex-col items-center gap-3">
  <div class="px-4 py-2 rounded-lg bg-teal-100 text-teal-800 text-sm font-bold">
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
AI的两极分化大部分是闻道有先后造成的。
但这里存在的"少数人飞起、多数人观望"的组织问题是实际存在和需要解决的。

组织里会有一些约定的实践，比如通用的 skill 和 workflow 等。很多这些实践的推广大多是自下而上的。
传统自上而下路径在这个周期里通常偏慢——等制度跟上，可能高手已经迭代三轮了。反过来，让这些高手能带动团队一起进步，可能是更正确的方向。
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
Harness 策略：从道到术。

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
  <div class="px-4 py-2 rounded-lg bg-teal-100 text-teal-800 text-sm font-semibold">
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
  <carbon-template class="text-xl text-teal-500 mb-1" />
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
这是从个人能力到组织能力的桥梁。积累讲完了，最后来看协作。
-->

---
layout: new-section
---

# 协作

从人指挥到 Agent 自协作

<!--
第三组：协作。
有了上下文和积累的基础，最后看协作范式如何演进，以及怎么把任务交给 agent。
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
  <carbon-user class="text-2xl text-teal-500 mx-1" />
  <carbon-arrow-right class="text-xl text-gray-400 mx-1" />
  <carbon-bot class="text-2xl text-gray-500 mx-1" />
  <carbon-bot class="text-2xl text-gray-500 mx-1" />
  <carbon-bot class="text-2xl text-gray-500 mx-1" />
  <div class="text-xs opacity-50 mt-3">人工编排，注意力是瓶颈</div>
</div>

<div class="p-6 rounded-xl bg-teal-50 border border-teal-200 text-center" v-click>
  <div class="text-sm text-teal-600 mb-2">下一阶段</div>
  <div class="text-lg font-bold text-teal-800 mb-3">Agent ↔ Agent</div>
  <carbon-bot class="text-2xl text-teal-500 mx-1" />
  <carbon-connect class="text-xl text-teal-400 mx-1" />
  <carbon-bot class="text-2xl text-teal-500 mx-1" />
  <carbon-connect class="text-xl text-teal-400 mx-1" />
  <carbon-bot class="text-2xl text-teal-500 mx-1" />
  <div class="text-xs text-teal-600 mt-3">自协作，人做策略与兜底</div>
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
    <carbon-arrow-right class="text-3xl text-teal-500" />
    <div class="text-xs text-teal-600 font-semibold mt-1">关键跨越</div>
  </div>
  <div class="px-5 py-3 rounded-xl bg-teal-600 text-white font-bold">
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
跨越点明确了，怎么把任务交给 agent？关键是任务切分。
-->

---
layout: default
---

# 任务切分：可验收交付单元

<div class="mt-6">

<div class="text-base mb-6">让 agent 接受的不是模糊需求，而是<strong>可验收的工作单元</strong></div>

<div class="grid grid-cols-4 gap-4" v-click>
<div class="p-4 rounded-xl bg-gray-50 border border-gray-200 text-center">
  <carbon-pull-request class="text-2xl text-teal-500 mb-2" />
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

<div class="mt-6 p-4 rounded-lg bg-teal-50 border border-teal-100" v-click>
  <div class="text-sm font-semibold text-teal-800 mb-1">
    <carbon-transform-instructions class="inline mr-1" /> 角色转变
  </div>
  <div class="text-xs text-teal-700">
    工程师从"亲自实现者"转向"任务编排 + 质量守门"
  </div>
</div>

</div>

<!--
任务切分：可验收交付单元。从道到术。

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

<div class="p-4 rounded-xl border border-teal-200 bg-teal-50" v-click>
  <carbon-catalog class="text-xl text-teal-600 mb-2" />
  <div class="text-sm font-bold text-teal-800">日志</div>
  <div class="text-xs text-teal-600 mt-1">行为链路可追溯</div>
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

着重提一下测试 BDD:
- 最接近自然语言的测试
- 天生适合作为 spec 规范
- LLM 通过自然语言生成测试
- 然后代码实现时由测试确保

验收标准要前置定义：
- 测试：单元/集成/UI 测试覆盖
- 日志：行为链路可追溯
- 回滚：可逆性保障，出问题能回退
- 风险列表：已知风险前置声明

验收标准前置的好处：减少返工 + 提高 agent 产出的可信度。
如果你不告诉 agent 怎么验证，它就不会自验。
三组道术讲完，来看整体的工程价值变化。
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

  - **TDD** 缩短试错回路<br/><span class="text-xs opacity-60">为 agent 提供即时反馈信号</span>
  - **可观测性** + Benchmark<br/><span class="text-xs opacity-60">让产出可度量，从"感觉"变成"数据"</span>
  - **可验证循环** 变更→证据→回归→沉淀<br/><span class="text-xs opacity-60">自动化回归边界大幅扩大</span>

  </v-clicks>
</CompareColumn>

<!--
工程价值重排 + 既有实践新价值。

弱化：DRY 边际下降、手写代码稀缺性下降、传统 review 需重构。
增强：TDD 即时反馈、可观测性让产出可度量、可验证循环扩大回归边界。

AI 变强后，不是"少做工程"，而是"重排工程优先级"。
这些既有实践——TDD、Benchmark、可观测性——在 AI 时代价值被放大了，
因为 agent 需要明确的验证信号才能自我修正。
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
战略落点明确后，来看实际案例。
-->
---
layout: new-section
---

# 案例

不是"AI 很神"，而是"流程如何标准化和沉淀"

<!--
过渡页。三组道术讲完，不靠口号，直接看两个案例。
案例不该只讲"AI 很神"，而应讲"流程如何被标准化和沉淀"。
-->

---
layout: default
---

# 大规模代码库中的 Subagent 协作

<div class="mt-4 text-sm opacity-70 mb-6">多语言、多模块、超大仓库 —— 单 agent 很难稳定覆盖</div>

<div class="flex items-center justify-center gap-3 mt-4" v-click>
  <div class="p-4 rounded-xl bg-teal-50 border border-teal-200 text-center w-36">
    <carbon-search class="text-2xl text-teal-600 mb-2" />
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

<div class="p-5 rounded-xl bg-teal-50 border border-teal-100 text-center" v-click>
  <carbon-increase-level class="text-3xl text-teal-600 mb-3" />
  <div class="font-bold text-teal-800 mb-2">并行度提升</div>
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
    <div class="w-6 h-6 rounded-full bg-teal-100 text-teal-600 flex items-center justify-center text-xs font-bold">3</div>
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

<div class="text-center p-6 rounded-2xl bg-gradient-to-b from-teal-50 to-teal-100 border border-teal-200 w-48" v-click>
  <carbon-save class="text-3xl text-teal-600 mb-3" />
  <div class="font-bold text-teal-800">资产沉淀</div>
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

<div v-click class="flex items-center gap-4 p-4 rounded-xl bg-teal-50 border border-teal-100">
<carbon-data-definition class="text-2xl text-teal-600 flex-shrink-0" />
<div>
<div class="font-bold text-teal-800">把问题讲清楚</div>
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
