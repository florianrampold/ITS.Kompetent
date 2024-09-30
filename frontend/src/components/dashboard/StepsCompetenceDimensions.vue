<template>
  <section>
    <div class="relative flex justify-center items-center">
      <div
        class="absolute w-full flex justify-between items-center"
        style="top: 50%; transform: translateY(-50%); z-index: 0"
      ></div>

      <div class="flex-1 text-center relative">
        <div class="relative mb-2 z-10">
          <div
            :class="
              activestate == '0'
                ? 'bg-green-500 border-2 border-action'
                : 'bg-gray-400'
            "
            class="w-10 h-10 mx-auto rounded-full text-lg text-white flex items-center justify-center"
          >
            <span class="font-bold">1</span>
          </div>
        </div>
      </div>

      <div class="flex-1 text-center relative">
        <div class="relative mb-2 z-10">
          <div
            :class="activestate == '1' ? 'bg-action' : 'bg-gray-400'"
            class="w-10 h-10 mx-auto rounded-full text-lg text-white flex items-center justify-center"
          >
            <span class="font-bold">2</span>
          </div>
        </div>
      </div>

      <div class="flex-1 text-center relative">
        <div class="relative mb-2 z-10">
          <div
            :class="activestate == '2' ? 'bg-action' : 'bg-gray-400'"
            class="w-10 h-10 mx-auto rounded-full text-lg text-white flex items-center justify-center"
          >
            <span class="font-bold">3</span>
          </div>
        </div>
      </div>

      <div class="flex-1 text-center relative">
        <div class="relative mb-2 z-10">
          <div
            :class="activestate == '3' ? 'bg-action' : 'bg-gray-400'"
            class="w-10 h-10 mx-auto rounded-full text-lg text-white flex items-center justify-center"
          >
            <span class="font-bold">4</span>
          </div>
        </div>
      </div>
      <div class="flex-1 text-center relative">
        <div class="relative mb-2 z-10">
          <div
            :class="activestate == '4' ? 'bg-action' : 'bg-gray-400'"
            class="w-10 h-10 mx-auto rounded-full text-lg text-white flex items-center justify-center"
          >
            <span class="font-bold">5</span>
          </div>
        </div>
      </div>
      <div class="flex-1 text-center relative">
        <div class="relative mb-2 z-10">
          <div
            :class="activestate == '5' ? 'bg-action' : 'bg-gray-400'"
            class="w-10 h-10 mx-auto rounded-full text-lg text-white flex items-center justify-center"
          >
            <span class="font-bold">6</span>
          </div>
        </div>
      </div>
      <div class="flex-1 text-center relative">
        <div class="relative mb-2 z-10">
          <div
            :class="activestate == '6' ? 'bg-action' : 'bg-gray-400'"
            class="w-10 h-10 mx-auto rounded-full text-lg text-white flex items-center justify-center"
          >
            <span class="font-bold">7</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  props: {
    linecolor: {
      type: String,
      default: "gray",
    },
    activestate: {
      type: Number,
      default: 0,
    },
  },
};
</script>
