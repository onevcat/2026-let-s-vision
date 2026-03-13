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

# 每周 PR 数量 <carbon-chart-line class="inline text-teal-500" />

<img src="/1_weekly_pr_count.png" class="w-full mt-4 rounded-lg shadow-sm" />

<div class="mt-4 pl-5 border-l-3 border-teal-300 text-base opacity-60">
  PR 总量保持稳定，趋势线微降——不是产出变少了，而是 PR 粒度在变大
</div>

<!--
第一张趋势图：每周 PR 数量。

趋势线斜率 -1.6/周，但整体量级保持稳定。
看起来 PR 数量没有爆发式增长，反而微降。
这不是产出变少了——而是 PR 的粒度在变大。

以前一个小改动一个 PR，现在 Agent 一次可以完成更完整的任务，
所以单个 PR 的改动量在增加，PR 数量反而不需要更多了。
生产模式在变化。
-->

---
layout: default
---

# PR 合并效率 <carbon-chart-line class="inline text-teal-500" />

<img src="/2_monthly_merge_time.png" class="w-full mt-4 rounded-lg shadow-sm" />

<div class="mt-4 pl-5 border-l-3 border-teal-300 text-base opacity-60">
  均值从 50+ 小时降至 20 小时，中位数降至个位——Review 效率在倍增
</div>

<!--
第二张趋势图：PR 平均合并时间。

均值从 8 月的 51 小时降至 3 月的 20 小时，中位数更是降到了 6.5 小时。
这意味着 review 和合并的效率在显著提升。

一方面是 AI 生成的 PR 更规范、更容易 review；
另一方面团队也在适应新的 review 节奏——
不再是"等人来看"，而是更主动、更快速地验收。
-->

---
layout: default
---

# AI 协作占比 <carbon-chart-line class="inline text-teal-500" />

<img src="/3_ai_coauthor_trend.png" class="w-full mt-4 rounded-lg shadow-sm" />

<div class="mt-4 pl-5 border-l-3 border-teal-300 text-base opacity-60">
  半年内从 1% 飙升至 40%——AI 协作已从尝鲜变为常态
</div>

<!--
第三张趋势图：AI Co-Authored PR 占比。

这张图最直观：从 2025 年 8 月的 1.1%，到 2026 年 3 月的 39.8%。
半年时间，AI 协作占比增长了近 40 倍。

注意增长曲线的形态——不是线性增长，而是指数型的。
2025 年底开始加速，和模型能力的台阶式提升（Opus 4.5、GPT-5.2 Codex）高度吻合。
AI 协作已经从少数人的尝鲜变成了团队的日常。
-->

---
layout: default
---

# Issue 消化趋势 <carbon-chart-line class="inline text-teal-500" />

<img src="/4_jira_issue_trend.png" class="w-full mt-4 rounded-lg shadow-sm" />

<div class="mt-4 pl-5 border-l-3 border-teal-300 text-base opacity-60">
  Net Change 趋近零线——解决速度追上了创建速度，Backlog 不再膨胀
</div>

<!--
第四张趋势图：JIRA Issue 创建 vs 解决。

重点看橙色的 Net Change 线：从 10 月的高峰下降到接近零线。
这意味着 Issue 的解决速度追上了创建速度，Backlog 不再膨胀。

但注意：这不是因为创建变少了（红色柱子一直在），
而是解决速度在加快（蓝色柱子追上来了）。
AI 帮助团队更快地消化任务，但前提是问题定义要清晰。
-->

---
layout: default
---

# AI 使用两极分化 <carbon-chart-line class="inline text-teal-500" />

<img src="/5_ai_developer_scatter.png" class="mt-4 mx-auto rounded-lg shadow-sm" style="max-height: 420px;" />

<!--
最后一张：开发者 AI 使用分布散点图。

横轴是总 Commit 数（产出量），纵轴是 AI Co-Author 占比。
四个象限非常清晰：

右上：高产出 + 高 AI 使用——这就是"高手飞轮"。
左上：低产出但高 AI 使用——可能在学习或做探索性任务。
右下：高产出但低 AI 使用——传统高手，还没开始用 AI。
底部大量蓝点：AI 使用为零——还完全没有开始。

这张图最直观地展示了我们后面要讨论的"AI 格差"问题。
团队里的两极分化已经形成，需要主动治理。
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

# 组织挑战：处理团队断层

<div class="mt-2 text-base opacity-60">实践推广大多是自下而上的——让高手带动团队</div>

<div class="mt-8 flex items-stretch justify-center gap-5">

<div v-click class="flex-1 rounded-2xl bg-teal-50 border border-teal-200 p-6 shadow-sm flex flex-col items-center justify-center text-center">
  <carbon-user class="text-4xl mb-3 text-teal-600" />
  <div class="text-xl font-bold text-teal-800 mb-2">少数高手</div>
  <div class="text-sm text-teal-600 leading-relaxed">个体实践涌现<br/>效率提升显著</div>
</div>

<div v-click class="flex items-center flex-shrink-0">
  <carbon-arrow-right class="text-3xl text-gray-300" />
</div>

