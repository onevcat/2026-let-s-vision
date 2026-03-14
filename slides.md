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
- 感谢组委会邀请，大周末来的各位
- 题目来由："做大一点好卖票"
- Agentic Engineering 话题太大且高速变化
- [click] 划掉副标题 → 真实定位：个人和团队的 AI agent 心得分享
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
- OpenClaw 龙虾出圈，意义和启发
- [click] Peter 社媒发布：理想中 Geek 的样子
- 理想 vs 现实的差距
- [click] 实际使用——AI 从办公桌渗透到厨房
- Geek 的未来：与 AI agent 共存
-->

---
layout: new-section
---

# 身在此山中

<div class="flex justify-center">
<div class="text-left space-y-3">
<p class="!opacity-80 !text-3xl flex items-center"><carbon-map class="text-slate-400 mr-2 text-3xl flex-shrink-0" />我们是怎么走到今天这一步的？</p>
<p class="!opacity-80 !text-3xl flex items-center"><carbon-compass class="text-slate-400 mr-2 text-3xl flex-shrink-0" />为今后的工程决策定坐标</p>
</div>
</div>

<!--
- 讨论未来前，先定位当下
- “不识庐山真面目，只缘身在此山中”
- 定坐标，判断当前位置，推断下一阶段
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
- [click] Phase I：Tab 补全，AI 第一次摸到代码
- [click] Phase II：Chatbot，强大但割裂，复制粘贴搬运
- [click] Phase III：AI Editor，读整个仓库，生成大段代码
- [click] Phase IV：Code Agent，自主运行/调试/提交
- 人从编码主体 → 辅助位/验收位
- 回顾是为了给工程决策定坐标
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
- 过渡：当前阶段，我们体会到，人逐渐成为瓶颈的瓶颈
- [click] 人类线：持续学习积累，但线性增长
- [click] 模型线：指数增长，Opus 4.5 / Codex 5.2 后感知明显
- [click] 感知阈值 = 大部分的工程师开始承认 AI 的能力远超自己
- [click] 人类工程师成为瓶颈。模型能力和配套设置发展太快，开发者工作上移：定义问题、设边界、做验收
-->

---
layout: new-section
---

# <carbon-chart-line-smooth class="inline text-slate-400 mr-2" /> 趋势汇报

<div class="mt-4 text-3xl opacity-70">
一个大型 iOS 开发团队的变化实例
</div>

<!--
- 我们今天做的是工程中的体验和实践分享
- 让大家对接下来的内容发生的尺度有个概念
- 个人身份，已公开范围内介绍
- 提供基准参照：实践发生在什么规模下
-->

---
layout: default
---

# 规模背景

<div v-click class="mt-4 flex items-center gap-2.5 text-lg font-semibold text-slate-400">
  <logos-swift class="text-xl" /> Swift + Objective-C
</div>

<div v-click>
  <div class="mt-5 flex items-baseline">
    <span class="text-[7rem] font-black leading-none tracking-tighter"><span class="text-slate-300">~</span><span class="text-slate-800">250</span></span>
    <span class="text-2xl font-bold text-slate-400 ml-3">万行代码</span>
  </div>
  <div class="w-16 h-1 bg-slate-200 rounded-full mt-6 mb-8"></div>
</div>

<div class="flex gap-16">
  <div v-click class="flex items-baseline gap-2">
    <span class="text-4xl font-black text-slate-600 tracking-tight">~650</span>
    <span class="text-base text-slate-400">模块</span>
  </div>
  <div v-click class="flex items-baseline gap-2">
    <span class="text-4xl font-black text-slate-600 tracking-tight">25,000</span>
    <span class="text-base text-slate-400">文件</span>
  </div>
</div>

<div class="mt-10 text-lg text-slate-400" v-click>
  覆盖全局困难，很多小项目和个人项目中不存在的挑战，需要系统化的工程方法
</div>

<!--
- 规模背景（脱敏），建立"问题难度感"
- [click] Swift + ObjC
- [click] ~250 万行代码
- [click] ~650 个模块
- [click] ~25,000 个文件
- [click] 这个规模下单 agent 难覆盖全局，需系统化工程方法
- 更具体一些的这段时间的开发者体验的样本
-->

---
layout: default
---

# 每周 PR 数量 <carbon-chart-line class="inline text-slate-400" />

<img src="/1_weekly_pr_count.png" class="w-full mt-4 rounded-lg shadow-sm" />

<div class="mt-4 text-base text-slate-400">
  PR 总量保持稳定，趋势线微降——<strong class="text-slate-600">不是产出变少了，而是 PR 粒度在变大</strong>
</div>

<!--
- 趋势图：每周 PR 数量
- 趋势线微降，整体量级稳定
- 不是产出少了——PR 粒度在变大
- Agent 一次完成更完整的任务，单 PR 改动量增加
- 生产模式在变化
-->

---
layout: default
---

# PR 合并效率 <carbon-chart-line class="inline text-slate-400" />

<img src="/2_monthly_merge_time.png" class="w-full mt-4 rounded-lg shadow-sm" />

<div class="mt-4 text-base text-slate-400">
  均值从 50+ 小时降至 20 小时，中位数降至个位——<strong class="text-slate-600">Review 效率在倍增</strong>
</div>

