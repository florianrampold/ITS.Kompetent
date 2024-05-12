<template>
  <template v-if="loading">
    <spinner></spinner>
  </template>
  <template v-else>
    <div class="desktop">
      <Hero
        ><template #title>
          <h1 class="main-heading">
            <span class="text-primary xl:inline"
              >Herzlichen Glückwunsch! <br />
            </span>
            {{ " " }}
            <span class="text-secondary xl:inline"
              >Sie haben den ITS-Kompetenztest erfolgreich abgeschlossen</span
            >
          </h1></template
        >
        <template #content>
          <p
            class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
          >
            Auf den nächsten Seiten werden Ihnen zunächst Ihre Ergebnisse
            präsentiert. Sie haben dann die Möglichkeit sich diese an Ihre
            persönliche Email-Adresse senden zu lassen. Wenn Sie darüberhinaus
            Interesse daran haben, im Detail zu verstehen wie Ihre ITS-Kompetenz
            gemessen wurde, können Sie sich optional Ihre detailliierten
            Ergebnisse mit Erklärungen anschauen.
            <br />
            <br />
            Es besteht außerdem die Möglichkeit sich Ihre Ergebnisse aus dem
            ITS-Kompetenztest für Ihr gewähltes ITS-Anforderungsprofil als PDF
            zu exportieren.
          </p></template
        >
        <template #buttons>
          <div
            class="flex flex-row justify-center items-center lg:items-start lg:justify-start"
          >
            <div
              class="flex justify-center items-center lg:items-start lg:justify-start"
            >
              <a
                class="w-full cursor-pointer flex justify-between font-semibold items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-primary hover:bg-primaryAccent mt-12 md:py-4 md:text-lg md:px-10"
                @click="exportResultsToPDF()"
              >
                Ergebnisse abrufen
                <CloudArrowDownIcon class="ml-4 w-8 h-8"></CloudArrowDownIcon>
              </a>
            </div>
          </div>
        </template>

        <template #progress>
          <div
            class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10 lg:gap-20 xl:gap-40"
          >
            <metric
              metric="Erreichbare Punkte"
              :score="totalPossiblePoints"
            ></metric>
            <metric
              metric="Ihre erreichten Punkte"
              :score="competenceTestResult.totalPointsScored"
            ></metric>
            <metric
              metric="Getestete Bedrohungszenarien"
              :score="threatEvent.length"
            ></metric>
          </div>
        </template>
      </Hero>

      <div class="gradient-background">
        <div class="standard-container py-20">
          <explanation-card>
            <template #heading>Was sind ITS-Bedrohungen?</template>
            <template #title
              >ITS-Bedrohungen setzen sich aus ITS-Bedrohungsbereichen und
              ITS-Bedrohungsereignissen zusammen.</template
            >
            <template #content>
              <p class="text-gray-500">
                Als
                <span class="text-secondary font-semibold">
                  ITS-Bedrohungsbereich </span
                >definieren wir jene möglichen Unternehmenswerte (z. B.
                E-Mail-Programm), auf welche die unterschiedlichen
                ITS-Bedrohungsereignisse (z. B. Phishing-Attacke) abzielen
                können.
              </p>
              <p class="text-gray-500">
                Die zweite Dimension
                <span class="text-secondary font-semibold">
                  ITS-Bedrohungsereignis
                </span>
                beinhaltet wiederum Bedrohungsquellen, die potenziell einen
                Schaden an den zuvor erläuterten ITS-Bedrohungsbereichen
                verursachen können.
              </p>
              <p />
              <div class="grid grid-cols-2">
                <div class="mt-5">
                  <h2 class="font-semibold text-primary mb-4">
                    Beispielhafte ITS-Bedrohungsbereiche:
                  </h2>
                  <ul class="pl-4 list-disc text-gray-500">
                    <li>Laptop</li>
                    <li>Mobiltelefon</li>
                    <li>Buchungssystem</li>
                  </ul>
                </div>
                <div>
                  <div class="mt-5">
                    <h2 class="font-semibold text-primary mb-4">
                      Beispielhafte ITS-Bedrohungsereignisse:
                    </h2>
                    <ul class="pl-4 list-disc text-gray-500">
                      <li>Social Engineering</li>
                      <li>Phishing</li>
                      <li>Malware</li>
                    </ul>
                  </div>
                </div>
              </div>
            </template>
            <template #image>
              <img
                src="@/assets/bedrohungen.png"
                class="w-full exportImages"
                alt="Sample image"
              />
            </template>
          </explanation-card>
        </div>
      </div>
      <div class="bg-white pt-20 pb-10">
        <div class="standard-container">
          <div>
            <h1
              class="text-2xl tracking-tight font-extrabold text-primary sm:text-3xl md:text-4xl mb-10"
            >
              Relevante ITS-Bedrohungen für Ihr ITS-Anforderungsprofil
            </h1>
          </div>
          <div class="flex flex-row justify-center items-center">
            <div
              class="border-b-4 rounded-lg w-14 border-secondary mb-10"
            ></div>
          </div>
          <div class="flex flex-row justify-center items-center">
            <p
              class="mt-3 text-base mb-20 text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
            >
              Wir haben Ihre ITS-Kompetenz anhand der folgenden ITS-Bedrohungen
              getestet.
            </p>
          </div>

          <div
            v-if="competenceTestResult.test_situations"
            class="grid grid-cols-1 sm:grid-cols-2 gap-10 lg:gap-20 xl:gap-40 mb-40"
          >
            <div
              v-for="threat in competenceTestResult.test_situations"
              :key="threat"
            >
              <Accordion>
                <template #title
                  >{{ threat.threat_vector.threatVectorText }}
                </template>

                <template #content>{{
                  threat.threat_vector.threat_vector_description
                }}</template>
              </Accordion>
            </div>
          </div>
        </div>
      </div>
      <div class="page-background">
        <div class="standard-container">
          <h1
            class="text-2xl tracking-tight font-extrabold text-primary text-center sm:text-3xl md:text-4xl mb-10"
          >
            Statistiken zu relevanten ITS-Bedrohungen
          </h1>
          <div class="flex flex-row justify-center items-center">
            <div
              class="border-b-4 w-14 rounded-lg border-secondary mb-20"
            ></div>
          </div>

          <div class="flex flex-col items-center justify-center mb-10">
            <!--  <p
              ref="threatSummary"
              class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
              :innerHTML="setThreatSummary()"
            ></p> -->

            <p
              class="mt-3 text-base font-semibold text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
              :innerHTML="setThreatMotivationStatement()"
            ></p>
          </div>
          <div
            class="grid grid-cols-1 gap-10 lg:gap-20 xl:gap-40 mb-40"
          >
            <DoughnutChart
              :chart-data="chartDataAllThreats"
              :chart-options="chartOptionsAllThreats"
              title="Erreichte Punktzahl über alle ITS-Bedrohungen"
            />
          </div>
        </div>
      </div>
      <div class="gradient-background-secondary">
        <div class="standard-container py-20">
          <explanation-card>
            <template #heading>Was sind ITS-Kompetenzen?</template>
            <template #title
              >Unter ITS-Kompetenz verstehen wir die bei Individuen verfügbaren
              (oder erlernbaren) kognitiven Fähigkeiten und Fertigkeiten, um im
              Berufsalltag IT-sicher zu handeln, sowie die damit verbundenen
              motivationalen und sozialen Bereitschaften und Fähigkeiten, um in
              variablen Situationen erfolgreich und verantwortungsvoll eine
              Gefahr abwenden bzw. bewältigen zu können (Weinert 2001). Hierbei
              konnten 7 Dimensionen identifiziert werden, die rechts agbildet
              sind.</template
            >

            <template #image>
              <img
                :src="require('@/assets/kompetenzdimensionen.png')"
                class="w-full exportImages"
                alt="Sample image"
              />
            </template>
          </explanation-card>
        </div>
      </div>
      <div class="bg-white pt-20 pb-10">
        <div class="standard-container">
          <h1
            class="text-2xl tracking-tight font-extrabold text-primary text-center sm:text-3xl md:text-4xl mb-10"
          >
            ITS-Kompetenzen für Ihr ITS-Anforderungsprofil
          </h1>

          <div class="flex flex-row justify-center items-center">
            <div
              class="border-b-4 w-14 rounded-lg border-secondary mb-40"
            ></div>
          </div>
          <div
            v-if="competenceTestResult.test_situations"
            class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-10 lg:gap-20 xl:gap-40 mb-40"
          >
            <div
              v-for="threat in competenceTestResult.test_situations[0]
                .threat_vector.test_items"
              :key="threat"
            >
              <Accordion>
                <template #title
                  >{{ threat.competence_dimension.dimension_name }}
                </template>

                <template #content>{{
                  threat.competence_dimension.dimension_description
                }}</template>
              </Accordion>
            </div>
          </div>
        </div>
      </div>
      <div class="page-background">
        <div class="standard-container">
          <h1
            class="text-2xl tracking-tight font-extrabold text-primary text-center sm:text-3xl md:text-4xl mb-10"
          >
            Statistiken zu relevanten ITS-Kompetenzen
          </h1>
          <div class="flex flex-row justify-center items-center">
            <div
              class="border-b-4 w-14 rounded-lg border-secondary mb-20"
            ></div>
          </div>
          <div class="flex flex-col items-center justify-center mb-10">
            <p
              class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
            >
              Jede ITS-Bedrohung wurde über 7 verschiedene
              ITS-Kompetenzdimensionen getestet. Im folgenden erhalten Sie einen
              Überblick, wie gut sie sich in den einzelnen
              ITS-Kompetenzdimensionen geschlagen haben.
            </p>
            <p
              v-if="goodResults != 0"
              class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
            >
              {{ competenceScoreGood }}
            </p>
            <p
              v-if="mediumResults != 0"
              ref="competenceScoreMedium"
              class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
            >
              {{ competenceScoreMedium }}
            </p>
            <p
              class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
            >
              {{ competenceScoreBad }}
            </p>
          </div>
          <div class="grid grid-cols-1 lg:grid-cols-6 mb-40">
            <BarChart
              class="lg:col-start-2 lg:col-span-4"
              chart-id="bar-chart2"
              :chart-data="chartDataPerCompetenceDimension"
              :chart-options="chartOptionsPerCompetenceDimension"
              title="Erreichte Punktzahl pro ITS-Kompetenzdimension"
            />
          </div>
        </div>
      </div>
      <div class="bg-white pt-20 pb-10">
        <div class="standard-container">
          <h1
            class="text-2xl tracking-tight font-extrabold text-primary text-center sm:text-3xl md:text-4xl mb-10"
          >
            Zusammenfassung & Empfehlungen
          </h1>
          <div class="flex flex-row justify-center items-center">
            <div
              class="border-b-4 w-14 rounded-lg border-secondary mb-10"
            ></div>
          </div>
          <div class="flex flex-row justify-center items-center">
            <p
              class="mt-3 text-base mb-20 text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
            >
              Zum Schluss zeigen wir Ihnen Ihr Ergebnis pro ITS-Bedrohung und
              ITS-Kompetenzdimension an.
            </p>
          </div>
          <recommendation-card
            :competence-dimensions="chartDataPerCompetenceDimension"
            :threat-vectors="chartDataPerThreat"
          ></recommendation-card>
        </div>
      </div>
    </div>
    <div class="page-background pb-10">
      <div class="standard-container">
        <div class="flex mt-10 justify-center items-center">
          <button
            class="w-40 lg:transform lg:hover:scale-105 lg:duration-500 bg-primary text-white lg:bg-white lg:border-primary border-2 border-primary lg:text-primary my-2 py-1 px-4 mx-2 rounded lg:hover:text-white lg:hover:bg-primary"
            @click="navigateToTrainings()"
          >
            Weiter
          </button>
        </div>
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
</template>