<div v-click class="flex-1 rounded-2xl bg-emerald-50 border border-emerald-200 p-6 shadow-sm flex flex-col items-center justify-center text-center">
  <carbon-events class="text-4xl mb-3 text-emerald-600" />
  <div class="text-xl font-bold text-emerald-800 mb-2">团队共识</div>
  <div class="text-sm text-emerald-600 leading-relaxed">Memory/Skill 可沉淀<br/>经验可分享、可复用</div>
</div>

<div v-click class="flex items-center flex-shrink-0">
  <carbon-arrow-right class="text-3xl text-gray-300" />
</div>

<div v-click class="flex-1 rounded-2xl bg-purple-50 border border-purple-200 p-6 shadow-sm flex flex-col items-center justify-center text-center">
  <carbon-enterprise class="text-4xl mb-3 text-purple-600" />
  <div class="text-xl font-bold text-purple-800 mb-2">组织能力</div>
  <div class="text-sm text-purple-600 leading-relaxed">对齐拉平 AI 格差<br/>制度与工具跟进</div>
</div>

</div>

<div v-click class="mt-10 mx-auto pl-5 border-l-3 border-teal-300 text-xl opacity-50" style="max-width: 80%;">
  传统自上而下路径在这个周期里偏慢——等制度跟上，高手已经迭代三轮了
</div>

<!--
AI 的两极分化大部分是闻道有先后造成的。
但"少数人飞起、多数人观望"的组织问题是实际存在、需要解决的。

[click] 起点是少数高手——他们率先摸索出高效的 AI 使用方式，效率提升非常显著。
[click] 关键一步是形成团队共识——高手的 Memory 和 Skill 需要可沉淀、可分享、可复用。
不能停留在个人脑子里，要变成团队资产。
[click] 最终目标是组织能力——通过对齐和拉平 AI 格差，让整个团队的效率一起上来。
制度和工具要跟进，但不能等制度先行，要让高手先跑起来带动其他人。

[click] 补充一句：传统自上而下路径在这个周期里偏慢。
等制度设计好，高手可能已经迭代三轮了。正确的路径是自下而上：高手先跑，沉淀经验，团队复用，最后制度兜底。
-->

---
layout: default
---

# 释放高手，沉淀实践

<div class="mt-2 text-base opacity-60">尊重高手的判断——让他们自由编排工具与工作流</div>

<div class="mt-8 space-y-8">

<div v-click class="pl-5 border-l-3 border-teal-300">
  <div class="flex items-center gap-2 mb-1">
    <carbon-explore class="text-lg text-teal-600" />
    <span class="font-bold text-lg">没有公认的最佳实践——让高手先跑</span>
  </div>
  <div class="text-base opacity-60 leading-relaxed">业界仍在摸索，过早统一标准反而限制探索空间。在安全合规的底线之上，放手让有好奇心的核心开发者自由编排。</div>
</div>

<div v-click class="pl-5 border-l-3 border-teal-300">
  <div class="flex items-center gap-2 mb-1">
    <carbon-compare class="text-lg text-teal-600" />
    <span class="font-bold text-lg">鼓励多 Harness 并存与比较</span>
  </div>
  <div class="text-base opacity-60 leading-relaxed">Claude Code、Codex、Pi、OpenCode……让高手充分体验每个工具的长短，抽选甚至构建最适合团队的 Harness。</div>
</div>

<div v-click class="pl-5 border-l-3 border-teal-500 bg-teal-50/50 py-4 pr-4 rounded-r-lg">
  <div class="flex items-center gap-2 mb-1">
    <carbon-build-tool class="text-lg text-teal-600" />
    <span class="font-bold text-lg">自定义 Harness 已不再遥不可及</span>
  </div>
  <div class="text-base opacity-60 leading-relaxed">以前需要大量开发且难以维护；现在在 AI Agent 的帮助下，团队级定制开发已完全可行。<br/><b>Domain 知识 × Agent 实践 = 团队的最大贡献。</b></div>
</div>

</div>

<!--
承接上一页：团队里确实存在高手，怎么用好他们？

核心观点：要让团队的 AI 使用方式发生突破，就必须尊重高手的判断，
让他们自由地编排自己需要的工具和工具链。

[click] 第一，业界目前没有公认的最佳实践，大家都还在摸索和探索。
这个时候去强调团队统一标准，或者试图确定哪一个方案是绝对的最佳实践，是不现实的。
在安全合规的底线之上，应该让有好奇心的核心开发者尽情探索。

[click] 第二，鼓励多 Harness 并存。Claude Code 是一套 Harness，Codex 是一套，
OpenCode、Pear 也是。允许团队在不同 Harness 之间尝试，
充分理解每个工具的长短，然后想办法抽选出最适合团队的方案，
甚至在需要的时候构建自己的 Harness。

[click] 第三，自定义 Harness 以前几乎不可能——需要大量开发且难以维护。
但现在在 Vibe Coding 和 AI Agent 的帮助下，这种级别的团队定制开发已经变得完全可行。
最了解项目的人，结合 Agent 实践，摸索出来的方法就是对团队最大的贡献。
-->

---
layout: default
---