<!--
- 趋势图：PR 平均合并时间
- 均值 51h → 20h，中位数降至 6.5h
- AI 生成的 PR 更规范、更容易 review
- 团队适应新节奏：从"等人看"到主动快速验收
-->

---
layout: default
---

# AI 协作占比 <carbon-chart-line class="inline text-slate-400" />

<img src="/3_ai_coauthor_trend.png" class="w-full mt-4 rounded-lg shadow-sm" />

<div class="mt-4 text-base text-slate-400">
  半年内从 1% 飙升至 40%——<strong class="text-slate-600">AI 协作已从尝鲜变为常态</strong>
</div>

<!--
- 趋势图：AI Co-Authored PR 占比
- 半年：1.1% → 39.8%，近 40 倍
- 指数型增长，2025 年底加速
- 与模型能力台阶式提升吻合
- 从少数人尝鲜变成团队日常
-->

---
layout: default
---

# Issue 消化趋势 <carbon-chart-line class="inline text-slate-400" />

<img src="/4_jira_issue_trend.png" class="w-full mt-4 rounded-lg shadow-sm" />

<div class="mt-4 text-base text-slate-400">
  Net Change 趋近零线——<strong class="text-slate-600">解决速度追上了创建速度，Backlog 不再膨胀</strong>
</div>

<!--
- 趋势图：Issue 创建 vs 解决
- Net Change 从高峰降至零线附近
- 不是创建变少，是解决速度追上了
- AI 加速消化任务，前提是问题定义清晰
-->

---
layout: default
---

# AI 使用两极分化 <carbon-chart-line class="inline text-slate-400" />

<img src="/5_ai_developer_scatter.png" class="mt-4 mx-auto rounded-lg shadow-sm" style="max-height: 420px;" />

<!--
- 散点图：横轴 Commit 数，纵轴 AI Co-Author 占比
- 右上：高产出 + 高 AI = 高手飞轮
- 左上：低产出高 AI = 学习/探索中
- 右下：高产出低 AI = 传统高手未启用
- 底部大量蓝点 = 完全没有开始
- 直观展示"AI 格差"，两极分化需主动治理
-->

---
layout: center
---

<div class="flex flex-col items-center justify-center h-full">
  <div class="text-6xl font-bold tracking-tight">序章已经落下</div>
  <div class="w-24 h-1 bg-slate-300 rounded-full mt-6 mb-8"></div>

  <div class="flex gap-2 w-full max-w-2xl" style="transform: scale(0.7); transform-origin: center;">
    <TimelineStage label="Phase I" title="Tab 补全">AI 进入编码动作</TimelineStage>
    <TimelineStage label="Phase II" title="Chatbot">同步提示-响应回路</TimelineStage>
    <TimelineStage label="Phase III" title="AI Editor">仓内上下文协作</TimelineStage>
    <TimelineStage label="Phase IV" title="Code Agent">长任务 / 少指令 / 自主</TimelineStage>
  </div>

  <v-click>
    <div class="mt-8 flex gap-8 text-base tracking-wide">
      <div class="flex items-start gap-2 opacity-60">
        <carbon-view class="text-slate-400 mt-0.5 flex-shrink-0" />
        <span>我们观察到的现象和实践</span>
      </div>
      <div class="flex items-start gap-2 opacity-60">
        <carbon-roadmap class="text-slate-400 mt-0.5 flex-shrink-0" />
        <span>推进中遇到的阻力与对策</span>
      </div>
    </div>
  </v-click>
</div>

<!--
- 经过一系列评估和业界实践，我想大方向已定：Code Agent 是理想的协作形态
- 四阶段是人类与 AI 共同编程的成果
- "序章已落下"——地基打好，人类科技树的这个分叉已经点亮
- 大量围绕于此的基建和生态正在蓬勃发展，后续也以此演化
- [click] 接下来分享的主要话题包含：
  - 观察到的现象和最佳实践
  - 推进 AI 落地的真实阻力与对策
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
- 其实在过程中遇到的课题非常多，今天只聊最重要的三个话题：
  1. 上下文工程——信息喂对喂好
  2. 团队化积累——高手做法推广沉淀
  3. 协作新范式——从人指挥到 Agent 自协作
- 每组：先看约束，再聊实践
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
- 模型 Context 有限：SOTA 200K-400K token
- 实际任务不断膨胀：多模块、复杂决策链
- [click] 1M 上下文不是万灵丹，塞越多问题越明显
- 推理成本飙升——attention 二次方
- Recall 下降——中间位置信息降超 30%
- 注意力涣散——输出质量不稳定
- 上下文管理依然非常重要
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
- 常见症状，遇到就知道上下文出问题了
- [click] 跳 context compact → 这次白干了
- [click] 反复”这里不对修一下” → 模型鬼打墙，recall 下降
- [click] “求求你别再动那个文件” → 边界信息丢失
- [click] “我们不是约好了么” → 架构约定被忘掉
- 不是偶发，是上下文有限的必然结果
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
  <div class="text-sm text-gray-500 mt-1">简化输出等</div>
