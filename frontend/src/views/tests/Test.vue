<template>
  <div class="standard-container">
    <steps :activestate="activeStep" linecolor="gray" class="pt-5"></steps>
  </div>

  <template v-if="loading">
    <spinner></spinner>
    <!-- here use a loaded you prefer -->
  </template>

  <template v-else>
    <!-- Base Hero, is displayed -->
    <Hero
      ><template #title>
        <div class="flex justify-center items-center lg:justify-start">
          <h1
            class="text-center main-heading lg:text-left flex flex-col lg:flex-row flex-wrap items-center lg:items-start"
          >
            <span class="text-primary">ITS-Bedrohungssituation&nbsp;</span>
            <span class="text-secondary">
              {{ threatVectorIndex }} von {{ testTotalThreatSituations }}
            </span>
          </h1>
        </div>
      </template>
      <template #content>
        <div
          class="flex flex-col justify-center items-center lg:items-start lg:justify-start"
        >
          <p
            class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
          >
            {{ activeThreatSituation.threat_description }}
          </p>
          <p
            v-if="!questionView"
            class="mt-3 text-base text-gray-500 font-semibold sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
          >
            {{ activeImpulseItems.impulse_text }}
          </p>
        </div>
        <div
          v-if="questionView && threatAwareness"
          class="flex flex-col justify-center items-center lg:items-start lg:justify-start"
        >
          <p
            class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
          >
            Schauen Sie sich bitte noch einmal
            <strong>{{ impulseScenario }} </strong> genauer an und beantworten
            Sie dann die dazu bereitgestellte Frage.
          </p>
        </div>
      </template>
     
    </Hero>

    <div ref="scrollTarget" class="mb-10"></div>
    <div class="page-background">
      <div class="standard-container">
        <div class="pb-16 flex flex-col justify-center items-center">
          <h2 class="ml-6 pt-3 pb-3 text-2xl font-semibold">Testfortschritt</h2>

          <ProgressBar
            ref="progress"
            class="w-full pt-20 mb-20 sm:w-3/4 2xl:w-1/2"
            :percentage="contentProgress"
          >
            <span
              class="text-sm text-white font-bold w-full flex justify-end pr-2"
            ></span>
          </ProgressBar>
        </div>
        <button
          v-if="!threatAwareness"
          class="mt-10 transform bg-primary text-white lg:hover:scale-105 duration-500 lg:text-primary lg:bg-white border-primary font-button border-2 my-2 py-1 px-4 mx-2 rounded hover:text-white hover:bg-primary"
          @click="toggleScenario()"
        >
          <span v-if="!showImpulse"> Szenario einblenden </span>
          <span v-if="showImpulse"> Szenario ausblenden</span>
        </button>
      </div>
      <div class="standard-container">
        <div v-if="showImpulse">
          <div v-if="loading" class="h-96 bg-white p-4 rounded-lg">
            <image-impulse-skeleton></image-impulse-skeleton>
          </div>
          <transition v-else appear name="fade">
            <div>
              <email-simulation
                v-if="activeImpulseItems.resourcetype == 'EmailImpulse'"
                :emails="activeImpulseItems.email"
                :filter-index="scenarioNumber"
              ></email-simulation>
              <image-impulse
                v-if="
                  activeImpulseItems.resourcetype == 'ImageImpulse' && !loading
                "
                :images="activeImpulseItems.image"
                :filter-index="scenarioNumber"
              ></image-impulse>
              <chat-impulse
                v-if="activeImpulseItems.resourcetype == 'ChatImpulse'"
                :chat-interfaces="activeImpulseItems.chat_interface"
                :filter-index="scenarioNumber"
              >
              </chat-impulse>
            </div>
          </transition>
          <div class="flex flex-col items-center justify-center">
            <div
              v-if="!loading && showFirstQuestionButton"
              class="flex justify-center mt-20"
            >
              <button
                class="mt-10 transform hover:scale-105 duration-500 bg-white border-primary font-button border-2 text-primary my-2 py-1 px-4 mx-2 rounded hover:text-white hover:bg-primary"
                @click="showQuestion"
              >
                Erste Testfrage anzeigen
              </button>
            </div>
            <sortable-question
              v-if="activeQuestion.type == 3 && showQuestionToImpulse"
              class="items-center justify-center mt-40"
              :options="activeAnswerOptions"
              @change="changesAnswerOfSortable"
            >
              <template #questionContent>
                <div class="whitespace-pre-line">
                  {{ activeQuestion.question }}
                </div></template
              >

              <template #questionTag>{{
                activeTestItem.competence_dimension.dimension_name
              }}</template>
            </sortable-question>
          </div>
        </div>
        <div v-show="questionView" v-if="!loading">
          <div
            v-if="activeTestItem.question_item"
            class="flex flex-col justify-center items-center mt-20"
          >
            <single-choice-question
              v-if="activeQuestion.type == 1"
              class="mb-10"
              :value="activeAnswer"
              :options="activeAnswerOptions"
              @change="changesAnswerOfSingleChoice"
            >
              <template #questionContent class="whitespace-pre-line"
                ><div class="whitespace-pre-line">
                  {{ activeQuestion.question }}
                </div></template
              >

              <template #questionTag>{{
                activeTestItem.competence_dimension.dimension_name
              }}</template>
            </single-choice-question>
            <multi-choice-question
              v-if="activeQuestion.type == 2"
              v-model="activeAnswer"
              class="mb-10"
              :value="activeAnswer"
              :options="activeAnswerOptions"
              @change="changesAnswerOfMultipleChoice"
            >
              <template #questionContent>
                <div class="whitespace-pre-line">
                  {{ activeQuestion.question }}
                </div></template
              >
              <template #questionTag>{{
                activeTestItem.competence_dimension.dimension_name
              }}</template>
              > >
            </multi-choice-question>
            <sortable-question
              v-if="activeQuestion.type == 3"
              :options="activeAnswerOptions"
              @change="changesAnswerOfSortable"
            >
              <template #questionContent
                ><div class="whitespace-pre-line">
                  {{ activeQuestion.question }}
                </div></template
              >

              <template #questionTag>{{
                activeTestItem.competence_dimension.dimension_name
              }}</template>
            </sortable-question>
            <!-- <rating-question
              v-if="activeQuestion.type == 3"
              :id="ratingItems[0].id"
              class="mb-10"
              @change="getButtonId"
            ></rating-question> -->
          </div>
        </div>
        <div v-else>
          <spinner></spinner>
        </div>

        <div
          v-if="!loading && showQuestionToImpulse"
          class="flex justify-center mt-20"
        >
          <button
            class="w-40 transform bg-primary text-white lg:hover:scale-105 duration-500 lg:text-primary lg:bg-white border-primary font-button border-2 my-2 py-1 px-4 mx-2 rounded hover:text-white hover:bg-primary"
            @click="continueTest"
          >
            Weiter
          </button>
        </div>
      </div>
      <PopUp
        v-if="showPopUp"
        type="danger"
        title="Antwortoption auswählen"
        content="Bitte wählen Sie eine Antwortoption aus"
        @popup-closed="showPopUp = false"
      />
    </div>
  </template>
