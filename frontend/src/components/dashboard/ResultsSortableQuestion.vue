<template>
  <div class="w-full bg-white rounded-lg shadow-lg py-4 px-4">
    <div class="flex justify-between items-start">
      <slot name="questionTag"></slot>
    </div>
    <p
      class="flex justify-start mt-3 mb-5 text-primary text-left sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
    >
      <slot name="questionContent"></slot>
    </p>
    <h2 class="flex justify-start font-semibold">
      Bitte sortieren Sie die Antwortmöglichkeiten nach Richtigkeit:
    </h2>

    <div class="answers rounded-lg">
      <div v-for="element in sortedItems" :key="element.id">
        <div
          :class="getClassForRating(element.answer_rating)"
          class="flex border-2 items-center text-sm md:text-lg justify-start text-left rounded-lg p-4 my-4"
        >
          {{ element.option }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    correctAnswer: {
      type: Boolean,
      default: false,
    },
    options: {
      type: Array,
      default: null,
    },
    userAnswer: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      list: this.options,
    };
  },
  computed: {
    /**
    * A computed property that returns the sorted answer options by correctness.
    *
    * 
    */
    sortedItems() {
      if (this.correctAnswer) {
        return this.options
          .slice()
          .sort((a, b) => b.answer_rating - a.answer_rating);
      } else {
        return this.options.slice().sort((a, b) => {
          return this.userAnswer.indexOf(a.id) - this.userAnswer.indexOf(b.id);
        });
      }
    },
  },

  methods: {
    /**
     * Applies the class to the user answer depending on the answer rating
     *
     * .
     */
    getClassForRating(rating) {
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
    },
  },
};
</script>