</div>
<div class="p-5 rounded-lg bg-teal-50 border border-teal-100" v-click>
  <carbon-machine-learning-model class="text-3xl text-teal-500 mb-3" />
  <div class="font-bold text-lg">选择顶级模型</div>
  <div class="text-sm text-gray-500 mt-2">推理密集 ≠ 省 token 的地方</div>
  <div class="text-sm text-gray-500 mt-1">弱模型 → 错误积累 → 返工</div>
</div>
</div>

<!--
- 应对策略一：精简注入——只给必要信息
- [click] AGENTS.md ≤ 100 行，只写领域知识
- 行为式引用、渐进式披露，不一次全塞
- [click] 辅助脚本：模块查找/架构速查，减少盲目搜索
- 为 agent 优化工具输出
- [click] 选顶级模型别省钱
- 弱模型 → 错误 → 纠正消耗上下文 → 恶性循环
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
  <div class="text-sm text-gray-500 mt-1">一个任务一个会话，避免历史污染</div>
</div>
</div>
</div>

<!--
- 应对策略二：控制边界
- [click] 任务拆分：超过一个 context window → 必须拆
- 每个子任务 ≤ 1 window，明确边界与依赖
- 上下文压缩几乎致命
- [click] Sub-agent 有用，但前提是先拆好任务
- 新开 Thread：一个任务一个线程，避免历史污染
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
- 模型注意力 U 型分布：开头/最近强，中段弱
- 精简注入 → 规则放开头
- 控制边界 → 上下文短，避免关键信息被挤到中段
- 新开 thread → 任务描述始终在高注意力位
- 核心：管理信息在上下文中的位置和密度
- 类比：像管理早期移动设备内存一样管理 Context
- 过渡 → 第二组：AI 使用两极分化
-->

---
layout: default
---

# 约束二：Agent 的天花板还是看人

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
- Agent 天花板依然由使用者决定
- 同一工具，高手 vs 入门者效果天差地别
- [click] 高手：丰富 Memory + Skill，日解十多个 issue
- 入门者：零积累，差距数十倍
- [click] 差距远超 Agent 前时代（以前 2-3 倍顶天）
- 个人强 ≠ 组织强，不治理会变团队断层
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
- 两极分化需组织层面解决
- [click] 少数高手率先摸索，效率显著提升
- [click]（过渡箭头）
- [click] 团队共识：Memory/Skill 沉淀、分享、复用
- [click]（过渡箭头）
- [click] 组织能力：对齐拉平 AI 格差
- [click] 正确路径自下而上：高手先跑 → 沉淀 → 复用 → 制度兜底
-->

---
layout: default
---

# 释放高手，沉淀实践

<div class="mt-2 text-base opacity-60">尊重高手的判断——让他们自由编排工具与工作流</div>

<div class="mt-8 space-y-8">

<div v-click>
  <div class="flex items-center gap-2 mb-1">
    <carbon-explore class="text-xl text-teal-600" />
    <span class="font-bold text-lg">没有公认的最佳实践——让高手先跑</span>
  </div>
  <div class="text-base opacity-60 leading-relaxed ml-7">业界仍在摸索，过早统一标准反而限制探索空间。在安全合规的底线之上，放手让有好奇心的核心开发者自由编排。</div>
</div>

<div v-click>
  <div class="flex items-center gap-2 mb-1">
    <carbon-compare class="text-xl text-teal-600" />
    <span class="font-bold text-lg">鼓励多 Harness 并存与比较</span>
  </div>
  <div class="text-base opacity-60 leading-relaxed ml-7">Claude Code、Codex、Pi、OpenCode……让高手充分体验每个工具的长短，抽选甚至构建最适合团队的 Harness。</div>
</div>

<div v-click class="pl-5 border-l-3 border-teal-500 bg-teal-50/50 py-4 pr-4 rounded-r-lg">
  <div class="flex items-center gap-2 mb-1">
    <carbon-build-tool class="text-xl text-teal-600" />
    <span class="font-bold text-lg">自定义 Harness 已不再遥不可及</span>
  </div>
  <div class="text-base opacity-60 leading-relaxed">以前需要大量开发且难以维护；现在在 AI Agent 的帮助下，团队级定制开发已完全可行。<br/><b>Domain 知识 × Agent 实践 = 团队的最大贡献。</b></div>
</div>

</div>

<!--
- 尊重高手判断，让他们自由编排工具链
- [click] 没有公认最佳实践，过早统一标准限制探索
- 安全合规底线上，放手让核心开发者探索
- [click] 鼓励多 Harness 并存：Claude Code / Codex / OpenCode
- 充分体验长短，抽选最适合团队的方案
- [click] 自定义 Harness 已可行——AI 让团队定制开发成本大降
- Domain 知识 × Agent 实践 = 团队最大贡献
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

<div v-click class="mt-3 text-xs opacity-50 pl-3 leading-relaxed">
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
- 两件事：Memory 沉淀 + Skill 分享
- [click] Memory：整理决策路径、Spec 记录、踩坑记录
- [click] 三层：Project（全局）→ Module（模块级）→ Personal（个人，鼓励共享）
- [click] 现阶段基于 Wiki，方向是本地化文档 + 索引
- 面向未来基础建设，让 Agent 主动消费知识
- [click] Skill Marketplace：内部共享平台
- [click] 贡献 → 精选（委员会评审）→ 共享（合入 Repo）
- Memory 做沉淀，Skill 做分享
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
- 协作范式在变
- [click] 当前：人指挥多 Agent，注意力是瓶颈
- 手动编排是过渡态
- [click] 下一阶段：Agent ↔ Agent 自协作
- 人做策略设定与异常兜底
- 10x 是人指挥多 agent，"人均 10x"需要 agent 自协作
- [click] 直接驱动因子：开发者注意力稀缺
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

