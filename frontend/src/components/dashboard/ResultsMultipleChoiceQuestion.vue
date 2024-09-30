<template>
  <div
    class="w-full bg-white border-2 rounded-lg shadow-lg py-4 px-4"
    :class="{ 'border-red-700': selected }"
  >
    <div class="flex justify-between items-start">
      <slot name="questionTag"></slot>
    </div>
    <p
      class="flex justify-start mt-3 mb-5 text-primary sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0 text-left"
    >
      <slot name="questionContent"></slot>
    </p>

    <div class="answers rounded-lg">
      <label
        v-for="(val, key) in options"
        :key="key"
        :class="getClassForRating(val.answer_rating, val.id)"
        class="flex text-sm md:text-lg border-2 items-center text-left justify-between rounded-lg p-4 my-4 cursor-pointer"
      >
        <input
          :id="val.id"
          :value="val.option"
          class="hidden"
          :checked="key in value"
          type="checkbox"
          label="Option 1"
        />
        <span class="pl-4 pr-4 w-4/5">{{ val.option }}</span>
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
      default: () => {},
    },
    selected: {
      type: Boolean,
      default: false,
    },
    correctMultipleChoiceQuestion: {
      type: Boolean,
      default: false,
    },
  },

  mounted() {
    console.log(this.correctMultipleChoiceQuestion, "corr");
  },

  methods: {
    /**
     * Checks if the id of the answer option is incuded in the user answer
     * Used to apply css to the wrapper of the answer option --> selected blue color
     * @return {Boolean} True if included, false else.
     */
    isIncluded(id) {
      return this.value.userAnswer.includes(id);
    },
    getClassForRating(rating, id) {
      if (this.correctMultipleChoiceQuestion) {

        switch (rating) {
          case 0:
            return "border-red-500 bg-red-100";
          case 2:
            return "border-green-500 bg-green-100";
          case 1:
            return "border-yellow-500 bg-yellow-100";
          default:
            return "";
        }
      } else {
        if (this.isIncluded(id)) {
          switch (rating) {
            case 0:
              return "border-red-500 bg-red-100";
            case 2:
              return "border-green-500 bg-green-100";
            case 1:
              return "border-yellow-500 bg-yellow-100";
            default:
              return "";
          }
        }
      }
    },
  },
};
</script>
