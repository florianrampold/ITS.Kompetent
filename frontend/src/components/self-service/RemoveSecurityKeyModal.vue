<template>
  <div
    class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full flex items-center justify-center"
    @click="closeModal"
  >
    <div
      class="relative mx-auto p-5 border w-1/2 shadow-lg rounded-md bg-white"
      style="max-height: calc(100vh - 4rem); overflow-y: auto"
      @click.stop
    >
      <div class="text-center">
        <!-- Header -->
        <div
          class="flex justify-between items-center border-b border-gray-200 p-3"
        >
          <h3 class="text-lg leading-6 font-medium text-gray-900">
            Sicherheits-Code vergessen
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
            Wenn Sie den Sicherheits-Code vergessen haben, können Sie die
            Nutzung des Sicherheits-Codes deaktivieren. Sollten Sie sich hierfür
            entscheiden haben Sie keinen Zugriff auf die E-Mail-Adressen im
            Klartext. <br />
            <br />
            <strong
              >Das heißt Sie müssen die Verteilung der Einladungs-Codes zu
              Teilnehmenden eigenständig nachverfolgen und vornehmen.
            </strong>
            <br />
            <br />
            Zu Anfang haben wir Ihnen einmalig eine Text-Datei bereitgestellt,
            die den Sicherheits-Code beinhaltet. Bevor Sie sich dazu entscheiden
            die Verwendung des Sicherheits-Codes zu deaktivieren, schauen Sie
            nach einer lokalen Text-Datei mit der Bezeichnung
            <strong>key.txt</strong>.
          </p>
        </div>
        <!-- Footer -->
        <div class="border-t flex justify-center border-gray-200 px-4 py-3">
          <button
            class="px-4 py-2 bg-secondary text-white text-base font-medium rounded-md w-64 shadow-sm hover:bg-secondaryAccent focus:outline-none focus:ring-2 focus:ring-blue-300"
            @click="confirm"
          >
            Sicherheits-Code zurücksetzen
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  emits: ["close-modal", "remove-security-key"],
  data() {
    return {
      showModal: false,
    };
  },

  methods: {
    /**
     * Closes the modal.
     */
    closeModal() {
      this.showModal = false;
      this.$emit("close-modal"); // Emit an closing event for the parent component
    },
    /**
     * Confirs the decision to remove the security key and emits the event to the parent component.
     */
    confirm() {
      this.$emit("remove-security-key"); // Emit an event for the parent component

      this.closeModal();
    },
  },
};
</script>