<div v-click class="mt-10 text-xl text-center text-slate-400">
  我们的中期目标：把人从 Loop 中移除，走向<strong class="text-slate-600">无人值守</strong>
</div>

<!--
- 现状：人在 Agent Loop 中的参与方式
- [click] 人启动：打开 CLI，输入提示词
- [click]（过渡箭头）
- [click] Agent 执行：跑完流程，生成 PR
- [click]（过渡箭头）
- [click] 人审核：Review，最终决策
- 起点是人，终点也是人
- [click] 目标：把人从 Loop 中移除 → 无人值守
- 分两步：去掉起点 + 去掉终点
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

<div v-click class="mt-8 text-xl text-center text-slate-400">
  不需要人坐到电脑前——事件发生时，<strong class="text-slate-600">Agent 自动响应</strong>
</div>

<!--
- 去掉起点，CI/CD 成熟工具链可复用
- [click] Webhook 事件触发：PR/Issue/Review → 自动启动 Agent
- [click] Cron 定时触发：巡检/清理/更新，无人坚守
- [click] Pipeline 上游触发：CI 失败自动修复，上游变更级联
- [click] 事件发生时 Agent 自动响应，不需人坐到电脑前
- 起点相对容易 → 接下来看终点
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
- 去掉终点，验收标准前置，Agent 自证完成
- [click] 测试守门：单元/集成/UI 全通过 = 前置门槛
- [click] Agent Review：独立 Agent 做 Code Review，交叉验证
- [click] 视觉验证：自动跑 App + 截图/录屏 + AI 视觉比对
- [click] 原则：先定义"怎么算做完"，再开始做
- 人只在异常时介入
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
      <carbon-pull-request class="text-xl text-slate-500 flex-shrink-0" />
      <div class="font-bold text-sm">PR Review</div>
    </div>
    <div class="text-sm text-gray-500 mt-1">Spec = PR Description</div>
  </div>
  <div class="px-4 py-3 rounded-xl bg-gray-50 border border-gray-200">
    <div class="flex items-center gap-2">
      <carbon-task class="text-xl text-slate-500 flex-shrink-0" />
      <div class="font-bold text-sm">Feature Issue</div>
    </div>
    <div class="text-sm text-gray-500 mt-1">Spec = 确认后的 Wiki 文档</div>
  </div>
  <div class="px-4 py-3 rounded-xl bg-gray-50 border border-gray-200">
    <div class="flex items-center gap-2">
      <carbon-debug class="text-xl text-slate-500 flex-shrink-0" />
      <div class="font-bold text-sm">Bug Fix</div>
    </div>
    <div class="text-sm text-gray-500 mt-1">Spec = QA Ticket 复现步骤</div>
  </div>
  <div class="px-4 py-3 rounded-xl bg-gray-50 border border-gray-200">
    <div class="flex items-center gap-2">
      <carbon-warning-alt class="text-xl text-slate-500 flex-shrink-0" />
      <div class="font-bold text-sm">CI Failure</div>
    </div>
    <div class="text-sm text-gray-500 mt-1">Spec = CI 错误 Log</div>
  </div>
</div>

</div>

<!--
- 从「道」进入「术」——具体怎么做
- [click] 核心原则：每个任务必须有 Spec
- 配备完整文档，让无人值守 Loop 跑起来
- [click] Spec 形态因任务而异
- [click] PR Review → PR Description
- Feature → 确认后的 Wiki
- Bug Fix → QA Ticket 复现步骤
- CI Failure → CI 错误 Log
- 先有 Spec → Agent 按 Spec 执行和验收 = 新时代 BDD
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
- 先定义"怎么算做完"
- [click] 事后生成测试无用：AI 只是把实现翻译成测试，不验证行为
- 人 Review 这些测试也很困难
- [click] 正确做法：根据 Spec 生成 Spec Test
- Review 对象从代码变成 Spec（自然语言），成本大降
- [click] BDD 天然贴近自然语言
- LLM 做自然语言→自然语言翻译几乎无损
- [click] 开发者新任务：把 Idea 翻译成可自动化测试的案例
- 验收行为，而非验收代码
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

<div v-click class="mt-3 text-sm text-gray-500 pl-3">
  自然语言写的 UI 测试——人能读、AI 能执行
</div>
</div>

<div>
<div v-click class="font-bold text-lg mb-3">执行与验收</div>

<div v-click class="px-5 py-4 rounded-xl bg-teal-50 border border-teal-200 space-y-2.5">
  <div class="flex items-center gap-4">
    <div class="w-8 h-8 rounded-full bg-teal-200 flex items-center justify-center flex-shrink-0 text-sm font-bold text-teal-700">1</div>
    <div class="font-bold text-lg">Simulator 自动操作 (a18y, Vision 等)</div>
  </div>
  <div class="flex items-center gap-4">
    <div class="w-8 h-8 rounded-full bg-teal-200 flex items-center justify-center flex-shrink-0 text-sm font-bold text-teal-700">2</div>
    <div class="font-bold text-lg">获取关键信息、截图或视频录制</div>
  </div>
  <div class="flex items-center gap-4">
    <div class="w-8 h-8 rounded-full bg-teal-200 flex items-center justify-center flex-shrink-0 text-sm font-bold text-teal-700">3</div>
    <div class="font-bold text-lg">决定性断言 + 模型语义断言，逐步验收</div>
  </div>
