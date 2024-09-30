<template>
  <div class="bg-white rounded-lg shadow-md text-left overflow-hidden">
    <div class="bg-primary px-6 py-4">
      <div
        class="font-bold text-white space-y-4 divide-y divide-gray-200 text-xl mb-2"
      >
        ITS-Trainingsempfehlungen für das ITS-Anforderungsprofil
        {{ jobProfile.job_profile_name }}
      </div>
    </div>
    <div class="px-6 py-4">
      <p class="text-gray-700 whitespace-pre-line text-base"></p>
      <div class="mt-4">
        <div class="overflow-x-auto">
          <table
            class="min-w-full bg-white text-md xl:text-lg border border-gray-300"
          >
            <thead>
              <tr>
                <th class="py-2 px-4 border-b">ITS-Bedrohungsereignis</th>

                <th class="py-2 px-4 border-b">
                  Beschreibung des ITS-Bedrohungsereignisses
                </th>
                <th class="py-2 px-4 border-b">
                  Beispielhafte betroffene ITS-Bedrohunsgbereiche
                </th>
                <th class="py-2 px-4 border-b">ITS-Trainigsmodul</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(event, eventIndex) in jobProfile.threat_events"
                :key="eventIndex"
              >
                <td class="py-2 px-4 border-b w-2/12">
                  {{ event.event_name }}
                </td>
                <td class="py-2 px-4 border-b w-5/12">
                  {{ event.event_description }}
                </td>
                <td class="py-2 px-4 border-b w-3/12">
                  <ul class="list-disc list-inside">
                    <li
                      v-for="(threat_area, areaIndex) in event.threat_areas"
                      :key="areaIndex"
                    >
                      {{ threat_area.area_name }}
                    </li>
                  </ul>
                </td>
                <td class="py-2 px-4 border-b w-4/12">
                  <div class="flex flex-col">
                    <span
                      v-for="(category, catIndex) in event.threat_categories"
                      :key="catIndex"
                      :class="getCategoryClass(category.category_name)"
                      class="rounded-full p-2 my-2 b text-center"
                    >
                      {{ category.category_name }}
                    </span>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="px-6 py-4 bg-white">
      <h4 class="font-semibold text-md xl:text-lg text-primary">
        Empfehlungen zur Gestaltung eines ITS-Trainingsprogramms
      </h4>
      <p class="text-md xl:text-lg whitespace-pre-line">
        {{ jobProfile.job_profile_training_recommendation }}
      </p>
      <p class="text-md xl:text-lg mt-2 whitespace-pre-line">
        Für das ITS-Anforderungsprofil {{ jobProfile.job_profile_name }} sollten
        folgende ITS-Trainingsmodule mit den angegebenen Prioritäten
        berücksichtigt werden. Jedes ITS-Trainingsmodul sollte aus mehreren
        Kombinationen von ITS-Bedrohungsereignissen und ITS-Bedrohungsbereichen
        (ITS-Bedrohungen) bestehen, anhand derer die ITS-Kompetenzdimensionen
        vermittelt werden. Die Handlungssituationen, in denen die
        ITS-Bedrohungen vermittelt werden, sollten an authentischen
        Alltagssituationen des ITS-Anforderungsprofils
        {{ jobProfile.job_profile_name }} angelehnt sein.
      </p>
      <div class="flex flex-row">
        <div
          v-for="(category, catIndex) in threatCategoryCounts"
          :key="catIndex"
          class="flex flex-col mr-4 mt-5 text-center font-semibold"
        >
          Priorität {{ category.position }}
          <span
            :class="getCategoryClass(category.category_name)"
            class="rounded-full p-2 my-2 b font-normal text-center"
          >
            {{ category.category_name }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "TrainingCategory",
  props: {
    jobProfile: {
      type: Object,
      required: true,
    },
    threatCategoryCounts: {
      type: Array,
      required: true,
    },
  },
  data() {
    return {
      categoryColors: {
        "Social Engineering": { bg: "bg-green-100", text: "text-green-600" },
        "Umgang mit Malware": { bg: "bg-blue-100", text: "text-blue-600" },
        "Hardware und Berechtigungen": {
          bg: "bg-yellow-100",
          text: "text-yellow-600",
        },
        Schwachstellenausnutzung: { bg: "bg-red-100", text: "text-red-600" },
        Informationsweitergabe: {
          bg: "bg-purple-100",
          text: "text-purple-600",
        },
        "Denial-of-Service": {
          bg: "bg-pink-100",
          text: "text-pink-600",
        },
        Passwortmanagement: {
          bg: "bg-indigo-100",
          text: "text-indigo-600",
        },
      },
    };
  },

  methods: {
    /**
   * Applies the custom color to each training category
   */
    getCategoryClass(categoryName) {
      const colors = this.categoryColors[categoryName] || {
        bg: "bg-gray-100",
        text: "text-gray-600",
      };
      return `${colors.bg} ${colors.text}`;
    },
  },
};
</script>