<script>
import Hero from "@/components/base/Hero.vue";
import Metric from "@/components/dashboard/Metric.vue";
import Accordion from "@/components/base/Accordion.vue";
import ExplanationCard from "@/components/dashboard/ExplanationCard.vue";
import BarChart from "@/components/dashboard/BarChart.vue";
import DoughnutChart from "@/components/dashboard/DoughnutChart.vue";
import RecommendationCard from "@/components/dashboard/RecommendationsCard.vue";
import { useCompetenceTestStore } from "@/store/CompetenceTestStore.js";
import { useJobProfileStore } from "@/store/JobProfileStore.js";
import { mapState } from "pinia";
import DOMPurify from "dompurify";

export default {
  components: {
    Hero,
    Metric,
    Accordion,
    BarChart,
    DoughnutChart,
    ExplanationCard,
    RecommendationCard,
  },

  setup() {
    const competenceTestStore = useCompetenceTestStore();

    return { competenceTestStore };
  },

  data() {
    return {
      // an object to store the competence test result
      competenceTestResult: {},

      threatEvent: [],
      threatEventsMapped: [],
      activeStep: 3,
      loading: false,
      // the maximum points
      totalPossiblePoints: 0,
      // the maximum points per security threat vector (usually 14)
      totalPossiblePointsThreat: 0,
      pointScoredThreats: 0,
      // get number
      numberOfCompetenceDimensions: 7,
      totalThreatVectors: 0,
      maxScorePerItem: 2,
      pointsScoredPerThreat: [],
      pointsScoredPerCompetenceDimension: [],
      // vaiables to create the charts
      chartDataPerThreat: {},
      chartDataAllThreats: {},
      chartOptionsPerThreat: [],
      chartOptionsAllThreats: [],
      chartDataPerCompetenceDimension: [],
      chartOptionsPerCompetenceDimension: [],

      competenceSummary: "",
      threatSummary: "",
      threatMotivationStement: "",
      competenceScoreSummary: "",
      competenceScoreGood: "",
      competenceScoreMedium: "",
      competenceScoreBad: "",
      goodResults: [],
      mediumResults: [],
      success: "",
      popupType: "",
      popupTitle: "",
      popupContent: "",
      showFailurePopUp: false,
      showSuccessPopUp: false,
    };
  },
  /**
   * A Vue component lifecycle method that runs once the component is mounted to the DOM.
   * It basically fecthes the data on scored points and prepares all chart data that is displayed including the results of the individual tst result.
   */
  mounted() {
    this.loading = true;

    this.competenceTestResult = this.getCompetenceTestResult();

    if (Object.keys(this.competenceTestResult).length == 0) {
      this.$router.push("/");
      return;
    }
    this.calculateBasePoints();
    this.populateCompetenceScore();
    this.populateThreatVectors();
    this.populatePointsTestResult();
    this.setUpThreatBarChart(
      this.threatEventsMapped,
      this.pointsScoredPerThreat
    );
    this.setUpCompetenceBarChart(
      this.competenceTestResult.competenceDimensionScore.label,
      this.competenceTestResult.competenceDimensionScore.score
    );
    this.setUpDoughnutChart();
    this.setThreatSummary();
    this.setCompetenceScores();

    setTimeout(() => (this.loading = false), 500);
  },
  methods: {
    /*   async getCompetenceDimensions() {
      this.competenceDimensions =
        await CompetenceTestService.getCompetenceDimensions();
      this.loading = false;
    }, */

    ...mapState(useJobProfileStore, ["getProfile"]),

    ...mapState(useCompetenceTestStore, [
      "getCompetenceTestResult",
      "getCompetenceTestPost",
    ]),

    /**
     * Routes to training landing page
     *
     */
    navigateToTrainings() {
      this.$router.push({
        name: "TrainingsLanding",
      });
    },
    /**
     * Generates a management report including the aggregated results of participants of the competence tests.
     * @throws {Error} Throws an error when the PDF cannot be downloaded
     */
    async exportResultsToPDF() {
      this.loading = true;
      try {
        const response =
          await this.competenceTestStore.generateIndividualReport(
            this.competenceTestResult
          );

        const file = new Blob([response.data], { type: "application/pdf" });

        // Create a URL for the blob
        const fileURL = URL.createObjectURL(file);

        window.open(fileURL, "_blank");
        setTimeout(() => URL.revokeObjectURL(fileURL), 100);

        const link = document.createElement("a");
        link.href = fileURL;
        link.setAttribute("download", "report.pdf");
        document.body.appendChild(link);
        link.click();

        // Trigger download
        this.popupType = "success";
        this.popupTitle = "PDF herunterladen";
        this.popupContent = "Eine PDF wurde erstellt und heruntergeladen";
        this.showSuccessPopUp = true;
      } catch (error) {
        console.log(error);
        console.error("Could not download PDF: ", error);
        this.popupType = "danger";
        this.popupTitle = "PDF herunterladen";
        this.popupContent = "Eine PDF konnte nicht heruntergeladen werden.";
        this.showFailurePopUp = true;
      }
      this.loading = false;
    },
    /**
     * This method generates html strings that give an evaluation about the reached scores per competence dimensions.
     * It distiguishes between bad (<=33%), medium (33 - 66%) and good (>66%) results
     */
    setCompetenceScores() {
      var badResults = [];

      var i;
      for (
        i = 0;
        i < this.chartDataPerCompetenceDimension.datasets[0].data.length;
        i++
      ) {
        if (this.chartDataPerCompetenceDimension.datasets[0].data[i] > 50) {
          this.goodResults.push(
            ` ${this.chartDataPerCompetenceDimension.labels[i]}`
          );
        } else if (
          this.chartDataPerCompetenceDimension.datasets[0].data[i] == 0
        ) {
          badResults.push(` ${this.chartDataPerCompetenceDimension.labels[i]}`);
        } else {
          this.mediumResults.push(
            ` ${this.chartDataPerCompetenceDimension.labels[i]}`
          );
        }
      }
      this.competenceScoreGood = `Ihre Ergebnisse sind sehr gut in den ITS-Kompetenzdimensionen: ${this.goodResults}`;
      this.competenceScoreMedium = `In den folgenden ITS-Kompetenzdimensionen konnten sie befriedigende Ergebnisse erzielen: ${this.mediumResults}`;
      this.competenceScoreBad = `In diesen ITS-Kompetenzdimensionen besteht das größte Förderungspotential:  ${badResults} `;
    },
    /**
     * Sets a summary text for the competence dimensions
     */
    setCompetenceSummary() {
      this.competenceScoreSummary = `Jede ITS-Bedrohung wurde über 7 verschiedene ITS-Kompetenzdimensionen getestet. `;
    },
    /**
     * Evaluates the score reached over all testest security threat vectors.
     */
    setThreatSummary() {
      this.threatSummary = `In dem ITS-Kompetenztest für das ITS-Anforderungsprofil ${this.getProfile()} haben wir Ihr ITS-Wissen für eine spezifische ITS-Bedrohung getestet. Eine ITS-Bedrohung besteht immer aus einem Bedrohunsgsereignis und einem Bedrohungsbereich.
       Für die ITS-Bedrohung ${
         this.threatEventsMapped[0]
       } konnten Sie <strong>${
        this.pointsScoredPerThreat[0]
      }</strong> % der Punkte erzielen.`;
      return DOMPurify.sanitize(this.threatSummary);
    },
    setThreatMotivationStatement() {
      if (this.pointsScoredPerThreat[0] >= 66) {
        this.threatMotivationStement = `Super! Sie sind sehr kompetent im Umgang mit den ITS-Bedrohungen für Ihr ITS-Anforderungsprofil. Aber was bedeutet ITS-Kompetenz eigentlich? Dies erfahren Sie auf der nächsten Seite.`;
      } else if (this.pointsScoredPerThreat[0] <= 33) {
        this.threatMotivationStement = `Vielen Dank für Ihre Teilnahme. Sie besitzen bereits ein Grundverständnis für den Umgang mit ITS-Bedrohungen. An einigen Stellen fehlt es Ihnen aber noch an ITS-Kompetenz. Aber was bedeutet ITS-Kompetenz eigentlich? Dies erfahren Sie auf der nächsten Seite.`;
      } else {
        this.threatMotivationStement = `Super! Sie sind weitestgehend kompetent im Umgang mit den ITS-Bedrohungen für Ihr ITS-Anforderungsprofil. Aber was bedeutet ITS-Kompetenz eigentlich? Dies erfahren Sie auf der nächsten Seite.`;
      }
      return DOMPurify.sanitize(this.threatMotivationStement);
    },
    /**
     * Sets total possible points over all security threat vectors
     * Sets total possible points per threat
     */
    calculateBasePoints() {
      this.totalThreatVectors =
        this.competenceTestResult.test_situations.length;
      this.totalPossiblePoints =
        this.totalThreatVectors *
        this.numberOfCompetenceDimensions *
        this.maxScorePerItem;
      this.totalPossiblePointsThreat =
        this.maxScorePerItem * this.numberOfCompetenceDimensions;
    },
    /**
     * Sets inital scores per competence dimension
     */
    populateCompetenceScore() {
      this.competenceTestResult.competenceDimensionScore = {
        label: [
          "Threat Awareness",
          "Threat Identification",
          "Threat Impact Assessment",
          "Tactic Choice",
          "Tactic Justification",
          "Tactic Mastery",
          "Tactic Check & Follow Up",
        ],
        score: [0, 0, 0, 0, 0, 0, 0],
      };
    },
    /**
     * Sets threat area and threat event objects for each threat vector
     * Concatenates the threat are and threat event name to a specific threat vector text and appends the result to the comoetence test result
     * Sets total possible points per threat
     */
    populateThreatVectors() {
      var i = 0;
      for (i = 0; i < this.competenceTestResult.test_situations.length; i++) {
        var threatEventText = "";
        var threatAreaText = "";

        threatEventText =
          this.competenceTestResult.test_situations[i].threat_vector
            .threat_event.event_name;

        threatAreaText =
          this.competenceTestResult.test_situations[i].threat_vector.threat_area
            .area_name;

        const threatVectorText = threatEventText.concat(" / ", threatAreaText);
        const obj = { threatVectorText };
        this.threatEvent.push(obj);
        this.competenceTestResult.test_situations[
          i
        ].threat_vector.threatVectorText = this.threatEvent[i].threatVectorText;
      }
    },
    /**
     * Sets all scores: First it iterates over all threat vectors and inside over each competence dimension.
     * Stores the totalPoints scored over all threat vectors and competence dimensions
     * Stores the points scored per threat vector
     * Finally populates competenceDimensionScore per threat vector
     */
    populatePointsTestResult() {
      var i = 0;
      var totalPoints = 0;
      var tempScore = 0;
      for (i; i < this.totalThreatVectors; i++) {
        var j = 0;

        for (j; j < this.numberOfCompetenceDimensions; j++) {
          tempScore =
            this.competenceTestResult.test_situations[i].threat_vector
              .test_items[j].question_item[0].points;

          totalPoints += tempScore;

          if (j == 0) {
            this.competenceTestResult.test_situations[i].pointsScored =
              tempScore;
          } else {
            this.competenceTestResult.test_situations[i].pointsScored +=
              tempScore;
          }
          this.competenceTestResult.competenceDimensionScore.score[j] +=
            tempScore;
        }
      }
      this.competenceTestResult.totalPointsScored = totalPoints;
      this.threatEventsMapped = this.threatEvent.map(function (threat) {
        return threat.threatVectorText;
      });
      var k = 0;
      for (i; i < this.totalThreatVectors; i++) {
        this.pointsScoredPerThreat.push(
          Math.round(
            (this.competenceTestResult.test_situations[k].pointsScored /
              this.totalPossiblePointsThreat) *
              100
          )
        );
      }
    },
    /**
     * Sets up a bar chart where each bar represents the percentage score for a threat vector.
     *
     * @param {object} label The labels for the threat vector text
     * @param {object} data The percentgae score per threat vector

     */
    setUpThreatBarChart(label, data) {
      this.chartDataPerThreat = {
        labels: label,
        datasets: [
          {
            data: data,
            backgroundColor: "#EB5757",
            fill: true,
          },
        ],
      };
      this.chartOptionsPerThreat = {
        responsive: true,
        plugins: {
          title: {
            display: false,
            text: "Erreichte Punktzahl über Bedrohungsereignisse (in %)",
            font: {
              size: 20,
            },
          },
          legend: {
            display: false,
          },
        },
        scales: {
          x: {
            type: "category", // Explicitly set type to category
            grid: {
              display: false,
            },
            ticks: {
              font: {
                size: 12,
              },
            },
            title: {
              display: true,
              text: "ITS-Bedrohung",
              font: {
                size: 20,
              },
            },
          },
          y: {
            beginAtZero: true,
            min: 0,
            max: 100,
            grid: {
              display: false,
            },
            ticks: {
              font: {
                size: 12,
              },
            },
            title: {
              display: true,
              text: "Score in %",
              font: {
                size: 20,
              },
            },
          },
        },
        maintainAspectRatio: false,
        animations: {
          tension: {
            duration: 2000,
            easing: "linear",
            from: 1,
            to: 0,
            loop: true,
          },
        },
      };
    },
    /**
     * Sets up a bar chart where each bar represents the percentage score for a competence dimension.
     * Shows the aggregated score over all threat vectors.
     * Gets called in mounted hook
     * @param {object} label The labels for each competence dimension
     * @param {object} data The percentagee score per competence dimension over all threat vectors

     */
    setUpCompetenceBarChart(label, data) {
      var i = 0;
      var competenceScoreTemp = [];

      for (i = 0; i < data.length; i++) {
        competenceScoreTemp[i] = Math.round(
          (data[i] / (this.threatEvent.length * 2)) * 100
        );
      }
      this.chartDataPerCompetenceDimension = {
        labels: label,
        datasets: [
          {
            data: competenceScoreTemp,
            backgroundColor: "#EB5757",
            fill: true,
          },
        ],
      };
      this.chartOptionsPerCompetenceDimension = {
        responsive: true,
        plugins: {
          title: {
            display: false,
            text: "Erreichte Punktzahl über Bedrohungsereignisse (in %)",
            font: {
              size: 20,
            },
          },
          legend: {
            display: false,
          },
        },
        scales: {
          y: {
            beginAtZero: true,
            min: 0,
            max: 100,
            grid: {
              display: false,
            },
            ticks: {
              font: {
                size: 12,
              },
            },
            title: {
              display: true,
              text: "Score in %",
              font: {
                size: 20,
              },
            },
          },
          x: {
            grid: {
              display: false,
            },
            ticks: {
              font: {
                size: 16,
              },
            },
            title: {
              display: true,
              text: "ITS-Kompetenzdimension",
              font: {
                size: 20,
              },
            },
          },
        },
        maintainAspectRatio: false,
        animations: {
          tension: {
            duration: 2000,
            easing: "linear",
            from: 1,
            to: 0,
            loop: true,
          },
        },
      };
    },
    /**
     * Sets up a doughnut chart where one tile of the doughnut represents the percentage of correctly scored points and the other tile represents the percentage of wrongly scored.
     * Gets called in mounted hook
     */
    setUpDoughnutChart() {
      var i = 0;
      for (i; i < this.totalThreatVectors; i++) {
        this.pointsScoredPerThreat.push(
          Math.round(
            (this.competenceTestResult.test_situations[i].pointsScored /
              this.totalPossiblePointsThreat) *
              100
          )
        );
      }

      this.chartDataAllThreats = {
        labels: ["Korrekt beantwortet", "Falsch beantwortet"],
        datasets: [
          {
            data: [
              Math.round(
                (this.competenceTestResult.totalPointsScored /
                  this.totalPossiblePoints) *
                  100
              ),
              Math.round(
                ((this.totalPossiblePoints -
                  this.competenceTestResult.totalPointsScored) /
                  this.totalPossiblePoints) *
                  100
              ),
            ],
            backgroundColor: ["#303e7a", "#EB5757"],
          },
        ],
      };
      this.chartOptionsAllThreats = {
        plugins: {
          title: {
            display: false,
            text: "Erreichte Punktzahl über alle Bedrohungsereignisse (in %)",
            font: {
              size: 20,
            },
          },
          legend: {
            display: true,
            position: "bottom",
            labels: {
              font: {
                size: 20,
                padding: 50,
              },
            },
          },
        },
        maintainAspectRatio: false,
        responsive: true,
        animations: {
          tension: {
            duration: 2000,
            easing: "linear",
            from: 1,
            to: 0,
            loop: true,
          },
        },
      };
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
