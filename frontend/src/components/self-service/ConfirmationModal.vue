<template>
  <div
    class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full flex items-center justify-center"
    @click="closeModal"
  >
    <div
      class="relative mx-auto p-5 border w-96 shadow-lg rounded-md bg-white"
      @click.stop
    >
      <div class="text-center">
        <!-- Header -->
        <div
          class="flex justify-between items-center border-b border-gray-200 p-3"
        >
          <h3 class="text-lg leading-6 font-medium text-gray-900">
            Entscheidung Bestätigen
          </h3>
          <button
            class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center"
            @click="closeModal"
          >
            <XMarkIcon class="h-6 w-6 text-gray-500"></XMarkIcon>
          </button>
        </div>
        <!-- Body -->
        <div class="mt-2 px-7 py-3">
          <p class="text-left">
            Möchten Sie wirklich mit dieser Entscheidung fortfahren? Sie kann
            nicht rückgängig gemacht werden!
          </p>
        </div>
        <!-- Footer -->
        <div class="border-t border-gray-200 px-4 py-3">
          <button
            class="px-4 py-2 bg-primary text-white text-base font-medium rounded-md w-full shadow-sm hover:bg-primaryAccent focus:outline-none focus:ring-2 focus:ring-blue-300"
            @click="confirm"
          >
            Ja
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  emits: ["close-modal", "save-decision"],
  data() {
    return {
      showModal: false,
    };
  },

  methods: {
    /**
     * Closes the modal and emits the event to the parent component
     */
    closeModal() {
      this.showModal = false;
      this.$emit("close-modal"); // Emit an event for the parent component
    },
    /**
     * Confirms the decision and emits the event to the parent component
     * Finally calls closeModal
     */
    confirm() {
      // Handle the confirmation action here
      this.$emit("save-decision"); // Emit an event for the parent component

      this.closeModal();
    },
  },
};
</script>
