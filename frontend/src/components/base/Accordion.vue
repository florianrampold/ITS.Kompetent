<template>
  <div
    class="flex flex-col bg-white rounded-md shadow-md border"
    :class="{ 'text-primary': isOpen }"
  >
    <button
      class="h-24 flex font-semibold text-lg items-center justify-between p-5"
      :aria-expanded="isOpen"
      @click="toggleAccordion()"
    >
      <slot name="title" />
      <ChevronDownIcon class="h-6 w-6"></ChevronDownIcon>
    </button>
    <div v-show="isOpen" class="border-t text-left p-4 h-64">
      <transition appear name="fade">
        <slot name="content" />
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isOpen: false,
    };
  },

  methods: {
    /**
     * Toggles the accordion state and changes it from closed to open and the other way around.
     *
     */
    toggleAccordion() {
      this.isOpen = !this.isOpen;
    },
  },
};
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: height 0.3s ease-in-out;
  overflow: hidden;
}
.fade-enter-from,
.fade-leave-to {
  height: 0px !important;
}
</style>
