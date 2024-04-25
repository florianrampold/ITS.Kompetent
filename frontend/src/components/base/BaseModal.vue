<template>
  <div
    v-if="show"
    class="modal fixed w-full h-full top-0 left-0 z-50 flex items-center justify-center"
  >
    <div
      class="modal-overlay absolute w-full h-full bg-gray-900 opacity-80"
      @click.self="close_modal()"
    ></div>
    <div class="modal-dialog relative w-auto pointer-events-none">
      <div
        class="modal-content border-none shadow-lg relative flex flex-col w-full pointer-events-auto bg-white bg-clip-padding rounded-md outline-none text-current"
      >
        <div
          class="modal-header flex flex-shrink-0 items-center justify-between p-4 border-b border-gray-200 rounded-t-md"
        >
          <h5
            id="exampleModalLabel"
            class="text-xl font-medium leading-normal text-gray-800"
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
        <div class="modal-body relative p-4">{{ content }}</div>
        <div
          class="modal-footer flex flex-shrink-0 flex-wrap items-center justify-end p-4 border-t border-gray-200 rounded-b-md"
        >
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
            Fortfahren
          </button>
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
  emits: ["close", "confirm"],

  data() {
    return {
      firstname: "",
      lastname: "",
      gender: "",
      residence: "",
    };
  },

  methods: {
    /**
     * Closes the modal and emits the closing event to the parent component
     *
     */
    close_modal() {
      this.$emit("close");
    },
    /**
     * Confirms the decision and closes the modal and emits the confirmation event to the parent component
     *
     */
    confirm() {
      this.close_modal();
      this.$emit("confirm");
    },
  },
};
</script>
