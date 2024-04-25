<!-- ToolTip.vue -->
<template>
  <transition name="fade">
    <div class="relative flex items-center">
      <div>
        <!-- Use a slot for the trigger element -->
        <slot name="trigger"></slot>
      </div>
      <div
        v-show="isVisible"
        class="absolute z-10 w-64 p-2 text-sm text-gray-700 bg-white border rounded shadow-lg"
        :class="{ '-top-10': isVisible, 'opacity-0': !isVisible }"
        @mouseenter="$emit('update-is-visible', true)"
        @mouseleave="$emit('update-is-visible', false)"
      >
        <!-- The tooltip content -->
        <slot></slot>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  props: {
    isVisible: Boolean,
  },
  emits: ["update-is-visible"],
};
</script>

<style scoped>
.fade-enter-from {
  opacity: 0;
}
.fade-enter-active {
  transition: all 2s ease;
}
</style>