# Memory & Skill 沉淀

<div class="mt-2 text-base opacity-60">Memory 整理沉淀，Skill 分享复用——面向未来的基础建设</div>

<div class="mt-6 grid grid-cols-2 gap-6">

<div>
<div v-click class="flex items-center gap-2 mb-3">
  <carbon-data-structured class="text-xl text-teal-600" />
  <span class="font-bold text-lg">Memory 分层体系</span>
</div>

<div v-click class="space-y-2">
  <div class="flex items-stretch gap-2">
    <div class="w-1 rounded-full bg-teal-600 flex-shrink-0"></div>
    <div class="flex-1 px-4 py-2.5 rounded-lg bg-teal-50 border border-teal-200">
      <div class="font-bold text-teal-800 text-sm">Project Memory</div>
      <div class="text-xs text-teal-600 mt-0.5">代码风格 · 整体架构 · 技术选型 · 全局共享</div>
    </div>
  </div>
  <div class="flex items-stretch gap-2">
    <div class="w-1 rounded-full bg-teal-500 flex-shrink-0"></div>
    <div class="flex-1 px-4 py-2.5 rounded-lg bg-teal-50 border border-teal-200">
      <div class="font-bold text-teal-800 text-sm">Module Memory</div>
      <div class="text-xs text-teal-600 mt-0.5">决策路径 · Spec 变更 · 踩坑记录 · 团队共享</div>
    </div>
  </div>
  <div class="flex items-stretch gap-2">
    <div class="w-1 rounded-full bg-teal-400 flex-shrink-0"></div>
    <div class="flex-1 px-4 py-2.5 rounded-lg bg-teal-50 border border-teal-200">
      <div class="font-bold text-teal-800 text-sm">Personal Memory</div>
      <div class="text-xs text-teal-600 mt-0.5">个人偏好与习惯 · 默认可见 · 鼓励共享</div>
    </div>
  </div>
</div>

<div v-click class="mt-3 text-xs opacity-50 pl-3 border-l-2 border-gray-300 leading-relaxed">
  逐步替代 Wiki → 本地化文档 + 索引<br/>面向未来的基础建设，让 Agent 主动消费知识
</div>
</div>

<div>
<div v-click class="flex items-center gap-2 mb-3">
  <carbon-catalog class="text-xl text-purple-600" />
  <span class="font-bold text-lg">Skill Marketplace</span>
</div>

<div v-click class="space-y-2">
  <div class="flex items-stretch gap-2">
    <div class="w-1 rounded-full bg-purple-600 flex-shrink-0"></div>
    <div class="flex-1 px-4 py-2.5 rounded-lg bg-purple-50 border border-purple-200">
      <div class="font-bold text-purple-800 text-sm">贡献</div>
      <div class="text-xs text-purple-600 mt-0.5">成员提交 Skill 到内部平台</div>
    </div>
  </div>
  <div class="flex items-stretch gap-2">
    <div class="w-1 rounded-full bg-purple-500 flex-shrink-0"></div>
    <div class="flex-1 px-4 py-2.5 rounded-lg bg-purple-50 border border-purple-200">
      <div class="font-bold text-purple-800 text-sm">精选</div>
      <div class="text-xs text-purple-600 mt-0.5">委员会评审，筛选高质量 Skill</div>
    </div>
  </div>
  <div class="flex items-stretch gap-2">
    <div class="w-1 rounded-full bg-purple-400 flex-shrink-0"></div>
    <div class="flex-1 px-4 py-2.5 rounded-lg bg-purple-50 border border-purple-200">
      <div class="font-bold text-purple-800 text-sm">共享</div>
      <div class="text-xs text-purple-600 mt-0.5">入选 Skill 合入 Repo，团队直接复用</div>
    </div>
  </div>
</div>
</div>

</div>

<!--
这一页讲两件事：Memory 的整理沉淀，和 Skill 的分享复用。

[click] 先看 Memory。基本思路是：把 repo 里的决策路径、Spec 修改记录、别人踩过的坑，都整理成结构化的 Memory。

[click] 三层结构：
- Project Memory：宏观层面的东西——代码风格、整体架构、技术选型，这些是全局性的约定。
- Module Memory：具体到每个模块的决策路径、Spec 变更、踩坑记录，粒度更细，以文档形式沉淀并索引。
- Personal Memory：个人偏好和习惯。这一层也鼓励共享——默认团队成员之间可以看到各自的 Memory。

[click] 现阶段我们还是基于当前的基建在做这件事，比如传统的 Wiki。但方向是逐步切换到本地化文档加索引的路径，提供更高效的检索方式，进一步共享团队的知识和记忆。
Memory 不一定现在就有特别大的用处，但它是面向未来的基础建设。Wiki 的问题大家都知道——没人看、更新不及时。而 Memory 可以暴露成 Skill，如果我们用自己的一套编排，在合适的时候让 Agent 自主地去发现和更新这些 Memory，效率会提高非常多。

[click] 再看 Skill。这边更直接——建一个公司内部的 Skill Marketplace。

