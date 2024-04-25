<!-- This example requires Tailwind CSS v2.0+ -->
<template>
  <div
    class="bg-white border-2 h-300 md:h-220 border-white rounded-lg"
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
          <p class="mt-4 text-lg whitespace-pre-line text-gray-500">
            {{ description }}
          </p>
        </div>
        <div class="w-full rounded-md shadow">
          <button
            v-if="choosingMode"
            class="w-full flex items-center justify-center px-8 border border-transparent text-base font-medium rounded-md text-white bg-primary hover:bg-primaryAccent py-2 md:text-lg md:px-10"
            @click="selectProfile()"
          >
            Auswählen und Weiter
          </button>
        </div>
        <div
          v-if="!choosingMode"
          class="flex flex-row justify-center items-center"
        >
          <div class="border-b-4 rounded-lg w-14 border-secondary mb-10"></div>
        </div>
        <div class="pt-10 pb-8 px-6">
          <h3
            class="text-lg font-medium divide-y divide-gray-200 text-gray-900 tracking-wide uppercase"
          >
            Tätigkeiten
          </h3>
          <p class="mt-4 text-lg text-left whitespace-pre-line text-gray-500">
            {{ tasks }}
          </p>
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
      default: 0,
    },
    id: {
      type: Number,
      default: 0,
    },
    choosingMode: {
      type: Boolean,
      default: false,
    },
  },
  emits: ["change"],

  methods: {
    /**
     * Selects the job profile and emits it to the parent component including the label of the selected job profile
     * Emits the label, job profile name and id.
     */
    selectProfile() {
      this.$emit("change", this.label, this.name, this.id);
    },
  },
};
</script>
