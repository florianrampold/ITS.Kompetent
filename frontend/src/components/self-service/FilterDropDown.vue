<template>
  <div class="text-left font-semibold text-primary">
    <slot name="title" />
    <div class="relative w-full inline-block">
      <div>
        <button
          v-if="selectedOption"
          id="options-menu"
          type="button"
          class="inline-flex justify-center h-10 w-full rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none"
          aria-haspopup="true"
          aria-expanded="true"
          @click="toggleDropdown"
        >
          {{ selectedOption.text }}
          <ChevronDownIcon class="w-7 h-7 pb-2 text-gray-500"></ChevronDownIcon>
        </button>
      </div>
      <div
        class="origin-top-right cursor-pointer absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none"
        role="menu"
        aria-orientation="vertical"
        aria-labelledby="options-menu"
      >
        <div
          v-show="isDropdownOpen"
          class="origin-top-right absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none"
          role="menu"
          aria-orientation="vertical"
        >
          <div
            v-for="option in filterOptions"
            :key="option.id"
            class="py-1"
            role="none"
          >
            <a
              class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900"
              role="menuitem"
              @click="selectOption(option)"
              >{{ option.text }}</a
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    filterOptions: {
      type: Array,
      default: () => [],
    },
  },
  emits: ["changeOption"],

  data() {
    return {
      isDropdownOpen: false,
      selectedOption: "",
    };
  },
  /**
   * A Vue component lifecycle method that runs once the component is mounted to the DOM.
   * Initially set the selected option in the filter dropwdown to the first element.
   *
   */
  mounted() {
    this.selectedOption = this.filterOptions[0];
  },
  methods: {
    /**
     * Changes the open and closing state of the dropdown
     */
    toggleDropdown() {
      this.isDropdownOpen = !this.isDropdownOpen;
    },
    /**
     * Selects a new filter option and emits the event to the parent component
     * Finally toggles the dropdown state
     * @param {Object} option The new filter option
     */
    selectOption(option) {
      this.selectedOption = option;
      this.$emit("changeOption", option);
      this.toggleDropdown();
    },
  },
};
</script>
