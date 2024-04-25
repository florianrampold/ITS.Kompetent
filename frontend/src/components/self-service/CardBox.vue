<template>
  <div class="bg-white rounded shadow p-4">
    <div class="flex items-center justify-center">
      <h2 class="text-lg text-center font-semibold">{{ header }}</h2>
    </div>
    <div class="mt-4 flex justify-center">
      <p class="text-3xl mr-4 font-bold">{{ number }}</p>
      <span class="text-gray-600">
        <slot name="icon"></slot>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    header: {
      type: String,
      required: true,
    },
    number: {
      type: Number,
      required: true,
    },
  },
};
</script>
