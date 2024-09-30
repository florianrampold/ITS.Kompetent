<template>
  <div
    class="bg-white border-2 w-full md:w-3/4 lg:w-1/2 h-150 lg:h-200 border-gray-200 rounded-lg"
    :class="{ 'border-primary': value == label }"
  >
    <div class="mx-auto px-4 sm:px-6 lg:px-8">
      <div
        class="mt-8 space-y-4 sm:space-y-0 lg:max-w-4xl lg:mx-auto xl:max-w-none xl:mx-0 xl:grid-cols-2"
      >
        <div class="p-6">
          <h2 class="text-xl leading-6 font-medium text-gray-900">
            {{ name }}
          </h2>
          <div class="lg:h-128">
            <p class="mt-4 text-lg whitespace-pre-line text-gray-500">
              {{ description }}
            </p>
            <form
              v-if="label == 2"
              class="bg-white px-8 pt-6 pb-4 mb-2 w-full"
              @submit.prevent="submitForm"
            >
              <div class="">
                <label
                  class="block text-gray-700 text-sm font-bold mb-2"
                  for="champagneName"
                >
                  Ihr Einladungs-Code
                </label>
                <input
                  v-model="internalValue"
                  class="appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  type="text"
                  placeholder="Einladungs-Code"
                  required
                />
              </div>
            </form>
          </div>
        </div>

        <div class="w-full rounded-md shadow">
          <button
            class="w-full flex bg-primary hover:bg-primaryAccent items-center justify-center px-8 border border-transparent text-base font-medium rounded-md text-white py-2 md:text-lg md:px-10"
            @click="selectTestMode()"
          >
            Auswählen und Weiter
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    name: {
      type: String,
      default: "",
    },
    description: {
      type: String,
      default: "",
    },
    tasks: {
      type: String,
      default: "",
    },
    label: {
      type: Number,
      default: 0,
    },
    value: {
      type: Number,
      default: 2,
    },
    id: {
      type: Number,
      default: 0,
    },
    invitationToken: {
      type: Number,
      default: null,
    },
  },
  emits: ["change", "input"],

  computed: {
    /**
     * A computed property that watches the input invitation token by the user.
     * Emits the new value to the parent component.
     * @return {string} Returns the invitation token.
     *
     */
    internalValue: {
      get() {
        // Get the value from the parent prop
        return this.invitationToken;
      },
      set(newValue) {
        // Emit an input event with the new value to update the parent
        this.$emit("input", newValue);
      },
    },
  },
  methods: {
    /**
     * Selects the testmode and emits it to the parent component including the label of the selected testmode.
     *
     *
     */
    selectTestMode() {
      this.$emit("change", this.label);
    },
  },
};
</script>
