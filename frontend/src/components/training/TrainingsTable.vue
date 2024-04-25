<template>
  <div class="overflow-x-auto">
    <table
      class="rounded-lg w-full text-xs md:text-sm xl:text-lg text-left px-4 bg-white"
    >
      <thead
        class="border-b pl-6 bg-primary rounded-lg text-white uppercase h-20"
      >
        <tr class="h-24">
          <th class="pl-2 w-1/12">Trainings-Gruppe</th>
          <th class="px-2 w-3/12">SETA Programm</th>
          <th class="px-2 w-2/12">Anbieter</th>
          <th class="px-2 w-2/12">Methode</th>
          <th class="px-2 w-3/12">Kompetenzdimensionen</th>
          <th class="px-2 w-1/12">Rang</th>
        </tr>
      </thead>
      <tbody v-if="trainings">
        <tr
          v-for="(resource, index) in trainings"
          :key="resource.id"
          class="h-24 hover:bg-gray-300 cursor-pointer border-b break-words"
          @click="openTrainingModal(resource)"
        >
          <td class="max-w-xs px-4 break-words">
            {{ resource.training_group.identifier }}
          </td>
          <td class="max-w-xs px-4 break-words">
            {{ resource.training_name }}
          </td>
          <td class="px-2 whitespace-normal">
            {{ resource.training_provider }}
          </td>
          <td class="px-2">
            <span
              v-for="method in trainings[index].delivery_method"
              :key="method.id"
              class="flex flex-col my-2"
            >
              {{ method.delivery_method }}
            </span>
          </td>
          <td class="px-2">
            <span
              v-for="dimension in trainings[index].competence_dimensions"
              :key="dimension.id"
              class="flex flex-col my-2"
            >
              {{ dimension.dimension_name }}
            </span>
          </td>
          <td class="max-w-xs px-4 break-words">
            {{ resource.rank }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <div v-if="totalPages > 1" class="mt-10">
    <trainings-pagination
      :total-pages="totalPages"
      :total="trainings.length"
      :total-trainings="totalTrainings"
      :per-page="perPage"
      :current-page="currentPage"
      :has-more-pages="hasMorePages"
      @pagechanged="showMore"
    ></trainings-pagination>
  </div>
  <Teleport to="body">
    <div v-if="modalVisible">
      <view-training-modal
        :training="selectedTraining"
        @closeModal="closeTrainingModal()"
      ></view-training-modal>
    </div>
  </Teleport>
</template>

<script>
import TrainingsPagination from "@/components/training/TrainingPagination.vue";
import ViewTrainingModal from "@/components/training/ViewTrainingModal.vue";

export default {
  components: {
    TrainingsPagination,
    ViewTrainingModal,
  },
  props: {
    columns: {
      type: Array,
      default: null,
    },
    perPage: {
      type: Number,
      default: 0,
    },
    currentPage: {
      type: Number,
      default: 0,
    },
    totalPages: {
      type: Number,
      default: 0,
    },
    trainings: {
      type: Object,
      default: null,
    },
    totalTrainings: {
      type: Number,
      default: 0,
    },
  },
  emits: ["reFilterTraining", "closeModal"],
  data: function () {
    return {
      page: 1,
      hasMorePages: true,
      modalVisible: false,
      selectedTraining: null,
    };
  },

  methods: {
    /**
     * Sets the current page to the specified page number and emits an event to re-filter trainings.
     * @param {Number} page - The page number to navigate to and emit for refiltering.
     */
    showMore(page) {
      this.page = page;
      this.$emit("reFilterTraining", page);
    },

    /**
     * Opens a modal window for a specific training. It sets the selected training data and makes the modal visible.
     * @param {Object} training - The training data object that will be displayed in the modal.
     */
    openTrainingModal(training) {
      this.selectedTraining = training;
      this.modalVisible = true;
    },

    /**
     * Closes the training modal and emits an event indicating that the modal has been closed.
     * This could be used to trigger clean-up actions or updates in other parts of the application.
     */
    closeTrainingModal() {
      this.modalVisible = false;
      this.$emit("closeModal");
    },
  },
};
</script>