[click] 流程三步：
- 贡献：任何成员都可以把成功经验封装成 Skill，提交到内部平台。
- 精选：委员会评审，筛选高质量的 Skill。
- 共享：通过评审的 Skill 合入 Repo，团队直接复用。

Memory 做沉淀，Skill 做分享，两条腿走路。
-->

---
layout: default
---

# 约束三：协作范式在变

<div class="mt-6">

<div class="grid grid-cols-2 gap-8">
<div class="p-8 rounded-xl bg-gray-50 border border-gray-200 text-center" v-click>
  <div class="text-base text-gray-500 mb-2">当前</div>
  <div class="text-xl font-bold mb-4">人 → 多 Agent</div>
  <carbon-user class="text-3xl text-teal-500 mx-1" />
  <carbon-arrow-right class="text-2xl text-gray-400 mx-1" />
  <carbon-bot class="text-3xl text-gray-500 mx-1" />
  <carbon-bot class="text-3xl text-gray-500 mx-1" />
  <carbon-bot class="text-3xl text-gray-500 mx-1" />
  <div class="text-sm text-gray-500 mt-4">人工编排，注意力是瓶颈</div>
</div>

<div class="p-8 rounded-xl bg-teal-50 border border-teal-200 text-center" v-click>
  <div class="text-base text-teal-600 mb-2">下一阶段</div>
  <div class="text-xl font-bold text-teal-800 mb-4">Agent ↔ Agent</div>
  <carbon-bot class="text-3xl text-teal-500 mx-1" />
  <carbon-connect class="text-2xl text-teal-400 mx-1" />
  <carbon-bot class="text-3xl text-teal-500 mx-1" />
  <carbon-connect class="text-2xl text-teal-400 mx-1" />
  <carbon-bot class="text-3xl text-teal-500 mx-1" />
  <div class="text-sm text-teal-700 mt-4">自协作，人做策略与兜底</div>
</div>
</div>

<div class="mt-6 text-center text-base text-gray-500" v-click>
  直接驱动因子：开发者注意力稀缺
</div>

</div>

<!--
我们在团队里推进AI进程时，和项目里的高手们聊天和访谈时..
可能算是一个预言，或者说是未来的展望
开发的协作范式在变。

AI 时代前就不说了，人和人的关系，大家都熟悉

[click] 在当下，在卷"人指挥多 agent"——因为开发者注意力是稀缺资源。
典型场景：你同时开几个 agent，一个查代码，一个写实现，一个跑测试。
但这种手动编排多个 agent 是过渡态。

下一阶段会走向"多个智能体自行协作工作"——
人类更多做策略设定与异常兜底。
10x 开发者是人指挥多 agent，但"人均 10x"需要 agent 自协作。
-->

---
layout: default
---

# 现状：Human in the Loop

<div class="mt-2 text-base text-gray-500">中间过程已自动化，但起点和终点仍是人</div>

<div class="mt-10 flex items-center justify-center gap-4">

<div v-click class="flex-1 rounded-2xl bg-gray-50 border border-gray-200 p-6 shadow-sm flex flex-col items-center justify-center text-center">
  <carbon-user class="text-4xl mb-3 text-gray-600" />
  <div class="text-xl font-bold text-gray-800 mb-2">人启动</div>
  <div class="text-sm text-gray-500 leading-relaxed">打开 CLI / Agent App<br/>输入提示词</div>
</div>

<div v-click class="flex items-center flex-shrink-0">
  <carbon-arrow-right class="text-3xl text-gray-300" />
</div>

<div v-click class="flex-1 rounded-2xl bg-teal-50 border border-teal-200 p-6 shadow-sm flex flex-col items-center justify-center text-center">
  <carbon-bot class="text-4xl mb-3 text-teal-600" />
  <div class="text-xl font-bold text-teal-800 mb-2">Agent 执行</div>
  <div class="text-sm text-teal-600 leading-relaxed">跑完流程<br/>生成 PR 并提交</div>
</div>

<div v-click class="flex items-center flex-shrink-0">
  <carbon-arrow-right class="text-3xl text-gray-300" />
</div>

<div v-click class="flex-1 rounded-2xl bg-gray-50 border border-gray-200 p-6 shadow-sm flex flex-col items-center justify-center text-center">
  <carbon-user class="text-4xl mb-3 text-gray-600" />
  <div class="text-xl font-bold text-gray-800 mb-2">人审核</div>
  <div class="text-sm text-gray-500 leading-relaxed">Review 结果<br/>最终决策</div>
</div>

</div>

<div v-click class="mt-10 mx-auto pl-5 border-l-3 border-gray-300 text-xl text-gray-500" style="max-width: 80%;">
  我们的中期目标：把人从 Loop 中移除，走向无人值守
</div>

<!--
这一页先看现状：企业开发中，人在 Agent Loop 里的参与方式是什么样的？

[click] 第一步，人启动——坐到电脑前，打开 CLI 或者 Agent App，输入一段提示词，告诉 Agent 今天想做什么。
[click] 第二步，Agent 执行——跑完所有流程，生成一个 PR 提交出来，告知任务完成。
[click] 第三步，人审核——最后还是人去 Review、做最终决策。

