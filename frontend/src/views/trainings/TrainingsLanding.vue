<template>
  <div class="standard-container mb-20">
    <steps :activestate="activeStep" linecolor="gray" class="pt-10"></steps>
  </div>
  <Hero
    ><template #title>
      <h1 class="main-heading">
        <span class="text-primary xl:inline"
          >Trainingsempfehlungen <br />
        </span>
        {{ " " }}
        <span class="text-secondary xl:inline"
          >im Bereich Informationssicherheit</span
        >
      </h1></template
    >
    <template #content>
      <p
        class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
      >
        In dieser Ansicht erhalten Sie kostenlose ITS-Trainingsempfehlungen.
        <br />
        Diese sind nach Relevanz basierend auf den Ergebnissen aus Ihrem
        ITS-Kompetenztest geordnet. <br />
        <strong>
          Angebote, die einer Trainings-Gruppe angehören sind als gleich
          effektiv bewertet!
        </strong>
        <br />
        Durch einen Klick auf das jeweilige Training erhalten Sie umfassende
        Informationen zu dem Trainings-Angebot. Ihr ITS-Kompetenztest ist nun
        beendet. Vielen Dank für Ihre Teilnahme! <br />
        <br /></p
    ></template>
    <template #buttons>
      <div class="flex flex-row justify-center items-center lg:justify-start">
        <div
          class="flex flex-col justify-center items-center lg:items-start lg:justify-start"
        >
          <a
            class="w-full cursor-pointer flex justify-between font-semibold items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-primary hover:bg-primaryAccent mt-12 md:py-4 md:text-lg md:px-10"
            @click="exportTrainingsToExcel()"
          >
            Trainings abrufen
            <CloudArrowDownIcon class="ml-4 w-8 h-8"></CloudArrowDownIcon>
          </a>
        </div>
      </div>
    </template>
  </Hero>
  <div class="page-background">
    <div class="standard-container mb-10">
      <trainings-table
        v-if="trainings && !loading"
        :columns="columns"
        :per-page="perPage"
        :total-pages="totalPages"
        :current-page="currentPage"
        :trainings="trainingsFiltered"
        :total-trainings="trainings.length"
        @re-filter-training="reFilterTrainings"
      ></trainings-table>
      <div v-else class="h-150 bg-white p-4 rounded-lg">
        <image-impulse-skeleton></image-impulse-skeleton>
      </div>
    </div>
  </div>
  <div class="standard-container mb-10">
    <h1 class="main-heading mb-10 mt-10">Weitere Trainings-Empfehlungen</h1>
    <div class="flex flex-row justify-center items-center">
      <div class="border-b-4 w-14 rounded-lg border-secondary mb-10"></div>
    </div>
    <div class="flex flex-col items-center justify-center mb-10">
      <p
        class="mt-3 text-base text-center text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
      >
        Sie möchten sich über die frei verfügbaren ITS-Trainingsangebote hinaus
        weiterbilden?
        <br />
        Im Folgenden stellen wir Ihnen vor, worauf Sie dabei gemäß des Ansatzes
        von ITS.kompetent bei Ihrer Suche nach ITS-Trainingsangeboten achten
        sollten.
        <br />
      </p>
    </div>
    <h1
      class="text-2xl tracking-tight font-extrabold text-primary text-center sm:text-3xl md:text-4xl mb-10"
    >
      ITS-Trainigsmodule
    </h1>
    <div class="flex flex-row justify-center items-center">
      <div class="border-b-4 w-14 rounded-lg border-secondary mb-10"></div>
    </div>
    <div class="flex flex-col items-center justify-center mb-10">
      <p
        class="mt-3 text-base text-center text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
      >
        Unsere Klassifikation von ITS-Bedrohungen lässt sich insgesamt zu 7
        ITS-Trainingsmodulen zuordnen.
        <br />
      </p>
    </div>
    <div
      v-if="activeTrainingCategory"
      class="flex justify-center items-center mb-10"
    >
      <Listbox v-model="activeTrainingCategory">
        <div class="relative mt-1 w-1/2">
          <ListboxButton
            class="relative w-full cursor-default rounded-lg text-primary bg-gray-100 pl-2 text-center py-2 text-left shadow-md focus:outline-none focus-visible:border-indigo-500 focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75 focus-visible:ring-offset-2 focus-visible:ring-offset-orange-300 text-sm lg:text-xl"
          >
            <span class="block truncate">{{
              activeTrainingCategory.training_category_name
            }}</span>
            <span
              class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-2"
            >
              <ChevronUpDownIcon
                class="h-6 w-6 text-gray-500"
              ></ChevronUpDownIcon>
            </span>
          </ListboxButton>

          <transition
            leave-active-class="transition duration-100 ease-in"
            leave-from-class="opacity-100"
            leave-to-class="opacity-0"
          >
            <ListboxOptions
              class="absolute mt-1 max-h-60 w-full text-primary overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none text-sm lg:text-xl"
            >
              <ListboxOption
                v-for="category in trainingCategories"
                v-slot="{ selected }"
                :key="category.training_category_name"
                :value="category"
                as="template"
              >
                <li
                  :class="[
                    selected ? 'bg-gray-200 text-primary' : 'text-gray-900',
                    'relative cursor-pointer select-none py-2 pl-10 pr-4',
                  ]"
                >
                  <span
                    :class="[
                      selected ? 'font-medium' : 'font-normal',
                      'block truncate',
                    ]"
                    >{{ category.training_category_name }}</span
                  >
                  <span
                    v-if="selected"
                    class="absolute inset-y-0 left-0 flex items-center pl-3 text-primary"
                  >
                  </span>
                </li>
              </ListboxOption>
            </ListboxOptions>
          </transition>
        </div>
      </Listbox>
    </div>
    <div
      v-if="activeTrainingCategory"
      class="rounded-lg bg-gray-100 p-8 whitespace-pre-line text-md xl:text-lg text-left"
      v-html="sanitizedTrainingCategoryContent"
    ></div>
  </div>
  <div class="gradient-background">
    <div class="standard-container p-10">
      <explanation-card>
        <template #heading>Aufbau eines ITS-Trainingsmoduls</template>
        <template #title
          >Jedes ITS-Trainingsmodul sollte anhand verschiedener
          Handlungssituationen trainiert werden. Eine Handlungssituation wird
          über eine kurze Szenariobeschreibung eingeleitet, die möglichst nah an
          realistischen Arbeitssituationen der Mitarbeitenden eines jeweiligen
          ITS-Anforderungsprofils ist. Jede Handlungssituation beinhaltet zudem
          eine Kombination aus einem ITS-Bedrohungsereignis und einem
          ITS-Bedrohungsbereich. Pro Handlungssituation werden die 7
          verschiedenen ITS-Kompetenzdimensionen trainiert. Die Abbildung
          veranschaulicht den Zusammenhang.</template
        >

        <template #image>
          <img
            src="@/assets/Structure_of_Trainings.png"
            class="w-full exportImages"
            alt="Sample image"
          />
        </template>
        <template #title2>ITS-Kompetenzdimensionen</template>
        <template #threatAwareness>Threat Awareness</template>
        <template #threatAwarenessText
          >Pro Handlungssituation innerhalb eines ITS-Trainingsmoduls können
          drei verschiedene Szenarien aus dem Alltag einer Tätigkeit dargestellt
          werden, die unterschiedlich bedeutsame oder keine ITS-Bedrohung
          darstellen. Mitarbeitende bekommen nun erklärt, welche ITS-Bedrohung
          am gefährlichsten ist, welches eine moderate ITS-Bedrohung darstellt
          und welche Situation mit der geringsten Wahrscheinlichkeit eine
          ITS-Bedrohung darstellt. Auf diese Weise lernen Mitarbeitende
          bedrohliche von eher unbedrohlichen Situationen in ihrem Arbeitsalltag
          abzugrenzen.
        </template>
        <template #threatIdentification>Threat Identification</template>
        <template #threatIdentificationText
          >Pro Handlungssituation innerhalb eines ITS-Trainingsmoduls sollten
          für die jeweiligen ITS-Bedrohungen mit großem und moderatem
          Gefahrenpotential, die in der Threat Awareness behandelt werden,
          Merkmale der Gefahrenquelle aufgelistet werden.
        </template>
        <template #threatImpactAssessment>Threat Impact Assessment</template>
        <template #threatImpactAssessmentText
          >Pro Handlungssituation innerhalb eines ITS-Trainingsmoduls sollten
          Mitarbeitende mit einer Auswahl an Konsequenzen ihres potenziellen
          Handelns im Umgang mit ITS-Bedrohungen konfrontiert werden. Anhand
          verschiedener Beispiele sollte deutlich werden, welche Konsequenz den
          größten Einfluss auf die Unternehmenstätigkeit hat.
        </template>
        <template #tacticChoice>Tactic Choice</template>
        <template #tacticChoiceText
          >Pro Handlungssituation innerhalb eines ITS-Trainingsmoduls sollten
          Mitarbeitende geschult werden erste Schritte zur Gefahrenabwehr im
          eigenen Handlungs-/Verantwortungsbereich vornehmen zu können, wenn sie
          mit einer ITS-Bedrohung konfrontiert sind.
        </template>
        <template #tacticJustification>Tactic Justification</template>
        <template #tacticJustificationText
          >Pro Handlungssituation innerhalb eines ITS-Trainingsmoduls sollten
          Mitarbeitende geschult werden, die ausgewählten ersten Gegenmaßnahmen
          zur Begegnung der ITS-Bedrohung im Hinblick auf die Handlungssituation
          begründen zu können. Das Wissen über Begründungen könnte wesentlich
          dazu beitragen, dass Mitarbeitende das geforderte Verhalten adäquat
          umsetzen.
        </template>
        <template #tacticMastery>Tactic Mastery</template>
        <template #tacticMasteryText
          >Pro Handlungssituation innerhalb eines ITS-Trainingsmoduls sollten
          Mitarbeitende trainiert werden, die richtige Gegenmaßnahme
          durchzuführen, um eine ITS-Bedrohung einzudämmen.
        </template>
        <template #tacticCheck>Tactic Check & Follow-Up</template>
        <template #tacticCheckText
          >Mitarbeitende sollen darauf vorbereitet werden, wie sich angemessene
          Folgemaßnahmen in verschiedenen Situationen, die eine ITS-Bedrohung in
          Ihrem Arbeitsalltag darstellen können, unterscheiden können. Diese
          Folgemaßnahmen beziehen sich auf die Wirkungskontrolle und die
          Prävention.
        </template>
      </explanation-card>
    </div>
  </div>
  <div class="page-background">
    <div class="standard-container">
      <h1
        class="text-2xl tracking-tight font-extrabold text-primary text-center sm:text-3xl md:text-4xl mb-10"
      >
        ITS-Trainigsmodule pro ITS-Anforderungsprofil
      </h1>
      <div class="flex flex-row justify-center items-center">
        <div class="border-b-4 w-14 rounded-lg border-secondary mb-10"></div>
      </div>
      <div class="flex flex-col items-center justify-center mb-10">
        <p
          class="mt-3 text-base text-center text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
        >
          <br />
          Die zuvor vorgestellten ITS-Trainingsmodule lassen sich zu den
          ITS-Bedrohungsereignissen für Ihr ITS-Anforderungsprofil zuordnen.
        </p>
        <p
          class="mt-3 font-semibold text-center text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
        >
          <br />
          Achtung: Die hier dargestellten ITS-Trainigsmodule sowie die darunter
          fallenden ITS-Bedrohungsereignisse und zugeordneten
          ITS-Bedrohungsbereiche basieren ausschließlich auf den Inhalten der
          ITS-Kompetenztests. Wir erheben keinen Anspruch auf Vollständigkeit.
          Mitunter können zum Beispiel auch weitere ITS-Trainingsmodule und
          ITS-Bedrohungsbereiche zu einem jeweiligen ITS-Bedrohunsgereignis
          relevant als Gegegenstand in einem ITS-Trainingsprogramm sein!
        </p>
      </div>

      <div
        v-if="activeJobProfilesWithTrainingCategories"
        class="flex flex-col xl:flex-row justify-center xl:text-lg items-center text-center bg-white mb-10 pt-4 xl:pt-2 rounded-lg xl:rounded-full p-2"
      >
        <button
          class="flex justify-center text-center py-4 mx-4 px-2 mb-2 sm:mb-0 rounded-full shadow bg-primary px-2 text-white w-1/2 xl:w-auto font-semibold"
        >
          {{ activeJobProfilesWithTrainingCategories.job_profile_name }}
        </button>
      </div>
      <div v-if="activeJobProfilesWithTrainingCategories">
        <training-category
          :job-profile="activeJobProfilesWithTrainingCategories"
          :threat-category-counts="sortedThreatCategoriesByRelevanceScore"
        ></training-category>
      </div>
    </div>
  </div>
  <div class="flex justify-center mt-20 pb-20">
    <button
      class="w-40 lg:transform lg:hover:scale-105 lg:duration-500 bg-primary text-white lg:bg-white lg:border-primary border-2 border-primary lg:text-primary my-2 py-1 px-4 mx-2 rounded lg:hover:text-white lg:hover:bg-primary"
      @click="navigateToGetStarted()"
    >
      Zurück zum Start
    </button>
  </div>
  <PopUp
    v-if="showFailurePopUp"
    :type="popupType"
    :title="popupTitle"
    :content="popupContent"
    @popup-closed="showFailurePopUp = false"
  />
  <PopUp
    v-if="showSuccessPopUp"
    :type="popupType"
    :title="popupTitle"
    :content="popupContent"
    @popup-closed="showSuccessPopUp = false"
  />
