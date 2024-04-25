<template>
  <div class="overflow-x-auto">
    <table
      class="rounded-lg w-full text-xs md:text-sm xl:text-lg text-left px-4 bg-white"
    >
      <thead
        class="border-b pl-6 bg-primary rounded-lg text-white uppercase h-20"
      >
        <tr class="h-24">
          <th class="pl-2 w-4/12">ITS-Bedrohung</th>
          <th class="px-2 w-6/12">Beschreibung</th>
          <th class="px-2 w-2/12">Punktzahl</th>
        </tr>
      </thead>
      <tbody v-if="threats">
        <tr
          v-for="resource in threats"
          :key="resource.id"
          class="my-4 border-b break-words"
        >
          <td class="max-w-xs px-4 break-words">
            {{ resource.threat_vector_name }}
          </td>
          <td class="max-w-xs px-4 my-4 break-words">
            {{ resource.threat_vector_description }}
          </td>
          <td
            class="px-2 whitespace-normal"
            :class="{
              'text-green-500':
                Math.round(
                  (resource.total_scoredPoints /
                    (numberOfParticipants * totalPossiblePointsPerThreat)) *
                    100
                ) >= 65,
              'text-red-500':
                Math.round(
                  (resource.total_scoredPoints /
                    (numberOfParticipants * totalPossiblePointsPerThreat)) *
                    100
                ) < 65,
            }"
          >
            {{
              Math.round(
                (resource.total_scoredPoints /
                  (numberOfParticipants * totalPossiblePointsPerThreat)) *
                  100
              )
            }}%
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    threats: {
      type: Object,
      default: null,
    },
    maxPointsPerCompetenceDimension: {
      type: Number,
      default: 0,
    },

    totalPossiblePointsPerThreat: {
      type: Number,
      default: 0,
    },
    numberOfParticipants: {
      type: Number,
      default: 0,
    },
  },
};
</script>