中间过程确实已经自动化了，但整个 Loop 的起点是人，终点也是人。这就是现状。

[click] 如果我们想跨越这一点，最核心的就是把人的角色从整个 Loop 中去掉。
从 Human in the Loop，走向无人值守。接下来分两步讲：怎么去掉起点的人，怎么去掉终点的人。
-->

---
layout: default
---

# 去掉起点：自动触发

<div class="mt-2 text-base text-gray-500">CI/CD 时代的成熟工具链，可直接复用</div>

<div class="mt-8 space-y-4">

<div v-click class="flex items-stretch gap-3">
  <div class="w-1.5 rounded-full bg-teal-600 flex-shrink-0"></div>
  <div class="flex-1 px-5 py-4 rounded-xl bg-teal-50 border border-teal-200">
    <div class="font-bold text-teal-800 text-base">Webhook 事件触发</div>
    <div class="text-sm text-teal-600 mt-1">PR 提交、Issue 创建、Code Review 请求 → 自动启动 Agent</div>
  </div>
</div>

<div v-click class="flex items-stretch gap-3">
  <div class="w-1.5 rounded-full bg-teal-500 flex-shrink-0"></div>
  <div class="flex-1 px-5 py-4 rounded-xl bg-teal-50 border border-teal-200">
    <div class="font-bold text-teal-800 text-base">Cron 定时触发</div>
    <div class="text-sm text-teal-600 mt-1">Backlog 清理、依赖更新、自动化重构 → 无人坚守的持续改进</div>
  </div>
</div>

<div v-click class="flex items-stretch gap-3">
  <div class="w-1.5 rounded-full bg-teal-400 flex-shrink-0"></div>
  <div class="flex-1 px-5 py-4 rounded-xl bg-teal-50 border border-teal-200">
    <div class="font-bold text-teal-800 text-base">Pipeline 上游触发</div>
    <div class="text-sm text-teal-600 mt-1">CI 失败自动修复、构建完成触发部署、上游变更级联更新</div>
  </div>
</div>

</div>

<div v-click class="mt-8 mx-auto pl-5 border-l-3 border-teal-300 text-xl text-gray-500" style="max-width: 80%;">
  不需要人坐到电脑前——事件发生时，Agent 自动响应
</div>

<!--
怎么去掉起点的「人」？

其实从上一代 CI 自动化开始，已经有很多现成的工具可以做这件事。

[click] Webhook 事件触发——PR 提交、Issue 创建这些事件发生时，自动启动 Agent 来处理。
[click] Cron 定时触发——定时巡检、清理 Backlog、更新依赖，这些日常维护不需要人来发起。
[click] Pipeline 上游触发——CI 失败后自动修复，构建完成后自动触发部署，上游变更级联更新下游。

[click] 这些触发方式都是 CI/CD 时代成熟的工具链，直接复用就行。
做的内容有一部分是以前依靠脚本的，比如依赖更新，一些资源文件的生成等
另一些是 agent 时代的，自动重构，自主 CI 修复等
不需要人坐到电脑前打开工具输入提示词，事件发生时 Agent 自动响应。
起点解决相对容易，接下来看终点——验收怎么自动化。
-->

---
layout: default
---

# 去掉终点：自动验收

<div class="mt-2 text-base text-gray-500">验收标准前置，让 Agent 自证完成</div>

<div class="mt-8 space-y-4">

<div v-click class="flex items-stretch gap-3">
  <div class="w-1.5 rounded-full bg-purple-600 flex-shrink-0"></div>
  <div class="flex-1 px-5 py-4 rounded-xl bg-purple-50 border border-purple-200">
    <div class="font-bold text-purple-800 text-base">测试守门</div>
    <div class="text-sm text-purple-600 mt-1">单元 / 集成 / UI 测试全部通过 → 前置门槛</div>
  </div>
</div>

<div v-click class="flex items-stretch gap-3">
  <div class="w-1.5 rounded-full bg-purple-500 flex-shrink-0"></div>
  <div class="flex-1 px-5 py-4 rounded-xl bg-purple-50 border border-purple-200">
    <div class="font-bold text-purple-800 text-base">Agent Review</div>
    <div class="text-sm text-purple-600 mt-1">用另一个 Agent 做 Code Review → 交叉验证</div>
  </div>
</div>

<div v-click class="flex items-stretch gap-3">
  <div class="w-1.5 rounded-full bg-purple-400 flex-shrink-0"></div>
  <div class="flex-1 px-5 py-4 rounded-xl bg-purple-50 border border-purple-200">
    <div class="font-bold text-purple-800 text-base">视觉验证</div>
    <div class="text-sm text-purple-600 mt-1">自动跑起 App、按需自动操作、截图 / 录屏 → 自然语言断言的 E2E 测试</div>
  </div>
</div>

</div>

<div v-click class="mt-8 mx-auto pl-5 border-l-3 border-purple-300 text-xl text-gray-500" style="max-width: 80%;">
  先定义「怎么算做完」，再开始做——人只在异常时介入
</div>

<!--
起点解决了，终点怎么办？怎么去掉最后「人审核」这一步？

核心思路是：验收标准前置，让 Agent 自己证明任务完成。

