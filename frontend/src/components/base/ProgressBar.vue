<template>
  <div
    class="w-full sm:w-3/4 2xl:w-3/5 bg-gray-200 h-4 relative overflow-hidden"
    :class="[{ 'rounded-full': rounded }, { indeterminate: indeterminate }]"
  >
    <div
      class="h-full progressbar"
      :class="[
        'bg-primary',
        { 'absolute top-0': indeterminate },
        { 'rounded-full': rounded },
      ]"
      role="progressbar"
      :style="{ width: `${percentage}%` }"
      :aria-valuenow="percentage"
      aria-valuemin="0"
      aria-valuemax="100"
    >
      <span class="flex items-center h-full">
        <slot></slot>
      </span>
    </div>
  </div>
</template>
<script>
export default {
  inheritAttrs: false,
  props: {
    color: {
      type: String,
      default: "gray",
    },
    percentage: {
      type: Number,
      default: 0,
    },
    rounded: {
      type: Boolean,
      default: true,
    },
    indeterminate: Boolean,
  },
};
</script>
<style scoped>
@keyframes progress-indeterminate {
  0% {
    width: 30%;
    left: -40%;
  }
  60% {
    left: 100%;
    width: 100%;
  }
  to {
    left: 100%;
    width: 0;
  }
}
.progressbar {
  transition: width 0.25s ease;
}
.indeterminate .progressbar {
  animation: progress-indeterminate 1.4s ease infinite;
}
</style>