</template>

<script>
import Steps from "@/components/base/Steps.vue";
import Hero from "@/components/base/Hero.vue";
import TrainingsTable from "@/components/training/TrainingsTable.vue";
import ImageImpulseSkeleton from "@/components/base/ImageImpulseSkeleton.vue";
import DOMPurify from "dompurify";
import TrainingCategory from "@/components/training/TrainingCategory.vue";
import ExplanationCard from "@/components/dashboard/ExplanationCard.vue";

import { useCompetenceTestStore } from "@/store/CompetenceTestStore";
import { useTrainingsStore } from "@/store/TrainingsStore";
import { useJobProfileStore } from "@/store/JobProfileStore";

import * as XLSX from "xlsx";

import { mapState } from "pinia";

import {
  Listbox,
  ListboxButton,
  ListboxOptions,
  ListboxOption,
} from "@headlessui/vue";

export default {
  components: {
    Steps,
    Hero,
    ExplanationCard,
    TrainingsTable,
    TrainingCategory,
    ImageImpulseSkeleton,
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  },
  setup() {
    const competenceTestStore = useCompetenceTestStore();
    const trainingsStore = useTrainingsStore();

    return { competenceTestStore, trainingsStore };
  },

  data() {
    return {
      trainingsFiltered: null,
      trainings: null,
      trainingsTopic: 1,
      competenceTestResult: {},
      modalVisible: false,
      threatEvent: [],
      totalPages: 0,
      currentPage: 1,
      perPage: 5,
      activeStep: 4,
      loading: false,
      popupType: "",
      popupTitle: "",
      popupContent: "",
      showFailurePopUp: false,
      showSuccessPopUp: false,
      columns: [
        { name: "Trainings-Gruppe", attribute: "title", sortable: "title" },
        { name: "SETA Programm", attribute: "title", sortable: "title" },
        { name: "Anbieter", attribute: "status" },
        { name: "Methode", attribute: "status" },
        { name: "Kompetenzdimension", attribute: "status" },
        { name: "Matching-Score", attribute: "status" },
      ],
      trainingCategories: [],
      jobProfilesWithTrainingCategories: [],
      activeTabId: null,
      activeCategoryId: null,
      activeJobProfilesWithTrainingCategories: null,
      activeTrainingCategory: null,
      selectedProfileForThreatCategories: null,
      profileID: undefined,
    };
  },
  computed: {
    /**
     * Sanitizes the training cagtegory description
     */
    sanitizedTrainingCategoryContent() {
      return DOMPurify.sanitize(
        this.activeTrainingCategory.training_category_description
      );
    },
    /**
     * A Vue computed property.
     * Gets called whenever the selected job Profile for training categories changes
     * If so it calculates a relevance score for each training category associated to the job profile
     */
    threatCategoryCounts() {
      const categoryMap = {};

      this.activeJobProfilesWithTrainingCategories.threat_events.forEach(
        (event) => {
          const countMultiplier = event.threat_areas.length;

          event.threat_categories.forEach((category) => {
            if (categoryMap[category.category_name]) {
              categoryMap[category.category_name].relevanceScore +=
                countMultiplier;
            } else {
              categoryMap[category.category_name] = {
                category_name: category.category_name,
                category_description: category.category_description,
                relevanceScore: countMultiplier,
              };
            }
          });
        }
      );

      return Object.values(categoryMap);
    },
    /**
     * A Vue computed property.
     * Sorts the training categories by relevance score to be able to prioritize specifc training categories for a job profile.
     */
    sortedThreatCategoriesByRelevanceScore() {
      let threatCategoryCounts = this.threatCategoryCounts;
      threatCategoryCounts.sort((a, b) => b.relevanceScore - a.relevanceScore);

      let position = 1; // Start ranking from 1
      let lastScore = threatCategoryCounts[0].relevanceScore; // Score of the first item for comparison
      threatCategoryCounts[0].position = position; // Assign first rank manually

      for (let i = 1; i < threatCategoryCounts.length; i++) {
        if (threatCategoryCounts[i].relevanceScore !== lastScore) {
          position += 1;
        }
        threatCategoryCounts[i].position = position;
        lastScore = threatCategoryCounts[i].relevanceScore; // Update lastScore for comparison
      }
      return threatCategoryCounts;
    },
  },

  /**
   * A Vue component lifecycle method that runs once the component is mounted to the DOM.
   * Performs async calls to trainingsStore to fetch training programs from the database
   * Sets the active tab to FAQ if campagne was not started else set to Einladungs-Management.
   * Routes to Home if the competence test result in local storage is not applicable
   * Finally calls matchTrainings
   */
  async mounted() {
    this.loading = true;
    this.profileID = this.getProfileID();
    this.catchError(this.profileID);
    this.trainings = await this.trainingsStore.getTrainings();

    this.totalPages = Math.ceil(this.trainings.length / this.perPage);
    this.competenceTestResult = this.getCompetenceTestResult();
    if (Object.keys(this.competenceTestResult).length == 0) {
      this.$router.push("/");
      return;
    }
    this.trainingCategories = await this.trainingsStore.getTrainingCategories();
    this.activeCategoryId = this.trainingCategories[0].id;
    this.activeTrainingCategory = this.trainingCategories[0];

    this.jobProfilesWithTrainingCategories =
      await this.trainingsStore.getJobProfilesByTrainingCategories();

    this.activeJobProfilesWithTrainingCategories =
      this.jobProfilesWithTrainingCategories.find(
        (profile) => profile.job_profile_id === this.profileID
      );
    this.activeTabId =
      this.activeJobProfilesWithTrainingCategories.job_profile_id;

    this.matchTrainings();
    setTimeout(() => (this.loading = false), 500);
  },

  methods: {
    /**
     * Utilizes Vuex's `mapState` to bind the `getProfileID` state from the `useJobProfileStore` to local component data.
     * This mapping allows the component to access `getProfileID` directly from the component's computed properties.
     */
    ...mapState(useJobProfileStore, ["getProfileID"]),
    /**
     * Handles undefined profile ID errors by stopping the loading state, redirecting to the "Profile" route,
     * and showing a popup notification.
     *
     * @param {string|undefined} profileID - The profile ID to check. If undefined, triggers error handling.
     */
    catchError(profileID) {
      if (profileID === undefined) {
        this.loading = false;
        this.$router.push({ name: "Profile" });
        this.showPopUp = true;
      }
    },
    /**
     * Is used to change the training category
     * @param {Array} index The index of the training catgeory that gets displayed
     */
    async changeTrainingCategory(index) {
      this.activeTrainingCategory = this.trainingCategories[index];
      this.activeCategoryId = this.activeTrainingCategory.id;
    },
    /**
     * Navigates to the GetStarted component
     *
     */
    navigateToGetStarted() {
      this.$router.push({ name: "GetStarted" });
    },
    /**
     * Utilizes Vuex's `mapState` to bind the `getCompetenceTestResult` state from the `competenceTestStore` to local component data.
     * This mapping allows the component to access `getCompetenceTestResult` directly from the component's computed properties.
     */
    ...mapState(useCompetenceTestStore, ["getCompetenceTestResult"]),
    /**
     * Base method to calcualate a matching score for each training program based on the competence test result of the user
     * Calls a method to sort and shuffle trainings
     */
    matchTrainings() {
      let matchingScore = 0;
      let tempArray = [];

      for (let i = 0; i < this.trainings.length; i++) {
        for (
          let j = 0;
          j < this.competenceTestResult.competenceDimensionScore.score.length;
          j++
        ) {
          let competenceDimensionMatchingScore = 0;
          let trainingCompetence = 0;
          let trainingFocus = 0;
          let inverseCompetenceDimensionScore = 0;
          if (
            this.isCompetenceDimensionInTraining(
              this.competenceTestResult.competenceDimensionScore.label[j],
              this.trainings[i]
            )
          ) {
            trainingCompetence = 1;
          }

          inverseCompetenceDimensionScore =
            this.competenceTestResult.competenceDimensionScore.score[j] /
            (this.competenceTestResult.test_situations.length * 2);

          inverseCompetenceDimensionScore =
            (1 - inverseCompetenceDimensionScore) * 10;

          trainingFocus =
            this.competenceTestResult.competenceDimensionScore.score.length /
            this.trainings[i].competence_dimension_count;

          competenceDimensionMatchingScore =
            inverseCompetenceDimensionScore *
            (trainingCompetence * trainingFocus);

          matchingScore += competenceDimensionMatchingScore;
          tempArray.push(competenceDimensionMatchingScore);
        }
        this.trainings[i].matchingScore = Math.round(matchingScore);
        this.trainings[i].tempArray = tempArray;
        tempArray = [];
        matchingScore = 0;
      }
      this.sortAndShuffleTrainings();
    },
    /**
     * helper method to check whether a specific competence dimension is conveyed in a training program
     * @param {string} competenceDimensionName The name of the competence dimension
     * @param {Object} training The training object
     * @return {Boolean} True or false
     */
    isCompetenceDimensionInTraining(competenceDimensionName, training) {
      return training.competence_dimensions.some(
        (obj) => obj.dimension_name === competenceDimensionName
      );
    },
    /**
     * Method to shuffle trainings with equal matching score to not prefer a training program
     * @param {Array} array The array of training programs
     */
    shuffleArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]]; // Swap
      }
    },
    /**
     * Method to assign ranks to the training program based on the matching score. The lower the rank, the better the match.
     */
    assignRanks() {
      let rank = 1; // Start ranking from 1
      let lastScore = this.trainings[0].matchingScore; // Score of the first item for comparison
      this.trainings[0].rank = rank; // Assign first rank manually

      for (let i = 1; i < this.trainings.length; i++) {
        if (this.trainings[i].matchingScore !== lastScore) {
          // Increment rank by the number of items with the previous score
          rank += 1;
          //sameScoreCount = 1; // Reset counter
        }
        this.trainings[i].rank = rank;
        lastScore = this.trainings[i].matchingScore; // Update lastScore for comparison
      }
    },
    /**
     * Method to sort the training programs by matchingScore in descending order
     * Calls shuffleArray to shuffle training programs with equal matching score.
     */
    sortAndShuffleTrainings() {
      // Initial sort by matchingScore in descending order
      this.trainings.sort((a, b) => b.matchingScore - a.matchingScore);

      // Group by matchingScore
      const groupedByScore = this.trainings.reduce((acc, curr) => {
        if (!acc[curr.matchingScore]) acc[curr.matchingScore] = [];
        acc[curr.matchingScore].push(curr);
        return acc;
      }, {});

      const sortedAndShuffled = [];

      // Sort scores in descending order
      const scores = Object.keys(groupedByScore)
        .map(Number)
        .sort((a, b) => b - a);

      scores.forEach((score) => {
        const trainings = groupedByScore[score];

        // Group by training_group.id within each matchingScore
        const groupedByTrainingGroup = trainings.reduce((acc, curr) => {
          if (!acc[curr.training_group.id]) acc[curr.training_group.id] = [];
          acc[curr.training_group.id].push(curr);
          return acc;
        }, {});

        const trainingGroups = Object.values(groupedByTrainingGroup);
        // Shuffle the order of training groups with the same matchingScore
        this.shuffleArray(trainingGroups);

        // Flatten, shuffle trainings within each group, and add to the final array
        trainingGroups.forEach((group) => {
          // Now shuffle trainings within each group
          this.shuffleArray(group);
          // Then concatenate to the sortedAndShuffled array
          sortedAndShuffled.push(...group);
        });
      });

      // Replace the original trainings array with the sorted and shuffled one
      this.trainings = sortedAndShuffled;
      this.mapPageNumbers();
      this.assignRanks();
      this.filterTrainingsPerPage();
    },
    /**
     * Method to add page numbers to each training after sorted by matching score
     */
    mapPageNumbers() {
      this.trainings = this.trainings.map((item, index) => ({
        ...item,
        pageNumber: Math.floor(index / this.perPage + 1),
      }));
    },
    /**
     * Method to filter the training programs by page number
     * Used for pagination
     */
    filterTrainingsPerPage() {
      this.trainingsFiltered = this.trainings.filter(
        (item) => item.pageNumber === this.currentPage
      );
    },
    /**
     * Method to call the filtering of training programs based on the page number.
     * @param {Number} page The current page number emitted
     */
    reFilterTrainings(page) {
      this.currentPage = page;
      this.filterTrainingsPerPage();
    },
    /**
     * Method to prepare the data before exporting to excel.
     * @param {Array} dataArray The training programs
     *
     */
    prepareDataForExport(dataArray) {
      return dataArray.map((item) => ({
        Anbieter: item.training_provider,
        "Programm Name": item.training_name,
        "Enthaltene ITS-Kompetenzdimensionen": item.competence_dimensions
          .map((competenceItem) => competenceItem.dimension_name)
          .join(", "),
        "Enthaltene ITS-Bedrohungsereignisse": item.threat_event
          .map((event) => event.event_name)
          .join(", "),
        Kosten: item.costs_name,
        Zertifizierung: item.certification,

        Sprachen: item.language
          .map((languageItem) => languageItem.language)
          .join(", "),
        "URL zum Anbieter": item.training_url,
        Vermittlungsmethode: item.delivery_method
          .map((methodItem) => methodItem.delivery_method)
          .join(", "),
        Rang: item.rank,
      }));
    },
    /**
     * Method to generate an excel file including the training programs sorted by matching score.
     * @throws {Error} Throws an error when an excel file cannot be created.
     */
    async exportTrainingsToExcel() {
      this.loading = true;
      let dataToExport = this.trainings;
      dataToExport = this.prepareDataForExport(dataToExport);

      // Continue with the SheetJS export process
      const workbook = XLSX.utils.book_new();

      const worksheet = XLSX.utils.json_to_sheet(dataToExport);
      XLSX.utils.book_append_sheet(
        workbook,
        worksheet,
        `ITS-Anforderungsprofil`
      );

      // Trigger download
      try {
        XLSX.writeFile(workbook, "ITS-Trainingsempfehlungen.xlsx");
        this.popupType = "success";
        this.popupTitle = "ITS-Trainingsempfehlungen exportieren";
        this.popupContent = "Ein Excel-File wurde erstellt und heruntergeladen";
        this.showSuccessPopUp = true;
      } catch (err) {
        console.error("Could not download excel file: ", err);
        this.popupType = "danger";
        this.popupTitle = "ITS-Trainingsempfehlungen exportieren";
        this.popupContent = "Der Text konnte nicht kopiert werden.";
        this.showFailurePopUp = true;
      }
      this.loading = false;
    },
  },
};
</script>

<style scoped>
.gradient-background {
  background: linear-gradient(
    to right,
    #303e7a 0%,
    #303e7a 50%,
    #f1f5f9 50%,
    #f1f5f9 100%
  );
}
.gradient-background-secondary {
  background: linear-gradient(
    to right,
    #eb5757 0%,
    #eb5757 50%,
    #1e293b 50%,
    #1e293b 100%
  );
}
</style>