[click] 第一层，测试守门——单元、集成、UI 测试全部通过，作为 PR 合入的前置条件。这是最基本的自动验收。
[click] 第二层，Agent Review——用另一个 Agent 来做 Code Review，交叉验证产出质量。不是自己改自己审，而是有独立的验证者。
[click] 第三层，视觉验证——自动把 App 跑起来，重放之前录制的 UI 操作流程，进行截图或录屏。
这个产出物有两个用途：一方面可以辅助人工验证，人类想看的其实就是操作过程和最终结果；
另一方面，现在的 AI 有很强的视觉能力，可以直接在视觉层面确认是否满足验收需求。

[click] 关键原则是：先定义「怎么算做完」，再开始做。
有了这套验收机制，人只需要在异常情况时介入，日常流程完全无人值守。
-->

---
layout: default
---

# 新时代的 BDD

<div class="mt-6">

<div v-click class="px-5 py-4 rounded-xl bg-teal-50 border border-teal-200 mb-6">
  <div class="font-bold text-teal-800 text-base mb-1">核心原则：每个任务必须有 Spec</div>
  <div class="text-sm text-teal-600">把任务切分为合理的单元，配备完整的、可追溯的文档，让无人值守的 Loop 能跑起来</div>
</div>

<div v-click class="mb-4 font-bold text-base">Spec 的形态因任务而异</div>

<div v-click class="grid grid-cols-2 gap-3">
  <div class="px-4 py-3 rounded-xl bg-gray-50 border border-gray-200">
    <div class="flex items-center gap-2">
      <carbon-pull-request class="text-xl text-teal-500 flex-shrink-0" />
      <div class="font-bold text-sm">PR Review</div>
    </div>
    <div class="text-sm text-gray-500 mt-1">Spec = PR Description</div>
  </div>
  <div class="px-4 py-3 rounded-xl bg-gray-50 border border-gray-200">
    <div class="flex items-center gap-2">
      <carbon-task class="text-xl text-teal-500 flex-shrink-0" />
      <div class="font-bold text-sm">Feature Issue</div>
    </div>
    <div class="text-sm text-gray-500 mt-1">Spec = 确认后的 Wiki 文档</div>
  </div>
  <div class="px-4 py-3 rounded-xl bg-gray-50 border border-gray-200">
    <div class="flex items-center gap-2">
      <carbon-debug class="text-xl text-teal-500 flex-shrink-0" />
      <div class="font-bold text-sm">Bug Fix</div>
    </div>
    <div class="text-sm text-gray-500 mt-1">Spec = QA Ticket 复现步骤</div>
  </div>
  <div class="px-4 py-3 rounded-xl bg-gray-50 border border-gray-200">
    <div class="flex items-center gap-2">
      <carbon-warning-alt class="text-xl text-teal-500 flex-shrink-0" />
      <div class="font-bold text-sm">CI Failure</div>
    </div>
    <div class="text-sm text-gray-500 mt-1">Spec = CI 错误 Log</div>
  </div>
</div>

</div>

<!--
从这一页开始，我们从「道」进入「术」。

前面几页讲的是趋势和方向——怎么把人从 Loop 中移除，走向无人值守。
那具体怎么做？术的第一点，就是任务切分。

[click] 核心原则：每个任务必须有 Spec。
把任务切分得合理、合适，配备完整的、可追溯的一组文档套件，让前面说的无人值守 Loop 真正跑起来。

[click] Spec 的形态因任务类型而异。

举几个例子：
- PR Review：Spec 就是 PR Description，描述变更意图和影响范围。
- Feature Issue：Spec 是和 Designer 或 Planner 确认好的 Wiki 文档。
- Bug Fix：Spec 是 Ticket 里 QA 汇报的复现步骤加期望行为。
- CI Failure：Spec 就更简单了，就是 CI 错误信息的 Log。

核心就是：在 AI 任务的起始点，必须有一个稳定的上下文告诉 AI 情况。
这个上下文可以是各种形态——PR Description、Wiki、Ticket、Log 都行，关键是它必须存在、必须可获取。
这就是新时代的 BDD：不是先写代码再补文档，而是先有 Spec，再让 Agent 按 Spec 执行、按 Spec 验收。
-->

---
layout: default
---

# 验收前置

<div class="text-base text-gray-500">先定义"怎么算做完"，再开始做</div>

<div class="mt-6 grid grid-cols-2 gap-5">

<div v-click class="px-6 py-5 rounded-xl bg-red-50 border border-red-200">
  <div class="flex items-center gap-2">
    <carbon-close-filled class="text-xl text-red-500 flex-shrink-0" />
    <div class="font-bold text-red-800 text-lg">事后生成测试</div>
  </div>
  <div class="text-base text-red-600 mt-2">把实现翻译成测试，低质量测试，人几乎无法验收</div>
</div>

<div v-click class="px-6 py-5 rounded-xl bg-teal-50 border border-teal-200">
  <div class="flex items-center gap-2">
    <carbon-checkmark-filled class="text-xl text-teal-500 flex-shrink-0" />
    <div class="font-bold text-teal-800 text-lg">根据 Spec 生成 Spec Test</div>
  </div>
  <div class="text-base text-teal-600 mt-2">Review 对象从代码变成 Spec，验收成本大幅降低</div>