</template>

<script>
import Steps from "@/components/base/Steps.vue";
import ProgressBar from "@/components/base/ProgressBar.vue";
import ImageImpulseSkeleton from "@/components/base/ImageImpulseSkeleton.vue";

import Hero from "@/components/base/Hero.vue";
import SingleChoiceQuestion from "../../components/questionnaire/SingleChoiceQuestion.vue";
import SortableQuestion from "../../components/questionnaire/SortableQuestion.vue";
import MultiChoiceQuestion from "../../components/questionnaire/MultiChoiceQuestion.vue";
// import Impulse items
import ChatImpulse from "../../components/simulations/ChatImpulse.vue";
import EmailSimulation from "../../components/simulations/EmailSimulation.vue";
import ImageImpulse from "../../components/simulations/ImageImpulse.vue";

// axios Services
import { useCompetenceTestStore } from "@/store/CompetenceTestStore";
import { useJobProfileStore } from "@/store/JobProfileStore";
import { useCampagneStore } from "@/store/CampagneStore";

import { mapState } from "pinia";

export default {
  components: {
    Steps,
    SingleChoiceQuestion,
    MultiChoiceQuestion,
    SortableQuestion,
    EmailSimulation,
    ImageImpulse,
    ProgressBar,
    Hero,
    ChatImpulse,
    ImageImpulseSkeleton,
  },
  /**
   * Initializes and returns the state for the Vue component using composition API.
   *
   * This setup function utilizes the Vuex stores specific to job profiles and competence tests.
   * It invokes `useCampagneStore` to access and manage the state related to job profiles,
   * and `useCompetenceTestStore` for managing state related to competence tests. The function
   * then returns these stores for use within the Vue component, enabling reactive state management
   * and encapsulation of business logic associated with job profiles and competence tests.
   *
   * @returns {Object} An object containing references to `campagneStore` and `competenceTestStore`.
   */
  setup() {
    const competenceTestStore = useCompetenceTestStore();
    const campagneStore = useCampagneStore();

    return { competenceTestStore, campagneStore };
  },

  data() {
    return {
      activeStep: 2,
      testItemCounter: 0,
      contentProgress: 0,
      loading: false,
      totalQuestions: 0,
      testSituations: [],
      threatSituations: [],
      testItems: [],
      // active Items
      activeThreatSituation: "",
      activeTestItem: "",
      activeQuestion: "",
      activeImpulseItems: [],
      activeAnswerOptions: [],
      activeAnswer: {
        userAnswer: [],
        answerQuality: 0,
      },
      answerRatingsByUser: [],
      impulseScenario: "",
      scenarioNumber: -1,
      scenarioNumberIterator: 0,

      // helper
      testTotalThreatSituations: [],
      totalCompetenceDimensions: 7,
      progressPercentage: 0,
      questionIndex: 0,
      questionView: false,
      threatAwareness: true,
      threatIdentification: false,
      showImpulse: true,
      showQuestionToImpulse: false,
      showFirstQuestionButton: true,
      showThreatImpulse: true,
      showPopUp: false,
      threatVectorIndex: 1,
      competenceTestResult: {},
      competenceTestPost: {
        participant: null,
        job_profile: null,
        threat_situation_score: [],
        competence_dimension_score: [],
      },
      profileID: 0,
    };
  },
  /**
   * A Vue component lifecycle method that is called after data changes and the DOM is re-rendered.
   * This method is used to adjust CSS variables and handle scroll behavior based on tab activation.
   *
   * It sets a CSS variable `--min-slide-height` based on the viewport height to control the minimum
   * height of slides. After DOM updates, it checks the current tab state and performs scrolling to
   * ensure that the correct tab content is in view.
   */
  updated() {
    const vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty("--min-slide-height", `${vh}px`);
    this.$nextTick(() => {
      // Scroll to the element
      if (this.$refs.scrollTarget && this.questionView) {
        this.$refs.scrollTarget.scrollIntoView();
      }
    });
  },
  /**
   * A Vue component lifecycle method that runs once the component is mounted to the DOM.
   * It asynchronously fetches different elemnts from competence tests from their respective stores.
   *
   * This method is critical for initializing the component with data required for rendering
   * job profiles and competence dimensions, fetched asynchronously from Vuex stores immediately
   * after the component has been rendered to the DOM.
   */
  async mounted() {
    this.loading = true;

    this.profileID = this.getProfileID();
    this.catchError(this.profileID)

    await this.getCompetenceTest();

    /*  await this.getThreatSituations(
      this.testSituations[0].threat_vector[this.threatVectorIndex - 1].id,
      this.profileID
    ); */
    // set total threatSituations of competence test
    this.testTotalThreatSituations = this.testSituations.length;

    // immer threatSituation 0 zunächst, da nur eine Handlungssituation pro ThreatVector modelliert wird
    this.activeThreatSituation =
      this.testSituations[this.threatVectorIndex - 1];

    // get alle TestSzenarien für den ersten ThreatVector
    await this.getTestItems(this.activeThreatSituation.id);

    await this.getAnswerOptions(this.activeQuestion.id);

    this.getScenarioNumber();

    this.totalQuestions =
      this.testTotalThreatSituations * this.testItems.length;
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
     * Toggles the visibility of the impulse scenario display in the UI.
     * This method switches the state of `showImpulse` between true and false each time it is called.
     */
    toggleScenario() {
      this.showImpulse = !this.showImpulse;
    },

    /**
     * Iterates through `activeAnswerOptions` to find  the scenario number for items where the answer rating is 2.
     * When a match is found, it sets the `impulseScenario` to the current scenario number.
     * This method finds the scenario that is the most threatining of the Threat Awareness question.
     */
    getScenarioNumber() {
      var i = 0;

      for (i = 0; i < this.activeAnswerOptions.length; i++) {
        this.scenarioNumberIterator += 1;

        if (this.activeAnswerOptions[i].answer_rating == 2) {
          this.impulseScenario = "Scenario " + this.scenarioNumberIterator;
          break;
        }
      }
    },
    /**
     * Triggers showing of the next or first question.
     *
     */
    showQuestion() {
      this.showQuestionToImpulse = true;
      this.showFirstQuestionButton = false;
    },
    /**
     * Initially sets the information on competence test results such as threat vectors and the job profile that will be tested.
     * Therfore utilizes some async calls to competence test store
     *
     */
    async getCompetenceTest() {
      

      this.testSituations = await this.competenceTestStore.getCompetenceTest(
        this.profileID
      );
      this.competenceTestResult.test_situations = JSON.parse(
        JSON.stringify(this.testSituations[0].threat_situations)
      );
      this.testSituations = this.testSituations[0].threat_situations;
      this.competenceTestResult.job_profile_id = this.profileID;
    },
    /**
     * Gets the threat situation related to the threat vector being tested an populates the competence test result initially with the threat situation.
     * Therfore utilizes some async calls to competence test store
     * @param {Object} threatVector The threatVector that is used to retrieve the threatSituations.

     */
    async getThreatSituations(threatVector) {
      this.threatSituations =
        await this.competenceTestStore.getThreatSituations(
          threatVector,
          this.profileID
        );
      /*    this.competenceTestResult.test_situations[
        this.threatVectorIndex - 1
      ].threat_situation = JSON.parse(JSON.stringify(this.threatSituations)); */
    },
    /**
     * Gets the test items related to the threat situation and threat vector being tested an populates the competence test result initially with the tests items to the threat situation.
     * Therfore utilizes some async calls to competence test store
     * Finally calls getImpulseItems
     * @param {Object} threatSituation The threatSituations that is used to retrieve the related test items.
     */
    async getTestItems(threatSituation) {
      this.testItems = await this.competenceTestStore.getTestItems(
        threatSituation
      );
      this.activeTestItem = this.testItems[0];
      // There may be multiple questions to a threat situation (NOT IMPLEMENTED)
      this.activeQuestion = this.activeTestItem.question_item[0];
      this.competenceTestResult.test_situations[
        this.threatVectorIndex - 1
      ].threat_vector.test_items = JSON.parse(JSON.stringify(this.testItems));
      if (this.activeTestItem.impulse_item) {
        this.getImpulseItems();
      }
    },
    /**
     * Gets the impulse items related to the test items retrieved before and sets these impulse items into an active array.
     * Therfore utilizes some async calls to competence test store
     */
    async getImpulseItems() {
      this.activeImpulseItems = await this.competenceTestStore.getImpulseItems(
        this.activeTestItem.impulse_item.id
      );
    },
    /**
     * Gets the answer options related to the active or current question and populates the competence test result initially with the answer options.
     * Therfore utilizes some async calls to competence test store
     * Finally calls getImpulseItems
     * @param {Object} question The active question.
     */
    async getAnswerOptions(question) {
      this.loading = true;
      this.activeAnswerOptions =
        await this.competenceTestStore.getAnswerOptions(question);
      this.competenceTestResult.test_situations[
        this.threatVectorIndex - 1
      ].threat_vector.test_items[this.testItemCounter].question_item[
        this.questionIndex
      ].answerOptions = JSON.parse(JSON.stringify(this.activeAnswerOptions));
      setTimeout(() => (this.loading = false), 500);
    },
    /**
     * Changes the answer option given by the user for single choice questions
     * Finally calls getImpulseItems
     * @param {Object} newAnswer The new answer emitted to the Test vue 
     * @param {Object} answerRating The rating of the answer (0 bad, 1 medium, 2 good)

     */
    changesAnswerOfSingleChoice(newAnswer, answerRating) {
      this.activeAnswer.userAnswer[0] = newAnswer;
      this.activeAnswer.answerQuality = answerRating;
    },
    /**
     * Changes the answer option given by the user for multiple choice questions
     * @param {Object} newAnswer The new answer emitted to the Test vue
     * @param {Array} answerRating The array including the rating of the answer (0 bad, 1 medium, 2 good)

     */
    changesAnswerOfMultipleChoice(newAnswer, answerRating) {
      if (!this.activeAnswer.userAnswer.includes(newAnswer)) {
        this.activeAnswer.userAnswer.push(newAnswer);
        this.answerRatingsByUser.push(answerRating);
      } else {
        this.activeAnswer.userAnswer.splice(
          this.activeAnswer.userAnswer.indexOf(newAnswer),
          1
        );
        this.answerRatingsByUser.splice(
          this.answerRatingsByUser.indexOf(answerRating),
          1
        );
      }

      // Check the contents of answerRatingsByUser
      if (this.answerRatingsByUser.every((rating) => rating === 2)) {
        this.activeAnswer.answerQuality = 2;
      } else if (this.answerRatingsByUser.some((rating) => rating === 2)) {
        this.activeAnswer.answerQuality = 1;
      } else {
        this.activeAnswer.answerQuality = 0;
      }
    },
    /**
     * Changes the answer option given by the user for sortable questions
     * Finally calls evaluateSortableQuestionAnswer
     * @param {Object} newAnswer The new answer emitted to the Test vue
     */
    changesAnswerOfSortable(newAnswer) {
      this.activeAnswer.userAnswer = [];
      var i;
      for (i = 0; i < newAnswer.length; i++) {
        this.activeAnswer.userAnswer.push(newAnswer[i].id);
      }
      this.evaluateSortableQuestionAnswer(newAnswer);
    },
    /**
     * Increaes the percentage in the test progress
     */
    increasePercentage() {
      this.contentProgress += 100 / this.totalQuestions;
    },
    /**
     * Calculates the points scored based on the quality of the answer given and sets the scored points to the competence test result.
     */
    calculatePoints() {
      var points = 0;
      if (this.activeAnswer.answerQuality == 2) {
        points = 2;
      } else if (this.activeAnswer.answerQuality == 1) {
        points = 1;
      } else {
        points = 0;
      }
      this.competenceTestResult.test_situations[
        this.threatVectorIndex - 1
      ].threat_vector.test_items[this.testItemCounter].question_item[
        this.questionIndex
      ].points = JSON.parse(JSON.stringify(points));
    },
    /**
     * Evaluates the answer quality for the sortable question type.
     * @param {Array} sortedAnswer An array including the answer options sorted by the user
     */
    evaluateSortableQuestionAnswer(sortedAnswer) {
      if (
        sortedAnswer[0].answer_rating == 2 &&
        sortedAnswer[sortedAnswer.length - 1].answer_rating == 0
      ) {
        this.activeAnswer.answerQuality = 2;
      } else if (
        sortedAnswer[0].answer_rating == 0 &&
        sortedAnswer[sortedAnswer.length - 1].answer_rating == 2
      ) {
        this.activeAnswer.answerQuality = 0;
      } else {
        this.activeAnswer.answerQuality = 1;
      }
    },
    /**
     * Prepares the generation of a POST object of the competence test result that is aligned with the database structure to save the result.
     * Is only relevant if an invitation token wwas provided
     */
    prepareCompetenceTestResult() {
      this.competenceTestPost.participant = this.$route.params.invitationToken;
      for (
        let i = 0;
        i < this.competenceTestResult.test_situations.length;
        i++
      ) {
        var totalPointsPerThreat = 0;
        let threatSituationScoreObj = {};
        let related_competence_dimension_scores = [];
        // threat situation index is always zero because by now there is only one threat situation for each threat vector modeled.
        this.competenceTestPost.job_profile =
          this.competenceTestResult.test_situations[i].job_profile.id;
        Object.assign(threatSituationScoreObj, {
          threat_situation: JSON.parse(
            JSON.stringify(this.competenceTestResult.test_situations[i].id)
          ),
          threat_vector: JSON.parse(
            JSON.stringify(
              this.competenceTestResult.test_situations[i].threat_vector.id
            )
          ),
        });

        this.competenceTestPost.threat_situation_score.push(
          threatSituationScoreObj
        );

        for (
          let j = 0;
          j <
          this.competenceTestResult.test_situations[i].threat_vector.test_items
            .length;
          j++
        ) {
          let competenceScoreObj = {};
          totalPointsPerThreat +=
            this.competenceTestResult.test_situations[i].threat_vector
              .test_items[j].question_item[0].points;
          Object.assign(competenceScoreObj, {
            competence_dimension: JSON.parse(
              JSON.stringify(
                this.competenceTestResult.test_situations[i].threat_vector
                  .test_items[j].competence_dimension.id
              )
            ),
            scoredPoints: JSON.parse(
              JSON.stringify(
                this.competenceTestResult.test_situations[i].threat_vector
                  .test_items[j].question_item[0].points
              )
            ),
          });

          related_competence_dimension_scores.push(
            JSON.parse(JSON.stringify(competenceScoreObj))
          );

          if (i == 0) {
            this.competenceTestPost.competence_dimension_score.push(
              JSON.parse(JSON.stringify(competenceScoreObj))
            );
          } else {
            this.competenceTestPost.competence_dimension_score[
              j
            ].scoredPoints +=
              this.competenceTestResult.test_situations[
                i
              ].threat_vector.test_items[j].question_item[0].points;
          }

          if (
            j ==
            this.competenceTestResult.test_situations[i].threat_vector
              .test_items.length -
              1
          ) {
            Object.assign(threatSituationScoreObj, {
              scoredPoints: totalPointsPerThreat,
              related_competence_dimension_scores:
                related_competence_dimension_scores,
            });
          }
        }
      }
    },

    /**
     * The main method in Test.vue. Is called whenever the user clicks 'Weiter'.
     *
     */
    async continueTest() {
      this.showPopUp = false;

      if (
        this.activeAnswer.userAnswer.length == 0 &&
        (this.activeQuestion.type == 1 || this.activeQuestion.type == 2)
      ) {
        this.showPopUp = true;
        setTimeout(() => (this.showPopUp = false), 3000);
      } else {
        this.increasePercentage();

        // save user answer of current QuestionItem nach jedem Weiter Klick
        this.contentProgress += this.progressPercentage;

        if (
          this.activeQuestion.type == 3 &&
          this.activeAnswer.userAnswer.length == 0
        ) {
          this.changesAnswerOfSortable(this.activeAnswerOptions);
        }
        this.competenceTestResult.test_situations[
          this.threatVectorIndex - 1
        ].threat_vector.test_items[this.testItemCounter].question_item[
          this.questionIndex
        ].userAnswer = JSON.parse(JSON.stringify(this.activeAnswer));
        this.calculatePoints();
        this.activeAnswer.userAnswer = [];
        this.activeAnswer.answerQuality = 0;

        if (!this.questionView) {
          // questionview is fase when the competence dimension related to a test scneario is Threat Awareness.

          this.questionIndex = 0;
          this.testItemCounter += 1;

          this.activeTestItem = this.testItems[this.testItemCounter];
          this.activeQuestion = this.activeTestItem.question_item[0];

          this.questionView = true;
          this.scenarioNumber = this.scenarioNumberIterator - 1;

          // Wenn Impuls dargestellt wird und erster ThreatVector, calle die Antworten zur nächsten Frage
          await this.getAnswerOptions(this.activeQuestion.id);

          // Wenn Impuls dargestellt wird und es einen vorherigen ThreatVector gab, hole die Antworten zur nächsten Frage
          // sonst schau ob es noch eine Frage zu dem Testszenario gibt
        } else {
          // set activeAnswer to 0 for next questiom

          // increment questionIndex
          this.questionIndex += 1;
          // wenn ja, ändere die aktuell aktive Frage
          if (this.questionIndex < this.activeTestItem.question_item.length) {

            this.activeQuestion =
              this.activeTestItem.question_item[this.questionIndex];
            await this.getAnswerOptions(this.activeQuestion.id);

            // sonst geh in das nächste Testszenario
          } else {
            this.loading = true;

            this.questionIndex = 0;
            this.testItemCounter += 1;

            // schau ob es ein weiteres Testszenario zum ThreatVector gibt
            if (this.testItemCounter < this.testItems.length) {
              this.activeTestItem = this.testItems[this.testItemCounter];
              if (
                this.activeTestItem.competence_dimension.id != 1 &&
                this.activeTestItem.competence_dimension.id != 2
              ) {
                this.threatAwareness = false;
                this.showImpulse = false;
              }

              this.activeQuestion = this.activeTestItem.question_item[0];
              await this.getAnswerOptions(this.activeQuestion.id);
              // wenn nicht gehe zum nächsten ThreatVector
            } else {
              this.threatVectorIndex += 1;
              this.testItemCounter = 0;
              this.scenarioNumber = -1;
              this.scenarioNumberIterator = 0;
              this.showQuestionToImpulse = false;
              this.showFirstQuestionButton = true;

              this.activeEmailImpuses = [];
              this.activeImageImpulses = [];
              // solange es einen nächsten ThreatVector gibt, wiederhole die Prozedur
              if (this.threatVectorIndex - 1 < this.testSituations.length) {
                this.questionView = false;
                this.threatAwareness = true;
                this.showImpulse = true;

              
                // IMMER threatSituation 0 zunächst, da nur eine Handlungssituation pro ThreatVector modelliert wird
                this.activeThreatSituation =
                  this.testSituations[this.threatVectorIndex - 1];

                // get alle TestSzenarien für den ersten ThreatVector
                await this.getTestItems(this.activeThreatSituation.id);


                await this.getAnswerOptions(this.activeQuestion.id);
                this.getScenarioNumber();
                this.testItemCounter = 0;
                // wenn der letzte ThreatVector erreicht worden ist, beende den Test
              } else {
                this.competenceTestStore.setCompetenceTestResult(
                  this.competenceTestResult
                );

                this.prepareCompetenceTestResult();

                this.competenceTestStore.endTest();
                // only if invitaionToken was specified, else do not save the test result
                if (this.$route.params.invitationToken) {
                  await this.campagneStore.postCompetenceTestResults(
                    this.competenceTestPost
                  );
                }

                this.$router.push({
                  name: "Dashboard",
                });
              }
            }
          }
        }
      }
    },
  },
};
</script>

<style scoped>
.fade-enter-from {
  opacity: 0;
}
.fade-enter-active {
  transition: all 2s ease;
}
.slide {
  min-height: var(--min-slide-height, 100vh);
}
</style>
