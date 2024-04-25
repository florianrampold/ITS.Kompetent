<template>
  <Teleport to="body">
    <Transition name="toast" appear>
      <div
        v-if="active"
        class="fixed z-50 block w-full max-w-xs rounded-lg shadow-lg"
        role="alert"
        :class="classList"
      >
        <div
          class="flex justify-between items-center py-2 px-3 bg-clip-padding border-b rounded-t-lg"
        >
          <p class="font-bold text-white flex items-center">
            <CheckIcon v-if="type === 'success'" class="h-6 w-6 text-white" />
            <ExclamationTriangleIcon
              v-else-if="type === 'warning'"
              class="h-6 w-6 text-white"
            />
            <XCircleIcon
              v-else-if="type === 'danger'"
              class="h-6 w-6 text-white"
            />
            {{ title }}
          </p>
          <div class="flex items-center">
            <XCircleIcon
              class="h-6 w-6 text-white hover:text-gray-100"
              @click="closePopUp()"
            />
          </div>
        </div>
        <div class="p-3 rounded-b-lg break-words text-white">
          {{ content }}
        </div>
      </div>
    </Transition>
  </Teleport>
</template>

<script>
export default {
  props: {
    type: {
      type: String,
      default: "default", // success, warning, danger
    },
    title: {
      type: String,
      default: "",
    },
    content: {
      type: String,
      default: "",
    },
    position: {
      type: String,
      default: "top-right", // top-right, top-left, bottom-right, bottom-left
    },
    timeout: {
      type: Number,
      default: 5000,
    },
  },
  emits: ["popup-closed"],
  data() {
    return {
      active: true,
      componentTimeout: 0,
    };
  },
  computed: {
    /**
     * Computed property that changes positioning and color of the PopUp based on specified properties in the parent component.
     * Sets the test button to inactive.
     *
     */
    classList() {
      return {
        //position
        "top-64": this.position === "top-right" || this.position === "top-left",
        "bottom-5":
          this.position === "bottom-right" || this.position === "bottom-left",
        "left-5":
          this.position === "top-left" || this.position === "bottom-left",
        "right-5":
          this.position === "top-right" || this.position === "bottom-right",
        //type
        "bg-primary": this.type === "default",
        "bg-green-500": this.type === "success",
        "bg-yellow-500": this.type === "warning",
        "bg-red-500": this.type === "danger",
      };
    },
  },
  /**
   * Mounted lifecycle method. When PopUp mounts a timeout is set to close it after defined timeframe.
   * Sets the test button to inactive.
   *
   */
  mounted() {
    this.componentTimeout = setTimeout(() => this.closePopUp(), this.timeout);
  },
  methods: {
    /**
     * Closes the PopUp
     *
     */
    closePopUp() {
      this.active = false;
      setTimeout(() => this.$emit("popup-closed"), 500);
      clearTimeout(this.componentTimeout);
    },
  },
};
</script>

<style>
.toast-enter-from,
.toast-leave-to {
  opacity: 0;
  transform: translateY(-60px);
}
.toast-enter-active,
.toast-leave-active {
  transition: all 0.5s ease;
}
</style>
