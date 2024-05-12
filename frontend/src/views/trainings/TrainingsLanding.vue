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
        beendet. Vielen Dank für Ihre Teilnahme!
      </p></template
    >
    <template #buttons>
      <div
        class="flex justify-center items-center lg:items-start lg:justify-start flex-row"
      >
        <div
          class="flex justify-center items-center lg:items-start lg:justify-start"
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
    <div class="flex justify-center mt-20 pb-20">
      <button
        class="w-40 lg:transform lg:hover:scale-105 lg:duration-500 bg-primary text-white lg:bg-white lg:border-primary border-2 border-primary lg:text-primary my-2 py-1 px-4 mx-2 rounded lg:hover:text-white lg:hover:bg-primary"
        @click="navigateToGetStarted()"
      >
        Zurück zum Start
      </button>
    </div>
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

import { useCompetenceTestStore } from "@/store/CompetenceTestStore";
import { useTrainingsStore } from "@/store/TrainingsStore";
import * as XLSX from "xlsx";

import { mapState } from "pinia";

export default {
  components: {
    Steps,
    Hero,
    TrainingsTable,
    ImageImpulseSkeleton,
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
    };
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
    this.trainings = await this.trainingsStore.getTrainings();

    this.totalPages = Math.ceil(this.trainings.length / this.perPage);
    this.competenceTestResult = this.getCompetenceTestResult();
    if (Object.keys(this.competenceTestResult).length == 0) {
      this.$router.push("/");
      return;
    }

    this.matchTrainings();
    setTimeout(() => (this.loading = false), 500);
  },

  methods: {
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
