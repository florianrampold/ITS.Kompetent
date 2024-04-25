<template>
  <div
    class="w-full sm:w-3/4 2xl:w-1/2 bg-white rounded-lg shadow-lg py-4 px-4"
  >
    <div class="flex justify-between items-start">
      <slot name="questionTag"></slot>
      <!-- <h2 class="font-bold">Sortier-Frage</h2> -->
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
      <draggable v-model="list" item-key="id" @change="changeOrderOfOptions">
        <template #item="{ element }">
          <div
            class="flex border-2 items-center text-sm md:text-lg justify-start text-left rounded-lg p-4 my-4 cursor-move"
          >
            {{ element.option }}
          </div>
        </template>
      </draggable>
    </div>
  </div>
</template>

<script>
import draggable from "vuedraggable";

export default {
  components: {
    draggable,
  },
  props: {
    options: {
      type: Array,
      default: null,
    },
  },
  emits: ["change"],
  data() {
    return {
      list: this.options,
    };
  },

  methods: {
    /**
     * Checks if the user changed the order of the answer options by dragging.
     * Emits the changed list of answer options.
     * .
     */
    changeOrderOfOptions() {
      this.$emit("change", this.list);
    },
  },
};
</script>