</div>

<div v-click class="mt-5 px-5 py-3.5 rounded-xl bg-gray-50 border border-gray-200 space-y-2">
  <div class="flex items-center gap-2 text-base">
    <carbon-checkmark-filled class="text-teal-500 flex-shrink-0" />
    <span class="text-teal-800 font-semibold">语义级操作 + 断言，天然抗 UI 重构</span>
  </div>
  <div class="flex items-center gap-2 text-base">
    <carbon-checkmark-filled class="text-teal-500 flex-shrink-0" />
    <span class="text-teal-800 font-semibold">非技术人员也可参与编写验收标准</span>
  </div>
</div>
</div>

</div>

</div>

<!--
- 端到端验收是 Loop 中最重的一环
- [click] 做法：写「评估剧本」
- [click] 自然语言 UI 测试：action（操作）+ eval（断言）交替
- 人能读、AI 能执行 = BDD 在 E2E 的延伸
- [click] 自然语言写的 UI 测试，人和 AI 都能理解
- [click] 执行与验收
- [click] 三步：Simulator 自动操作 → 自动截图 → AI 视觉比对
- 人看截图和录屏，不用手动操作
- [click] 两大优势：
  - 语义级断言，天然抗 UI 重构
  - 非技术人员可直接编写验收标准
-->

---
layout: default
clicks: 4
---

# 闭环：Agent to Agent

<div class="mt-1 text-base text-gray-500">{{ $clicks >= 4 ? '完成后沉淀 Skill & Memory' : ($clicks >= 3 ? '每一轮都是一个独立的 Context' : ($clicks >= 2 ? '人定规矩，Agent 自主迭代' : ($clicks >= 1 ? '起点和终点都交给 Agent' : '中间过程已自动化，但起点和终点仍是人'))) }}</div>

<AgentLoopDiagram :step="$clicks" class="-mt-2" />

<!--
- 串联前面所有内容
- 初始：人启动 → Agent 执行 → 人审核
- [click] 起点 → Trigger，终点 → Agent 自行验收，全链路 Agent
- [click] 扩展为自动循环：不通过 → 自动触发下一轮
- 人只"定规矩"，一次性定好 Spec 和验收标准
- [click] 每一轮都是独立 Context
- [click] 完成后沉淀 Spark：记忆和经验
-->

---
layout: default
---

# 案例：NavigationStack 假死排障 — Spec 定义

<div class="mt-1 text-sm text-gray-500">人的工作：从 Ticket 到可执行的 Spec</div>

<div class="mt-4 grid grid-cols-2 gap-6">

<div class="space-y-3">
  <div class="flex items-start gap-3 p-3 rounded-xl bg-slate-50 border border-slate-200" v-click>
    <div class="w-7 h-7 rounded-full bg-teal-100 text-teal-700 flex items-center justify-center text-xs font-bold flex-shrink-0 mt-0.5">1</div>
    <div>
      <div class="text-sm font-bold text-slate-700">收到 Ticket</div>
      <div class="text-xs text-slate-500 mt-0.5">QA 报告：iOS 18 下多层页面跳转后 UI 假死，需强杀重启</div>
    </div>
  </div>
  <div class="flex items-start gap-3 p-3 rounded-xl bg-slate-50 border border-slate-200" v-click>
    <div class="w-7 h-7 rounded-full bg-teal-100 text-teal-700 flex items-center justify-center text-xs font-bold flex-shrink-0 mt-0.5">2</div>
    <div>
      <div class="text-sm font-bold text-slate-700">喂给 LLM，生成剧本</div>
      <div class="text-xs text-slate-500 mt-0.5">将 Ticket 描述直接输入大语言模型<br/>LLM 输出结构化排障剧本：复现步骤 + 验收条件</div>
    </div>
  </div>
  <div class="flex items-start gap-3 p-3 rounded-xl bg-slate-50 border border-slate-200" v-click>
    <div class="w-7 h-7 rounded-full bg-teal-100 text-teal-700 flex items-center justify-center text-xs font-bold flex-shrink-0 mt-0.5">3</div>
    <div>
      <div class="text-sm font-bold text-slate-700">人审 Spec，确认交付</div>
      <div class="text-xs text-slate-500 mt-0.5">开发者过一遍：补充已知信息（iOS 26 正常）、修正方向<br/>确认后交给 Agent</div>
    </div>
  </div>
  <div class="mt-2 text-xs text-gray-400 pl-2" v-click>人的工作到此为止 → 接下来交给 Agent Loop</div>
</div>

