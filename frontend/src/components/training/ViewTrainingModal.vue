<template>
  <div
    class="fixed inset-0 z-50 flex items-center justify-center overflow-x-auto bg-black bg-opacity-50"
    @click="closeModal"
  >
    <div
      class="relative my-4 p-4 sm:mx-6 md:mx-10 lg:mx-20 bg-white rounded-lg shadow-lg w-full max-w-3xl"
      @click.stop
    >
      <!-- Header -->
      <div class="flex justify-between items-center border-b pb-3">
        <h3 class="text-xl font-semibold text-gray-900">
          {{ training.training_name }}
        </h3>
        <button
          class="text-gray-500 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center"
          aria-label="close"
          @click="closeModal"
        >
          <XMarkIcon class="h-6 w-6 text-gray-500"></XMarkIcon>
        </button>
      </div>
      <!-- Body -->
      <div class="my-5 text-sm md:text-md text-left text-gray-700">
        <div class="grid grid-cols-2 md:grid-cols-3">
          <!-- Provider -->
          <div class="md:col-span-2">
            <div class="mb-4">
              <h4 class="font-semibold mb-1">Anbieter:</h4>
              <p>{{ training.training_provider }}</p>
            </div>

            <!-- Costs -->
            <div class="mb-4">
              <h4 class="font-semibold mb-1">Kosten:</h4>
              <p>{{ training.costs_name }}</p>
            </div>

            <!-- Content with multiple values -->
            <div
              v-if="training.threat_event && training.threat_event.length"
              class="mb-4"
            >
              <h4 class="font-semibold mb-1">Agedeckte Inhalte:</h4>
              <ul class="list-disc pl-5">
                <li
                  v-for="(item, index) in training.threat_event"
                  :key="index"
                  class="mb-1"
                >
                  {{ item.event_name }}
                </li>
              </ul>
            </div>
            <div
              v-if="training.delivery_method && training.delivery_method.length"
              class="mb-4"
            >
              <h4 class="font-semibold mb-1">Vermittlungsmethoden:</h4>
              <ul class="list-disc pl-5">
                <li
                  v-for="(item, index) in training.delivery_method"
                  :key="index"
                  class="mb-1"
                >
                  {{ item.delivery_method }}
                </li>
              </ul>
            </div>
          </div>
          <div class="col-span-1">
            <div
              v-if="training.language && training.language.length"
              class="mb-4"
            >
              <h4 class="font-semibold mb-1">Verfügbare Sprachen</h4>
              <ul class="list-disc pl-5">
                <li
                  v-for="(item, index) in training.language"
                  :key="index"
                  class="mb-1"
                >
                  {{ item.language }}
                </li>
              </ul>
            </div>
            <div class="mb-4">
              <h4 class="font-semibold mb-1">Zertifizierung:</h4>
              <p>{{ training.certification }}</p>
            </div>
            <div
              v-if="
                training.competence_dimensions &&
                training.competence_dimensions.length
              "
              class="mb-4"
            >
              <h4 class="font-semibold mb-1">Kompetenzdimensionen</h4>
              <ul class="list-disc pl-5">
                <li
                  v-for="(item, index) in training.competence_dimensions"
                  :key="index"
                  class="mb-1"
                >
                  {{ item.dimension_name }}
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Footer -->
      <div class="border-t pt-3">
        <div class="flex justify-between">
          <button
            class="px-4 py-2 text-lg font-medium text-white bg-secondary rounded-md hover:bg-secondaryAccent focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-opacity-75"
            @click="closeModal"
          >
            Schließen
          </button>
          <button
            class="px-4 py-2 text-lg font-medium text-white bg-primary rounded-md hover:bg-primaryAccent focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-opacity-75"
            @click="followLink(training.training_url)"
          >
            Zum Angebot
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    training: {
      type: Object,
      default: null,
    },

  },
  emits: ["closeModal"],

  methods: {
    /**
     * Closes the modal
     */
    closeModal() {
      this.$emit("closeModal"); // Emit an event for the parent component
    },
    /**
     * Allows to follow the URL of a training program in a new window.
     * @param {string} link- The training URL
     */
    followLink(link) {
      window.open(link, "_blank");
    },
  },
};
</script>
