<template>
  <div
    v-if="show"
    class="modal w-full h-screen z-50 flex items-center overflow-y-auto justify-center"
  >
    <div
      class="modal-overlay absolute w-full h-screen bg-gray-900 opacity-80"
    ></div>
    <div
      class="modal-dialog md:max-w-xl relative w-full mx-5 mt-80 mb-5 sm:mt-0 pointer-events-none"
    >
      <div
        class="modal-content border-none shadow-lg relative flex flex-col w-full pointer-events-auto bg-white bg-clip-padding rounded-md outline-none text-current"
      >
        <div
          class="modal-header flex flex-shrink-0 items-center justify-between p-4 border-b border-gray-200 rounded-t-md"
        >
          <h5
            id="exampleModalLabel"
            class="text-xl font-medium uppercase leading-normal text-gray-800"
          >
            {{ title }}
          </h5>
          <button
            type="button"
            class="btn-close box-content w-4 h-4 p-1 text-black border-none rounded-none opacity-50 focus:shadow-none focus:outline-none focus:opacity-100 hover:text-black hover:opacity-75 hover:no-underline"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <h3 class="text-lg p-4 font-semibold">Technisch notwendige Cookies</h3>
        <div class="modal-body relative p-4">{{ content }}</div>
        <div class="flex px-4 pb-8 justify-between">
          <h3 class="text-lg font-semibold">Aktiv</h3>

          <label for="toggleB" class="flex items-center cursor-pointer">
            <div class="relative">
              <input
                id="toggleB"
                type="checkbox"
                class="sr-only"
                disabled
                checked
              />
              <div class="block bg-gray-600 w-14 h-8 rounded-full"></div>
              <div
                class="dot absolute left-1 top-1 bg-white w-6 h-6 rounded-full transition"
              ></div>
            </div>
          </label>
        </div>

        <div
          class="modal-footer flex flex-shrink-0 flex-wrap items-center justify-between p-4 border-t border-gray-200 rounded-b-md"
        >
          <div class="justify-start">
            <div>
              
              <router-link
                class="font-bold"
                to="/datenschutz"
                @click="checkTestMode()"
              >
                Datenschutz
              </router-link>
            </div>
          </div>

          <div class="justify-end">
            <button
              type="button"
              class="px-6 py-2.5 bg-secondary text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-secondaryAccent hover:shadow-lg focus:bg-purple-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-purple-800 active:shadow-lg transition duration-150 ease-in-out"
              @click.self="close_modal()"
            >
              Schließen
            </button>
            <button
              type="button"
              class="px-6 py-2.5 bg-primary text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-primaryAccent hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out ml-1"
              @click.self="confirm()"
            >
              Speichern
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BaseModal",

  props: {
    show: Boolean,
    title: {
      type: String,
      default: "",
    },
    content: {
      type: String,
      default: "",
    },
  },
  emits: ["close", "saveCookies"],

  data() {
    return {
      enabled: true,
    };
  },

  methods: {
    /**
     * Closes the modal and emits the event to the parent component
     *
     */
    close_modal() {
      this.$emit("close");
    },
    /**
     * Confirms the cookie decision and emits the saving state to the parent component
     *
     */
    confirm() {
      this.close_modal();
      this.$emit("saveCookies");
    },
  },
};
</script>

<style scoped>
input:checked ~ .dot {
  transform: translateX(100%);
  background-color: white;
}
</style>
