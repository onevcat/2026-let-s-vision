<template>
  <div class="key-point">
    <div class="kp-icon">
      <slot name="icon" />
    </div>
    <div class="kp-body">
      <div class="kp-title">{{ title }}</div>
      <div class="kp-desc"><slot /></div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: { type: String, required: true },
})
</script>

<style scoped>
.key-point {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  padding: 16px 20px;
  border-radius: 10px;
  background: rgba(241, 245, 249, 0.6);
  border-left: 3px solid #3b82f6;
  transition: background 0.2s ease;
}

.key-point:hover {
  background: rgba(241, 245, 249, 0.9);
}

.kp-icon {
  font-size: 24px;
  color: #3b82f6;
  flex-shrink: 0;
  margin-top: 2px;
}

.kp-body {
  flex: 1;
}

.kp-title {
  font-size: 16px;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 4px;
}

.kp-desc {
  font-size: 13px;
  color: #64748b;
  line-height: 1.5;
}
</style>