</div>

<div v-click class="px-6 py-5 rounded-xl bg-gray-50 border border-gray-200">
  <div class="flex items-center gap-2">
    <carbon-translate class="text-xl text-teal-500 flex-shrink-0" />
    <div class="font-bold text-lg">BDD 天然贴近自然语言</div>
  </div>
  <div class="text-base text-gray-500 mt-2">LLM 做自然语言 → 自然语言的翻译，几乎无损</div>
</div>

<div v-click class="px-6 py-5 rounded-xl bg-teal-50 border border-teal-200">
  <div class="flex items-center gap-2">
    <carbon-user class="text-xl text-teal-500 flex-shrink-0" />
    <div class="font-bold text-lg">开发者的新任务</div>
  </div>
  <div class="text-base text-teal-600 mt-2">把 Idea 翻译成可自动化测试的案例</div>
</div>

</div>

<!--
验收前置：先定义"怎么算做完"，再开始做。

[click] 先说一个我们实践中发现的问题：观察到很多团队成员的做法是先让AI写好实现，然后事后生成测试。我们的经验是，这种做法没有太大用处。很多时候AI只是把实现代码翻译成了测试代码，并没有真正验证行为，或者验证得十分低效。
人去 Review 这些测试也非常困难——一个是量一般很多有没啥营养，另一个是你需要在脑中把代码语言翻译成原始的想法，和实际需要验证的东西对应起来。
这个过程太复杂了，耗时且难以抓到问题。

[click] 更正确的做法是：根据上下文，也就是 Spec，生成 Spec Test。
谁写的东西谁 review：人类应该 Review 的是驱动 AI 的 Spec，而不是 AI 写的代码。验收的对象从代码变成 Spec，记住这个 spec 是自然语言，人类读起来成本大幅降低。

[click] 为什么这种方式有效？因为 Specification Test 的写法天然贴近自然语言。
而 LLM 最擅长的就是在自然语言之间进行翻译。这种转换几乎是无损的，SOTA 模型处理这种翻译几乎不会出错，且确保人类可控的覆盖。相对于事后生成的 test，虽然你没看过 test 代码，但你的信心会高非常多。

[click] 所以在这个部分，开发者的任务就变成了：怎么把 Idea——特别是非技术人员的 Idea——翻译成可以自动化测试的案例。（语音输入，AI 辅助整理自然语言的测试案例 ... ）
这才是验收环节中人最该做的事情：去验收行为，而不是验收代码。
-->

---
layout: default
---

# 验收自动化：评估剧本

<div class="text-base text-gray-500">端到端验收是 Human-in-the-Loop 最重的一环——把它也自动化</div>

<div class="mt-4">

<div class="grid grid-cols-2 gap-6">

<div>
<div v-click class="font-bold text-lg mb-3">编写「评估剧本」</div>

<div v-click class="px-5 py-4 rounded-xl bg-gray-100 border border-gray-200 font-mono text-sm leading-loose">
<span class="text-gray-400">// 好友聊天功能验收</span><br/>
<span class="text-teal-800">1. <span class="bg-teal-200 text-teal-900 px-1.5 py-0.5 rounded text-xs font-bold">action</span> 点击「好友列表」Tab</span><br/>
<span class="text-purple-800">2. <span class="bg-purple-200 text-purple-900 px-1.5 py-0.5 rounded text-xs font-bold">eval</span> 列表内有内容填满</span><br/>
<span class="text-teal-800">3. <span class="bg-teal-200 text-teal-900 px-1.5 py-0.5 rounded text-xs font-bold">action</span> 点击第一个好友头像</span><br/>
<span class="text-purple-800">4. <span class="bg-purple-200 text-purple-900 px-1.5 py-0.5 rounded text-xs font-bold">eval</span> 画面迁移到聊天详情页</span><br/>
<span class="text-teal-800">5. <span class="bg-teal-200 text-teal-900 px-1.5 py-0.5 rounded text-xs font-bold">action</span> 发送文字消息 "hello"</span><br/>
<span class="text-purple-800">6. <span class="bg-purple-200 text-purple-900 px-1.5 py-0.5 rounded text-xs font-bold">eval</span> 消息气泡正常显示</span>
</div>

<div v-click class="mt-3 text-sm text-gray-500 pl-3 border-l-2 border-gray-300">
  自然语言写的 UI 测试——人能读、AI 能执行
</div>
</div>

<div>
<div v-click class="font-bold text-lg mb-3">执行与验收</div>

