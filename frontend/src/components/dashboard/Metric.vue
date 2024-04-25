<template>
  <div class="p-5 bg-white rounded-lg border shadow-md">
    <div class="font-semibold text-primary">{{ metric }}</div>
    <div class="flex justify-center items-center pt-1">
      <div class="text-2xl font-bold text-gray-900">{{ score }}</div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    metric: {
      type: String,
      default: "",
    },
    score: {
      type: Number,
      default: 0,
    },
  },
};
</script>
