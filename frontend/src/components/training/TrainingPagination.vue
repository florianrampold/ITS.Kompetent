<template>
  <div class="flex flex-col xl:flex-row xl:justify-between">
    <div class="font-semibold pt-2">
      Zeigt Trainingsangebote {{ trainingsRangeMin }} bis
      {{ trainingsRangeMax }} von {{ totalTrainings }} Trainingsangeboten
    </div>
    <ul class="pagination p-2 shadow-sm bg-white rounded-lg">
      <li class="pagination-item">
        <span
          v-if="isInFirstPage"
          class="rounded-l rounded-sm border px-3 py-2 cursor-not-allowed no-underline text-gray-600 h-10"
          >&laquo;</span
        >
        <a
          v-else
          class="rounded-l rounded-sm border-t border-b border-l border-gray-100 px-3 py-2 text-gray-600 hover:bg-gray-100 no-underline"
          href="#"
          role="button"
          rel="prev"
          @click.prevent="onClickFirstPage"
        >
          &laquo;
        </a>
      </li>

      <li class="pagination-item">
        <button
          type="button"
          :disabled="isInFirstPage"
          aria-label="Go to previous page"
          class="rounded-sm border bg-primary border-gray-100 px-3 py-2 hover:bg-primaryAccent text-white no-underline mx-2 text-sm"
          :class="{ 'cursor-not-allowed': isInFirstPage }"
          @click="onClickPreviousPage"
        >
          Vorherige
        </button>
      </li>

      <li v-for="page in pages" :key="page.name" class="pagination-item">
        <span
          v-if="isPageActive(page.name)"
          class="rounded-sm border border-blue-100 px-3 py-2 bg-blue-100 no-underline text-blue-500 cursor-not-allowed mx-2"
          >{{ page.name }}</span
        >
        <a
          v-else
          class="rounded-sm border border-gray-100 px-3 py-2 hover:bg-gray-100 text-gray-600 no-underline mx-2"
          href="#"
          role="button"
          @click.prevent="onClickPage(page.name)"
          >{{ page.name }}</a
        >
      </li>

      <li class="pagination-item">
        <button
          type="button"
          :disabled="isInLastPage"
          aria-label="Go to next page"
          class="rounded-sm border bg-primary border-gray-100 px-3 py-2 hover:bg-primaryAccent text-white no-underline mx-2 text-sm"
          :class="{ 'cursor-not-allowed': isInLastPage }"
          @click="onClickNextPage"
        >
          Nächste
        </button>
      </li>

      <li class="pagination-item">
        <a
          v-if="!isInLastPage"
          class="rounded-r rounded-sm border border-gray-100 px-3 py-2 hover:bg-gray-100 text-gray-600 no-underline"
          href="#"
          rel="next"
          role="button"
          @click.prevent="onClickLastPage"
          >&raquo;</a
        >
        <span
          v-else
          class="rounded-r rounded-sm border border-gray-100 px-3 py-2 hover:bg-gray-100 text-gray-600 no-underline cursor-not-allowed"
          >&raquo;</span
        >
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    maxVisibleButtons: {
      type: Number,
      required: false,
      default: 5,
    },

    totalPages: {
      type: Number,
      required: true,
    },

    total: {
      type: Number,
      required: true,
    },

    perPage: {
      type: Number,
      required: true,
    },

    currentPage: {
      type: Number,
      required: true,
    },

    hasMorePages: {
      type: Boolean,
      required: true,
    },
    totalTrainings: {
      type: Number,
      default: 0,
    },
  },

  emits: ["pagechanged", "refetch"],
  data: function () {
    return {
      showNextButton: false,
      showPrevButton: false,
    };
  },
  computed: {
    /**
     * Calculates the starting page number for pagination.
     * - If the current page is the first page, it returns 1.
     * - If the current page is the last page, it decrements and returns the current page number.
     * - Otherwise, it simply returns the current page number.
     * @returns {Number} The start page number based on the current page context.
     */
    startPage() {
      if (this.currentPage === 1) {
        return 1;
      }

      if (this.currentPage === this.totalPages) {
        return this.currentPage - 1;
      }

      return this.currentPage;
    },

    /**
     * Calculates the minimum range number for displaying training items on a page.
     * @returns {Number} The first training item number on the current page.
     */
    trainingsRangeMin() {
      return this.currentPage * this.perPage - (this.perPage - 1);
    },

    /**
     * Calculates the maximum range number for displaying training items on a page.
     * If on the last page, it adjusts to return the total count of items, otherwise the max item of the current page.
     * @returns {Number} The last training item number on the current page or total items if the last page.
     */
    trainingsRangeMax() {
      return this.isInLastPage
        ? (this.currentPage - 1) * this.perPage + this.total
        : this.currentPage * this.perPage;
    },

    /**
     * Determines the last page number visible in the pagination controls.
     * Ensures it does not exceed the total pages available.
     * @returns {Number} The end page number for pagination, considering the maximum visible buttons.
     */
    endPage() {
      return Math.min(
        this.startPage + this.maxVisibleButtons - 1,
        this.totalPages
      );
    },

    /**
     * Generates an array of pages for pagination, marking the current page as disabled.
     * @returns {Array} An array of objects representing pages, where each object contains the page number and its disabled status.
     */
    pages() {
      const range = [];

      for (let i = this.startPage; i <= this.endPage; i += 1) {
        range.push({
          name: i,
          isDisabled: i === this.currentPage,
        });
      }

      return range;
    },

    /**
     * Checks if the current page is the first page.
     * @returns {Boolean} True if the current page is the first page, otherwise false.
     */
    isInFirstPage() {
      return this.currentPage === 1;
    },

    /**
     * Checks if the current page is the last page.
     * @returns {Boolean} True if the current page is the last page, otherwise false.
     */
    isInLastPage() {
      return this.currentPage === this.totalPages;
    },
  },

  methods: {
    /**
     * Emits page number 1 initially
     */
    onClickFirstPage() {
      this.$emit("pagechanged", 1);
    },
    /**
     * Emits page number -1 if the user wants to navigate to previous page
     */
    onClickPreviousPage() {
      this.$emit("pagechanged", this.currentPage - 1);
    },
    /**
     * Emits page number if the user clicks on a specifc page
     */
    onClickPage(page) {
      this.$emit("pagechanged", page);
    },
    /**
     * Emits page number -+1 if the user wants to navigate to previous page
     */
    onClickNextPage() {
      this.$emit("pagechanged", this.currentPage + 1);
    },
    /**
     * Emits page number = totalPages if the user wants to navigate to the last page
     */
    onClickLastPage() {
      this.$emit("pagechanged", this.totalPages);
    },
    /**
     * Checks wheter the pae is active
     * @param {Number} page The  page
     * @return {Boolean} Check wheter the current page is the page in the params, returns true if yes, false otherwise.
     */
    isPageActive(page) {
      return this.currentPage === page;
    },
  },
};
</script>

<style scoped>
.pagination {
  list-style-type: none;
}

.pagination-item {
  display: inline-block;
}
</style>