<div v-click class="px-5 py-4 rounded-xl bg-teal-50 border border-teal-200 space-y-2.5">
  <div class="flex items-center gap-4">
    <div class="w-8 h-8 rounded-full bg-teal-200 flex items-center justify-center flex-shrink-0 text-sm font-bold text-teal-700">1</div>
    <div class="font-bold text-base">Simulator 自动操作</div>
  </div>
  <div class="flex items-center gap-4">
    <div class="w-8 h-8 rounded-full bg-teal-200 flex items-center justify-center flex-shrink-0 text-sm font-bold text-teal-700">2</div>
    <div class="font-bold text-base">自动截图或视频录制</div>
  </div>
  <div class="flex items-center gap-4">
    <div class="w-8 h-8 rounded-full bg-teal-200 flex items-center justify-center flex-shrink-0 text-sm font-bold text-teal-700">3</div>
    <div class="font-bold text-base">AI 视觉比对，逐步验收</div>
  </div>
</div>

<div v-click class="mt-5 px-5 py-3.5 rounded-xl bg-gray-50 border border-gray-200 space-y-2">
  <div class="flex items-center gap-2 text-base">
    <carbon-checkmark-filled class="text-teal-500 flex-shrink-0" />
    <span class="text-teal-800 font-semibold">语义级断言，天然抗 UI 重构</span>
  </div>
  <div class="flex items-center gap-2 text-base">
    <carbon-checkmark-filled class="text-teal-500 flex-shrink-0" />
    <span class="text-teal-800 font-semibold">非技术人员可直接编写验收标准</span>
  </div>
</div>
</div>

</div>

</div>

<!--
端到端的验收，可能是 Human-in-the-Loop 里最重的一块。

以前的流程是：拿到 App 成品后，人工过一遍，新功能是否到位、各种行为是否符合预期。
这部分目前还是依赖人工参与，成本非常高。

[click] 我们的做法是写「评估剧本」。

[click] 什么是评估剧本？就是用自然语言写的 UI 测试。
比如：点击好友列表、确认列表有内容、点击某个好友、确认跳转到聊天页、发送一条消息、确认消息正常显示。
绿色的是操作指令，蓝色的是验收断言。人能读懂、AI 能执行——这就是 BDD 精神在端到端验收上的延伸。

[click] 自然语言写的 UI 测试，人和 AI 都能理解。

[click] 有了剧本，接下来就是执行与验收。

[click] 三步：
1. 用 Simulator 的自动化操作工具，按照评估剧本把整个过程跑一遍并录制下来。
2. 在每一步操作后自动截图，形成完整的视觉证据链。
3. 让 AI 对照评估剧本，逐步检查截图是否符合预期——利用 AI 的视觉能力做自动验收。

这样即使需要人工确认，人看到的也是截图和录屏，而不是让人去手动操作一遍。
大部分情况下 AI 视觉比对就能直接通过，人只需要在异常时介入。

[click] 这和传统 UI Test 有什么本质区别？两个关键点：

第一，语义级断言，天然抗 UI 重构。
传统 UI Test 的断言是 XCTAssert(label.text == "hello")，绑定控件 ID 和精确文本。UI 一重构，测试就挂。
评估剧本的断言是「消息气泡正常显示」——AI 通过视觉判断"看起来对不对"，跟人的验收方式一样。
只要产品行为没变，剧本就是稳定的，不需要随代码变更而维护。

第二，非技术人员可以直接编写验收标准。
传统 UI Test 只有开发者能写。评估剧本是自然语言，PM、QA、Designer 都能直接写。
这打通了"需求方直接定义验收条件"的最后一环——真正的 BDD 落地。
-->

---
layout: default
clicks: 4
---

# 闭环：Agent to Agent

<div class="mt-1 text-base text-gray-500">{{ $clicks >= 4 ? '完成后沉淀 Skill & Memory' : ($clicks >= 3 ? '每一轮都是一个独立的 Context' : ($clicks >= 2 ? '人定规矩，Agent 自主迭代' : ($clicks >= 1 ? '起点和终点都交给 Agent' : '中间过程已自动化，但起点和终点仍是人'))) }}</div>

<AgentLoopDiagram :step="$clicks" class="-mt-2" />

<!--
这一页把前面讲的内容串起来，做一个动画演示。

[初始状态] 回顾一下现状——人启动、Agent 执行、人审核。起点和终点都是人。

[click] 看变化：起点从「人启动」变成了「Trigger 启动」——事件、定时、上游触发自动发起任务。
终点从「人审核」变成了「Agent 自行验收」——测试守门、Agent Review、视觉验证，全自动完成。
整条链路上全是 Agent 了。

[click] 但光有一条链路还不够。验收可能不通过，需要迭代。
把这条链路缩小，扩展成三条并排——形成一个验证闭环。
验收不通过？自动触发下一轮。Agent 自己改、自己跑、自己验，直到通过为止。

关键看左边：人做的事变成了「定规矩」——一次性把 Spec 和验收标准定好，然后交给 Agent 自己去迭代。
Human 不在 Loop 里了，只在 Loop 开始前定义规则，然后退场。
这就是 Agent to Agent 的验证闭环。
-->

---
layout: default
---

# 一个实际案例

<div class="mt-4">

<div class="flex items-start gap-6">
<div class="flex-1">

<div class="mb-4 text-sm opacity-70">
  2~3 层 NavigationStack + 状态刷新 → UI 卡死
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

# 早期建设的建议

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
layout: end
---

<div class="text-center">
  <div class="text-2xl font-bold mb-6">Thank You!</div>
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