<div v-click>
  <div class="font-bold text-base mb-3">Spec 剧本产出</div>
  <div class="px-4 py-3 rounded-xl bg-gray-100 border border-gray-200 font-mono text-sm leading-loose">
    <span class="text-slate-600">0. <span class="bg-slate-200 text-slate-600 px-1.5 py-0.5 rounded text-xs font-bold">setup</span> 已登录 App，在首页</span><br/>
    <span class="text-teal-800">1. <span class="bg-teal-200 text-teal-900 px-1.5 py-0.5 rounded text-xs font-bold">action</span> 点击底栏「设置」Tab</span><br/>
    <span class="text-purple-800">2. <span class="bg-purple-200 text-purple-900 px-1.5 py-0.5 rounded text-xs font-bold">eval</span> 进入设置页，顶部显示用户头像</span><br/>
    <span class="text-teal-800">3. <span class="bg-teal-200 text-teal-900 px-1.5 py-0.5 rounded text-xs font-bold">action</span> 点击「账号管理」进入二级页</span><br/>
    <span class="text-purple-800">4. <span class="bg-purple-200 text-purple-900 px-1.5 py-0.5 rounded text-xs font-bold">eval</span> 导航正常推入，标题显示「账号管理」</span><br/>
    <span class="text-teal-800">5. <span class="bg-teal-200 text-teal-900 px-1.5 py-0.5 rounded text-xs font-bold">action</span> 点击「修改昵称」进入三级页</span><br/>
    <span class="text-purple-800">6. <span class="bg-purple-200 text-purple-900 px-1.5 py-0.5 rounded text-xs font-bold">eval</span> 页面正常显示，<strong>UI 可交互、未假死</strong></span>
  </div>
  <div class="mt-2 text-xs text-gray-500 pl-3">
    人能读、AI 能执行——与前面「评估剧本」格式一致
  </div>
</div>

</div>

<!--
- 实际案例：SwiftUI NavigationStack 假死
- [click] 收到 Ticket：iOS 18 下多层跳转后 UI 假死
- [click] 喂给 LLM：输出结构化排障剧本（复现 + 验收条件）
- [click] 人审 Spec：补充已知信息（iOS 26 正常），修正方向
- [click] 人的工作到此为止 → 交给 Agent Loop
- [click] Spec 剧本：action/eval 交替，验收条件 = UI 可交互未假死
-->

---
layout: default
---

# 案例：NavigationStack 假死排障 — Agent Loop

<div class="mt-1 text-sm text-gray-500">Agent 接手 Spec，每次迭代输出作为下一次的输入</div>

<div class="mt-4 relative">

<div class="space-y-2.5 max-w-2xl">
  <div class="flex items-center gap-3" v-click>
    <div class="w-20 flex-shrink-0 text-right">
      <div class="text-xs font-bold text-gray-500">迭代 1</div>
    </div>
    <div class="w-2 h-2 rounded-full bg-red-200 flex-shrink-0"></div>
    <div class="flex-1 p-3 rounded-xl bg-red-50 border border-red-100">
      <div class="text-sm"><strong class="text-red-700">假设</strong>：ViewModel 创建时机问题</div>
      <div class="text-xs text-red-600 mt-1">尝试在设置 NavigationPath 前创建 ViewModel → <strong>仍假死</strong>，排除此方向</div>
    </div>
  </div>

  <div class="flex items-center gap-3" v-click>
    <div class="w-20 flex-shrink-0 text-right">
      <div class="text-xs font-bold text-gray-500">迭代 2</div>
    </div>
    <div class="w-2 h-2 rounded-full bg-orange-200 flex-shrink-0"></div>
    <div class="flex-1 p-3 rounded-xl bg-orange-50 border border-orange-100">
      <div class="text-sm"><strong class="text-orange-700">假设</strong>：NavigationPath 状态冲突</div>
      <div class="text-xs text-orange-600 mt-1">隔离 path 管理为独立 ObservableObject → <strong>部分改善</strong>，方向接近</div>
    </div>
  </div>

  <div class="flex items-center gap-3" v-click>
    <div class="w-20 flex-shrink-0 text-right">
      <div class="text-xs font-bold text-gray-500">迭代 3</div>
    </div>
    <div class="w-2 h-2 rounded-full bg-amber-200 flex-shrink-0"></div>
    <div class="flex-1 p-3 rounded-xl bg-amber-50 border border-amber-100">
      <div class="text-sm"><strong class="text-amber-700">缩小范围</strong>：层级 ≥ 2 + push 时同步触发 State 更新</div>
      <div class="text-xs text-amber-600 mt-1">构建最小复现工程，3 个文件 → <strong>稳定复现</strong>，确认触发条件</div>
    </div>
  </div>

  <div class="flex items-center gap-3" v-click>
    <div class="w-20 flex-shrink-0 text-right">
      <div class="text-xs font-bold text-teal-500">迭代 4</div>
    </div>
    <div class="w-2 h-2 rounded-full bg-teal-200 flex-shrink-0"></div>
    <div class="flex-1 p-3 rounded-xl bg-teal-50 border border-teal-100">
      <div class="text-sm"><strong class="text-teal-700">修复</strong>：Model 链路断裂导致状态丢失不停重建</div>
      <div class="text-xs text-teal-600 mt-1">修正数据模型传递后假死消失 → <strong>自动验收通过</strong> ✓</div>
    </div>
  </div>
</div>

