<template>
  <div class="bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div
        class="border-2 rounded-lg shadow-lg divide-y divide-gray-200"
        :class="{
          'border-green-500':
            Math.round(
              (threat.total_scoredPoints /
                (competenceTestResults.number_of_participants *
                  totalPossiblePointsPerThreat)) *
                100
            ) >= 65,
          'border-red-500':
            Math.round(
              (threat.total_scoredPoints /
                (competenceTestResults.number_of_participants *
                  totalPossiblePointsPerThreat)) *
                100
            ) < 65,
        }"
      >
        <div class="p-6 h-80">
          <h2 class="text-lg leading-6 font-medium text-gray-900">
            {{ threat.threat_vector_name }}
          </h2>
          <p class="mt-4 text-sm text-gray-500">
            {{ threat.threat_vector_description }}
          </p>
          <p class="mt-8">
            <span class="text-4xl font-extrabold text-gray-900"
              >{{
                Math.round(
                  (threat.total_scoredPoints /
                    (competenceTestResults.number_of_participants *
                      totalPossiblePointsPerThreat)) *
                    100
                )
              }}%</span
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
              v-for="feature in threat.related_competence_dimension_scores[
                threatKey
              ]"
              :key="feature"
              class="flex space-x-3"
            >
              <CheckIcon
                v-if="
                  feature.total_scoredPoints /
                    (competenceTestResults.number_of_participants *
                      maxPointsPerCompetenceDimension) >=
                  0.66
                "
                class="flex-shrink-0 h-5 w-5 text-green-500"
                aria-hidden="true"
              />

              <XMarkIcon
                v-else-if="
                  feature.total_scoredPoints /
                    (competenceTestResults.number_of_participants *
                      maxPointsPerCompetenceDimension) <=
                  0.33
                "
                class="flex-shrink-0 h-5 w-5 text-red-500"
                aria-hidden="true"
              />
              <ExclamationTriangleIcon
                v-else
                class="flex-shrink-0 h-5 w-5 text-yellow-500"
                aria-hidden="true"
              />
              <span class="text-sm text-gray-500">{{
                feature.competence_dimension_name
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
            v-if="
              Math.round(
                (threat.total_scoredPoints /
                  (competenceTestResults.number_of_participants *
                    totalPossiblePointsPerThreat)) *
                  100
              ) < 65
            "
            class=""
          >
            Basierend auf den Ergebnissen aus den aggregierten
            ITS-Kompetenztests könnten Ihre Mitarbeiter*innen ein Training im
            Bereich
            {{ threat.threat_vector_name }} benötigen.
          </div>
          <div v-else>
            Basierend auf den Ergebnissen aus den aggregierten
            ITS-Kompetenztests benötigen Ihre Mitarbeiter*innen
            <strong>kein Training </strong> im Bereich
            {{ threat.threat_vector_name }} benötigen.
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    threatKey: {
      type: String,
      default: "",
    },
    maxPointsPerCompetenceDimension: {
      type: Number,
      default: 0,
    },
    threat: {
      type: Object,
      default: () => {},
    },
    totalPossiblePointsPerThreat: {
      type: Number,
      default: 0,
    },
    competenceTestResults: {
      type: Object,
      default: () => {},
    },
  },
};
</script>
