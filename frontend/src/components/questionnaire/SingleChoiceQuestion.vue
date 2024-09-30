<template>
  <div
    class="w-full sm:w-3/4 2xl:w-1/2 bg-white border-2 border-white rounded-lg shadow-xl py-4 px-4"
    :class="{ 'border-red-700': selected }"
  >
    <div class="flex justify-between items-start">
      <slot name="questionTag"></slot>
    </div>
    <p
      class="flex justify-start mt-3 mb-5 text-left text-primary sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
    >
      <slot name="questionContent"></slot>
    </p>
    <h2 class="flex justify-start font-semibold">
      Bitte nur eine Antwort angeben:
    </h2>

    <div class="answers rounded-lg">
      <label
        v-for="val in options"
        :key="val"
        :class="{ 'border-primary bg-blue-100': isIncluded(val.id) }"
        class="flex text-sm md:text-lg text-left border-2 items-center justify-between rounded-lg p-4 my-4 cursor-pointer"
      >
        <input
          :id="val.id"
          :value="val.option"
          class="hidden"
          :checked="val.id == value.userAnswer"
          type="radio"
          label="Option 1"
          @change="$emit('change', val.id, val.answer_rating)"
        />
        <span class="px-4">{{ val.option }}</span>
        <div v-if="isIncluded(val.id)" class="flex-shrink-0 text-white">
          <CheckCircleIcon class="w-6 h-6 text-primary"></CheckCircleIcon>
        </div>
      </label>
    </div>
    <div v-if="selected">
      <h2 class="text-red-700">Bitte geben Sie eine Antwort an</h2>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    options: {
      type: Array,
      default: null,
    },
    value: {
      type: Object,
      default: null,
    },
    selected: {
      type: Boolean,
      default: false,
    },
  },
  emits: ["change"],
  methods: {
    /**
     * Checks if the id of the answer option is incuded in the user answer
     * Used to apply css to the wrapper of the answer option --> selected blue color
     * @return {Boolean} True if included, false else.
     */
    isIncluded(id) {
      return this.value.userAnswer == id;
    },
  },
};
</script>