<div class="mt-4 flex items-center gap-4" v-click>
  <div class="flex-1 h-px bg-gray-200"></div>
  <div class="flex items-center gap-3 text-xs">
    <div class="px-3 py-1.5 rounded-full bg-teal-50 border border-teal-100 font-bold text-teal-600">Workaround 提交</div>
    <div class="px-3 py-1.5 rounded-full bg-violet-50 border border-violet-100 font-bold text-violet-600">写入团队 Memory</div>
    <div class="px-3 py-1.5 rounded-full bg-amber-50 border border-amber-100 font-bold text-amber-600">最小复现工程归档</div>
  </div>
  <div class="flex-1 h-px bg-gray-200"></div>
</div>

</div>

<!--
- Agent 接手 Spec，自主排障，类似二分法
- [click] 迭代 1：假设 ViewModel 创建时机 → 仍假死，排除
- [click] 迭代 2：假设 NavigationPath 状态冲突 → 部分改善，方向接近
- [click] 迭代 3：缩小范围，构建最小复现（3 文件）→ 稳定复现
- [click] 迭代 4：定位根因——Model 链路断裂 → 修复，验收通过
- [click] 产出：Workaround + 写入 Memory + 最小复现归档
- 全程无人介入
-->

---
layout: two-cols-header
clicks: 2
---

# 还有什么在变？

::left::

<CompareColumn title="正在弱化" variant="fading" :class="[$clicks >= 1 ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4', 'mr-3 transition-all duration-500']">
  <template #icon><carbon-arrow-down class="text-red-500" /></template>

  - **DRY** 的边际价值下降<br/><span class="text-sm text-slate-500">局部重复换取可理解性有时更优</span>
  - **语言/框架专精**不再是护城河<br/><span class="text-sm text-slate-500">AI 拉平了技术栈学习曲线，"我是 X 专家"的溢价在缩水</span>
  - 传统 **Code Review** 形态改变<br/><span class="text-sm text-slate-500">从审查"怎么写的"转向审查"要的是什么、结果对不对"</span>
  - **调试风格**正在转变<br/><span class="text-sm text-slate-500">强大的分析能力，简便的 log 追加能力；Debugger 被"弃用"</span>

</CompareColumn>

::right::

<CompareColumn title="正在增强" variant="rising" :class="[$clicks >= 2 ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-4', 'ml-3 transition-all duration-500']">
  <template #icon><carbon-arrow-up class="text-green-500" /></template>

  - **历史知识共享透明**<br/><span class="text-sm text-slate-500">几乎无穷的检索能力让团队或个人知识库的作用大幅提升</span>
  - **架构决策的杠杆**被放大<br/><span class="text-sm text-slate-500">模块边界清晰才能让多个 Agent 并行，设计选择影响倍增</span>
  - **自主改善**成为可能<br/><span class="text-sm text-slate-500">完备测试下的定时小任务、自动发 PR，代码库实现自我进化</span>
  - **为 Agent 而写**的时代<br/><span class="text-sm text-slate-500">API、注释、框架、乃至产品：第一消费者正在从人变成 Agent</span>

</CompareColumn>

<!--
- 三组核心话题之外，时间有限速览
- [click] 弱化：DRY 边际下降、语言专精拉平、Review 形态变化、调试风格转变
- [click] 增强：知识共享透明、架构杠杆放大、自主改善、为 Agent 而写
- 不是"少做工程"，是"重排工程优先级"
-->

---
layout: default
---

# 早期建设的建议

<div class="text-sm text-gray-500 -mt-2 mb-4">针对刚起步使用 AI 的个人和团队</div>

<div class="grid grid-cols-2 gap-5 mt-2">

<div class="rounded-xl bg-white border border-slate-200 shadow-sm p-5" v-click>
  <div class="flex items-center gap-2 mb-3">
    <div class="w-10 h-10 rounded-lg bg-slate-100 flex items-center justify-center"><carbon-certificate class="text-xl text-slate-600" /></div>
    <div class="font-bold text-lg">挑选靠谱的模型商</div>
  </div>
  <div class="text-sm text-slate-700 space-y-1 leading-relaxed">
    <div>· 优先选有完善 API + 稳定 SLA 的供应商</div>
    <div>· 关注上下文窗口和工具调用能力，而非只看跑分</div>
    <div>· 企业级先确认 data residency 和隐私政策</div>
  </div>
</div>

<div class="rounded-xl bg-white border border-slate-200 shadow-sm p-5" v-click>
  <div class="flex items-center gap-2 mb-3">
    <div class="w-10 h-10 rounded-lg bg-slate-100 flex items-center justify-center"><carbon-flash class="text-xl text-slate-600" /></div>
    <div class="font-bold text-lg">大量消耗 Token 做实践</div>
  </div>
  <div class="text-sm text-slate-700 space-y-1 leading-relaxed">
    <div>· 设置"token 使用目标"，而非使用限制</div>
    <div>· 同一任务用不同模型做 A/B 对比，建立直觉</div>
    <div>· 刻意试探失败边界，摸清能力天花板</div>
  </div>
</div>

