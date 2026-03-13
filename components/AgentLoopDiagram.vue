<script setup>
const props = defineProps({
  step: { type: Number, default: 0 }
})
</script>

<template>
<div class="relative" style="height: 360px;">

  <!-- Layer 1: Single chain (step 0 & 1) -->
  <div
    class="absolute inset-0 flex items-center justify-center gap-4 transition-all duration-600"
    :class="step >= 2 ? 'opacity-0 scale-90 pointer-events-none' : 'opacity-100 scale-100'"
  >
    <!-- Box 1: 人启动 / Trigger 启动 -->
    <div
      class="flex-1 rounded-2xl border p-6 shadow-sm flex flex-col items-center justify-center text-center transition-all duration-1000 ease-in-out"
      :class="step >= 1 ? 'bg-teal-50 border-teal-200' : 'bg-gray-50 border-gray-200'"
    >
      <div class="relative w-10 h-10 mb-3">
        <carbon-user class="absolute inset-0 m-auto text-4xl text-gray-600 transition-opacity duration-1000" :class="step >= 1 ? 'opacity-0' : 'opacity-100'" />
        <carbon-flash class="absolute inset-0 m-auto text-4xl text-teal-600 transition-opacity duration-1000" :class="step >= 1 ? 'opacity-100' : 'opacity-0'" />
      </div>
      <div class="relative h-7 w-full mb-2">
        <div class="absolute inset-0 flex items-center justify-center text-xl font-bold text-gray-800 transition-opacity duration-1000" :class="step >= 1 ? 'opacity-0' : 'opacity-100'">人启动</div>
        <div class="absolute inset-0 flex items-center justify-center text-xl font-bold text-teal-800 transition-opacity duration-1000" :class="step >= 1 ? 'opacity-100' : 'opacity-0'">Trigger 启动</div>
      </div>
      <div class="relative h-10 w-full">
        <div class="absolute inset-0 flex items-center justify-center text-sm leading-relaxed text-gray-500 transition-opacity duration-1000" :class="step >= 1 ? 'opacity-0' : 'opacity-100'">打开 CLI / Agent App<br/>输入提示词</div>
        <div class="absolute inset-0 flex items-center justify-center text-sm leading-relaxed text-teal-500 transition-opacity duration-1000" :class="step >= 1 ? 'opacity-100' : 'opacity-0'">事件 / 定时<br/>上游触发</div>
      </div>
    </div>

    <carbon-arrow-right class="text-3xl text-gray-300 flex-shrink-0" />

    <!-- Box 2: Agent 执行 (always teal) -->
    <div class="flex-1 rounded-2xl bg-teal-50 border border-teal-200 p-6 shadow-sm flex flex-col items-center justify-center text-center">
      <carbon-bot class="text-4xl mb-3 text-teal-600" />
      <div class="text-xl font-bold text-teal-800 mb-2">Agent 执行</div>
      <div class="text-sm text-teal-600 leading-relaxed">跑完流程<br/>生成 PR 并提交</div>
    </div>

    <carbon-arrow-right class="text-3xl text-gray-300 flex-shrink-0" />

    <!-- Box 3: 人审核 / Agent 自行验收 -->
    <div
      class="flex-1 rounded-2xl border p-6 shadow-sm flex flex-col items-center justify-center text-center transition-all duration-1000 ease-in-out"
      :class="step >= 1 ? 'bg-teal-50 border-teal-200' : 'bg-gray-50 border-gray-200'"
    >
      <div class="relative w-10 h-10 mb-3">
        <carbon-user class="absolute inset-0 m-auto text-4xl text-gray-600 transition-opacity duration-1000" :class="step >= 1 ? 'opacity-0' : 'opacity-100'" />
        <carbon-checkmark-outline class="absolute inset-0 m-auto text-4xl text-teal-600 transition-opacity duration-1000" :class="step >= 1 ? 'opacity-100' : 'opacity-0'" />
      </div>
      <div class="relative h-7 w-full mb-2">
        <div class="absolute inset-0 flex items-center justify-center text-xl font-bold text-gray-800 transition-opacity duration-1000" :class="step >= 1 ? 'opacity-0' : 'opacity-100'">人审核</div>
        <div class="absolute inset-0 flex items-center justify-center text-xl font-bold text-teal-800 transition-opacity duration-1000" :class="step >= 1 ? 'opacity-100' : 'opacity-0'">Agent 自行验收</div>
      </div>
      <div class="relative h-10 w-full">
        <div class="absolute inset-0 flex items-center justify-center text-sm leading-relaxed text-gray-500 transition-opacity duration-1000" :class="step >= 1 ? 'opacity-0' : 'opacity-100'">Review 结果<br/>最终决策</div>
        <div class="absolute inset-0 flex items-center justify-center text-sm leading-relaxed text-teal-500 transition-opacity duration-1000" :class="step >= 1 ? 'opacity-100' : 'opacity-0'">Agent Review<br/>视觉验证</div>
      </div>
    </div>
  </div>

  <!-- Layer 2: Loop layout (step 2) -->
  <div
    class="absolute inset-0 flex items-center gap-3 transition-all duration-600"
    :class="step >= 2 ? 'opacity-100 scale-100' : 'opacity-0 scale-110 pointer-events-none'"
  >
    <!-- Left: Human pre-review -->
    <div class="flex-shrink-0 w-28 rounded-2xl bg-amber-50 border-2 border-amber-300 p-4 shadow-sm flex flex-col items-center text-center">
      <carbon-user class="text-3xl mb-2 text-amber-600" />
      <div class="font-bold text-amber-800 text-sm">定规矩</div>
      <div class="text-xs text-amber-500 mt-1 leading-relaxed">Spec<br/>验收标准</div>
    </div>

    <div class="flex flex-col items-center flex-shrink-0">
      <carbon-arrow-right class="text-xl text-amber-400" />
      <div class="text-xs text-amber-400 whitespace-nowrap">一次性</div>
    </div>

    <!-- Center: Loop area -->
    <div class="flex-1 relative rounded-2xl border-2 border-teal-300 bg-teal-50/20 px-3 pt-5 pb-4">
      <!-- Top label -->
      <div class="absolute -top-3 right-4 bg-white px-2.5 py-0.5 text-sm font-bold text-teal-600 flex items-center gap-1 rounded">
        <carbon-renew class="text-sm" /> Agent 自动循环
      </div>

      <div class="space-y-1">
        <!-- Chain 1 with Context -->
        <div class="relative rounded px-1.5 py-1 transition-all duration-700" :class="step >= 3 ? 'border border-dashed border-indigo-200/70 bg-indigo-50/15' : 'border border-transparent'">
          <span class="absolute -top-1.5 right-1 bg-white px-1 text-[9px] font-semibold text-indigo-300 leading-none transition-opacity duration-700" :class="step >= 3 ? 'opacity-100' : 'opacity-0'">Context</span>
          <div class="flex items-center gap-1">
            <div class="flex items-center gap-1 px-2 py-1 rounded-lg bg-teal-50 border border-teal-200">
              <carbon-flash class="text-sm text-teal-600" />
              <span class="text-xs font-bold text-teal-800">Trigger</span>
            </div>
            <carbon-arrow-right class="text-xs text-teal-300" />
            <div class="flex items-center gap-1 px-2 py-1 rounded-lg bg-teal-50 border border-teal-200">
              <carbon-bot class="text-sm text-teal-600" />
              <span class="text-xs font-bold text-teal-800">Agent</span>
            </div>
            <carbon-arrow-right class="text-xs text-teal-300" />
            <div class="flex items-center gap-1 px-2 py-1 rounded-lg bg-teal-50 border border-teal-200">
              <carbon-checkmark-outline class="text-sm text-teal-600" />
              <span class="text-xs font-bold text-teal-800">验收</span>
            </div>
          </div>
        </div>
        <!-- Separator 1 -->
        <div class="flex items-center gap-1 pl-3">
          <carbon-arrow-down class="text-xs text-teal-300" />
          <span class="text-xs text-teal-400">触发下一轮</span>
        </div>
        <!-- Chain 2 with Context -->
        <div class="relative rounded px-1.5 py-1 transition-all duration-700" :class="step >= 3 ? 'border border-dashed border-indigo-200/70 bg-indigo-50/15' : 'border border-transparent'">
          <span class="absolute -top-1.5 right-1 bg-white px-1 text-[9px] font-semibold text-indigo-300 leading-none transition-opacity duration-700" :class="step >= 3 ? 'opacity-100' : 'opacity-0'">Context</span>
          <div class="flex items-center gap-1">
            <div class="flex items-center gap-1 px-2 py-1 rounded-lg bg-teal-50 border border-teal-200">
              <carbon-flash class="text-sm text-teal-600" />
              <span class="text-xs font-bold text-teal-800">Trigger</span>
            </div>
            <carbon-arrow-right class="text-xs text-teal-300" />
            <div class="flex items-center gap-1 px-2 py-1 rounded-lg bg-teal-50 border border-teal-200">
              <carbon-bot class="text-sm text-teal-600" />
              <span class="text-xs font-bold text-teal-800">Agent</span>
            </div>
            <carbon-arrow-right class="text-xs text-teal-300" />
            <div class="flex items-center gap-1 px-2 py-1 rounded-lg bg-teal-50 border border-teal-200">
              <carbon-checkmark-outline class="text-sm text-teal-600" />
              <span class="text-xs font-bold text-teal-800">验收</span>
            </div>
          </div>
        </div>
        <!-- Separator 2 -->
        <div class="flex items-center gap-1 pl-3">
          <carbon-arrow-down class="text-xs text-teal-300" />
          <span class="text-xs text-teal-400">触发下一轮</span>
        </div>
        <!-- Chain 3 with Context -->
        <div class="relative rounded px-1.5 py-1 transition-all duration-700" :class="step >= 3 ? 'border border-dashed border-indigo-200/70 bg-indigo-50/15' : 'border border-transparent'">
          <span class="absolute -top-1.5 right-1 bg-white px-1 text-[9px] font-semibold text-indigo-300 leading-none transition-opacity duration-700" :class="step >= 3 ? 'opacity-100' : 'opacity-0'">Context</span>
          <div class="flex items-center gap-1">
            <div class="flex items-center gap-1 px-2 py-1 rounded-lg bg-teal-50 border border-teal-200">
              <carbon-flash class="text-sm text-teal-600" />
              <span class="text-xs font-bold text-teal-800">Trigger</span>
            </div>
            <carbon-arrow-right class="text-xs text-teal-300" />
            <div class="flex items-center gap-1 px-2 py-1 rounded-lg bg-teal-50 border border-teal-200">
              <carbon-bot class="text-sm text-teal-600" />
              <span class="text-xs font-bold text-teal-800">Agent</span>
            </div>
            <carbon-arrow-right class="text-xs text-teal-300" />
            <div class="flex items-center gap-1 px-2 py-1 rounded-lg bg-teal-50 border border-teal-200">
              <carbon-checkmark-outline class="text-sm text-teal-600" />
              <span class="text-xs font-bold text-teal-800">验收</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Bottom label -->
      <div class="absolute -bottom-3 left-4 bg-white px-2.5 py-0.5 text-xs text-teal-500 rounded flex items-center gap-1">
        <carbon-checkmark-filled class="text-teal-500" /> 通过 → Done
        <span class="mx-1 text-gray-300">·</span>
        <carbon-close-filled class="text-red-400" /> 不通过 → 迭代
      </div>
    </div>

    <!-- Right arrow -->
    <div class="flex flex-col items-center flex-shrink-0 transition-opacity duration-700" :class="step >= 4 ? 'opacity-100' : 'opacity-0'">
      <carbon-arrow-right class="text-xl text-violet-400" />
    </div>

    <!-- Right: Skill & Memory extraction -->
    <div class="flex-shrink-0 w-28 rounded-2xl bg-violet-50 border-2 border-violet-300 p-4 shadow-sm flex flex-col items-center text-center transition-all duration-700" :class="step >= 4 ? 'opacity-100 translate-x-0' : 'opacity-0 -translate-x-4 pointer-events-none'">
      <carbon-save class="text-3xl mb-2 text-violet-600" />
      <div class="font-bold text-violet-800 text-sm">做总结</div>
      <div class="text-xs text-violet-500 mt-1 leading-relaxed">提取 Skill<br/>沉淀 Memory</div>
    </div>
  </div>

</div>
</template>
