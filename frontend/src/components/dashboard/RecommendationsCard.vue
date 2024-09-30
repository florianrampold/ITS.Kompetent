<template>
  <div class="bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div
        class="space-y-4 sm:space-y-0 sm:grid sm:grid-cols-1 sm:gap-6 lg:max-w-4xl lg:mx-auto xl:max-w-none xl:mx-0 xl:grid-cols-2"
      >
        <div
          v-for="threat in competenceTestResult.test_situations"
          :key="threat"
          class="border-2 rounded-lg shadow-lg divide-y divide-gray-200"
          :class="{
            'border-green-500':
              Math.round((threat.pointsScored / 14) * 100) >= 65,
            'border-red-500': Math.round((threat.pointsScored / 14) * 100) < 65,
          }"
        >
          <div class="p-6">
            <h2 class="text-lg leading-6 font-medium text-gray-900">
              {{ threat.threat_vector.threatVectorText }}
            </h2>
            <p class="mt-4 text-sm text-gray-500">
              {{ threat.threat_vector.threat_event.event_description }}
            </p>
            <p class="mt-8">
              <span class="text-4xl font-extrabold text-gray-900"
                >{{ Math.round((threat.pointsScored / 14) * 100) }}%</span
              >
              {{ " " }}
            </p>
          </div>
          <div class="pt-6 pb-8 px-6">
            <h3
              class="text-lg font-medium divide-y divide-gray-200 text-gray-900 tracking-wide uppercase"
            >
              Kompetenzdimension
            </h3>
            <ul role="list" class="mt-6 space-y-4">
              <li
                v-for="(feature, index) in threat.threat_vector.test_items"
                :key="index"
                class="flex space-x-3"
              >
                <CheckIcon
                  v-if="feature.question_item[0].points == 2"
                  class="flex-shrink-0 h-5 w-5 text-green-500"
                  aria-hidden="true"
                />
                <ExclamationTriangleIcon
                  v-if="feature.question_item[0].points == 1"
                  class="flex-shrink-0 h-5 w-5 text-yellow-500"
                  aria-hidden="true"
                />
                <XMarkIcon
                  v-if="feature.question_item[0].points == 0"
                  class="flex-shrink-0 h-5 w-5 text-red-500"
                  aria-hidden="true"
                />
                <span class="text-sm text-gray-500">{{
                  feature.competence_dimension.dimension_name
                }}</span>
              </li>
            </ul>
          </div>
          <div class="p-4">
            <h2
              class="text-lg font-medium divide-y divide-gray-200 text-gray-900 pb-6 tracking-wide uppercase"
            >
              Empfehlung
            </h2>
            <div
              v-if="Math.round((threat.pointsScored / 14) * 100) > 65"
              class=""
            >
              Basierend auf den Ergebnissen aus Ihrem ITS-Kompetenztest
              benötigen Sie kein Training im Bereich
              {{ threat.threat_vector.threat_event.event_name }}
            </div>
            <div v-if="Math.round((threat.pointsScored / 14) * 100) <= 65">
              Basierend auf den Ergebnissen aus Ihrem ITS-Kompetenztest könnte
              ein ITS-Training im Bereich
              {{ threat.threat_vector.threat_event.event_name }} ihre
              ITS-Kompetenzen verbessern.
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useCompetenceTestStore } from "@/store/CompetenceTestStore";
import { mapState } from "pinia";

export default {
  props: {
    competenceDimensions: {
      type: Object,
      default: () => {},
    },
    threatVectors: {
      type: Object,
      default: () => {},
    },
  },
  data() {
    return {
      competenceTestResult: {},
      goodResult: false,
      badResult: false,
    };
  },
  /**
   * A Vue component lifecycle method that runs once the component is mounted to the DOM.
   * Before the content is rendered this method fetches the competence test results from local storage.
   */
  mounted() {
    this.competenceTestResult = this.getCompetenceTestResult();
  },
  methods: {
    /**
     * Utilizes Vuex's `mapState` to bind the `getCompetenceTestResult` state from the `useCompetenceTestStore` to local component data.
     * This mapping allows the component to access `getCompetenceTestResult` directly from the component's computed properties.
     */
    ...mapState(useCompetenceTestStore, ["getCompetenceTestResult"]),
  },
};
</script>