<div class="rounded-xl bg-white border border-slate-200 shadow-sm p-5" v-click>
  <div class="flex items-center gap-2 mb-3">
    <div class="w-10 h-10 rounded-lg bg-slate-100 flex items-center justify-center"><carbon-migrate class="text-xl text-slate-600" /></div>
    <div class="font-bold text-lg">将现有工作流迁移到 AI</div>
  </div>
  <div class="text-sm text-slate-700 space-y-1 leading-relaxed">
    <div>· 从重复性工作入手：审查摘要、i18n、changelog</div>
    <div>· 先 AI 辅助，再 AI 主导。理解之前，不要一步到全自动</div>
    <div>· 建立"之前/之后"效果对照，用数据说服团队</div>
  </div>
</div>

<div class="rounded-xl bg-white border border-slate-200 shadow-sm p-5" v-click>
  <div class="flex items-center gap-2 mb-3">
    <div class="w-10 h-10 rounded-lg bg-slate-100 flex items-center justify-center"><carbon-idea class="text-xl text-slate-600" /></div>
    <div class="font-bold text-lg">不要过度纠结工具选型</div>
  </div>
  <div class="text-sm text-slate-700 space-y-1 leading-relaxed">
    <div>· 工具在快速迭代，今天的最优解三个月后可能变</div>
    <div>· 重要的是建立"与 AI 协作"的思维模式</div>
    <div>· 把精力花在理解约束，而非追逐功能</div>
  </div>
</div>

</div>

<!--
- 面向刚起步的团队和个人
- [click] 挑靠谱模型商：API 稳定、上下文够大、合规
- [click] 大量消耗 token：设预算不设限，A/B 对比，试边界
- [click] 工作流迁移：从重复性工作入手，先辅助再主导
- [click] 不纠结工具选型：工具会变，思维模式才是核心
-->

---
layout: default
---

# 中期建设的建议

<div class="text-sm text-gray-500 -mt-2 mb-4">针对已有实践经验、希望进一步提升的团队</div>

<div class="grid grid-cols-2 gap-5 mt-2">

<div class="rounded-xl bg-white border border-slate-200 shadow-sm p-5" v-click>
  <div class="flex items-center gap-2 mb-3">
    <div class="w-10 h-10 rounded-lg bg-violet-100 flex items-center justify-center"><carbon-meter class="text-xl text-violet-600" /></div>
    <div class="font-bold text-lg">建立团队 Harness 评测体系</div>
  </div>
  <div class="text-sm text-slate-700 space-y-1 leading-relaxed">
    <div>· 基于 domain 知识自建 harness，门槛已很低</div>
    <div>· 定期 benchmark，对比不同配置/模型的产出</div>
    <div>· 评测反馈为配置优化——"评测 → 调优"闭环</div>
  </div>
</div>

<div class="rounded-xl bg-white border border-slate-200 shadow-sm p-5" v-click>
  <div class="flex items-center gap-2 mb-3">
    <div class="w-10 h-10 rounded-lg bg-violet-100 flex items-center justify-center"><carbon-save class="text-xl text-violet-600" /></div>
    <div class="font-bold text-lg">团队经验沉淀</div>
  </div>
  <div class="text-sm text-slate-700 space-y-1 leading-relaxed">
    <div>· 成功的 prompt/skill 提炼为共享知识</div>
    <div>· 建立 AI 协作案例库——成功和失败都记录</div>
    <div>· 定期团队分享——缩小"AI 使用差距"</div>
  </div>
</div>

<div class="rounded-xl bg-white border border-slate-200 shadow-sm p-5" v-click>
  <div class="flex items-center gap-2 mb-3">
    <div class="w-10 h-10 rounded-lg bg-violet-100 flex items-center justify-center"><carbon-task-approved class="text-xl text-violet-600" /></div>
    <div class="font-bold text-lg">开始构建验收自动化</div>
  </div>
  <div class="text-sm text-slate-700 space-y-1 leading-relaxed">
    <div>· 从最关键的业务流程开始写评估剧本</div>
    <div>· 建立"变更 → 验证 → 回归"最小闭环</div>
    <div>· 逐步扩大 Agent 自主验收范围，为无人值守做准备</div>
  </div>
</div>

<div class="rounded-xl bg-white border border-slate-200 shadow-sm p-5" v-click>
  <div class="flex items-center gap-2 mb-3">
    <div class="w-10 h-10 rounded-lg bg-violet-100 flex items-center justify-center"><carbon-bot class="text-xl text-violet-600" /></div>
    <div class="font-bold text-lg">让基础设施变得 Agent-friendly</div>
  </div>
  <div class="text-sm text-slate-700 space-y-1 leading-relaxed">
    <div>· 文档和架构记录——从"给人看"到"给 Agent 消费"</div>
    <div>· 将知识结构化为可注入的 context 源</div>
    <div>· 内部工具提供 CLI/API，让 Agent 可直接调用</div>
  </div>
</div>

</div>

<!--
- 面向已有实践、希望系统化提升的团队
- [click] 建立 harness 评测：自建 benchmark，评测→调优闭环
- [click] 经验沉淀：高手 workflow 共享化、案例库、缩小格差
- [click] 验收自动化：核心路径写评估剧本，逐步扩大自主验收
- [click] Agent-friendly 基础设施：文档结构化、工具 CLI/API 化
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
- Q&A 常驻尾页
- 可接的问题方向：
  - 企业权限与安全落地
  - 模型与成本分层治理
  - 人工监督 → 无人值守过渡
  - Memory/Skill 最小可行版本
  - 个体飞轮与团队断层
-->
