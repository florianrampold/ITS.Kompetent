<template>
  <template v-if="isLoading">
    <spinner></spinner>
    <!-- here use a loaded you prefer -->
  </template>
  <template v-else>
    <Hero
      ><template #title>
        <div
          class="flex justify-center items-center lg:items-start lg:justify-start"
        >
          <h1 class="main-heading">
            <span class="text-primary font-semibold"
              >Ergebnisse zu<br />
            </span>
            {{ " " }}
            <span class="text-secondary xl:inline"
              >den ITS-Kompetenztests</span
            >
          </h1>
        </div>
      </template>
      <template #content>
        <div
          class="flex justify-center items-center lg:items-start lg:justify-start"
        >
          <p
            class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl md:mt-5 md:text-xl lg:mx-0"
          >
            In dieser Ansicht erhalten Sie Statistiken zu den Ergebnissen aus
            dem ITS-Kompetenztest Ihrer Mitarbeiter*innen. Sie können in der
            Navigation weiter unten auf dieser Seite die Ergebnisse nach
            ITS-Anforderungsprofilen filtern. Wenn Sie mehr Informationen zu dem
            Ablauf und der Auswertung der ITS-Kompetenztests erfahren möchten,
            wechseln Sie die Ansicht zum FAQ.
            <br />
            <br />
            Zudem habe Sie die Möglichkeit sich die Ergebnisse als
            Management-Report PDF-Datei erzeugen zu lassen. Ebenso können Sie
            die ITS-Trainingsempfehlungen als Excel-Datei exportieren.

            <br />
            <br />
            <strong>Achtung:</strong> In der Einstellung, die Sie vorgenommen haben, werden Ihnen erst
            aggregierte Daten zu einem ITS-Anforderungsprofil angezeigt, wenn
            mindestens {{ securityDisplayThreshold }} Mitarbeiter*innen aus
            diesem ITS-Anforderungsprofil an der Kampagne teilgenommen haben.
            <br/>   <br/>
            Sobald die Mindestanzahl erreicht ist, können Sie sich dazu
            entscheiden die Kampagne zu beenden.
          </p>
        </div>
      </template>

      <template #buttons>
        <div
          v-if="
            totalNumberOfParticipants >= securityDisplayThreshold &&
            campagneStore.campagneEnded
          "
          class="flex flex-row justify-center items-center lg:justify-start"
        >
          <div class="flex mr-4 flex-col">
            <a
              class="w-full cursor-pointer flex justify-between font-semibold items-center justify-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-secondary hover:bg-secondaryAccent mt-12 md:py-4 md:text-lg md:px-10"
              @click="exportManagementReport()"
            >
              <span> Report abrufen </span>
              <CloudArrowDownIcon class="ml-4 w-8 h-8"></CloudArrowDownIcon>
            </a>
          </div>
          <div
            class="flex ml-4 flex-col justify-center items-center lg:items-start lg:justify-start"
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
        <div
          v-if="!campagneStore.campagneEnded"
          class="flex flex-row justify-center items-center lg:justify-start"
        >
          <div class="flex mr-4 flex-col">
            <a
              class="w-full cursor-pointer flex justify-between font-semibold items-center justify-center px-6 py-3 border border-transparent text-base font-medium rounded-md text-white bg-secondary hover:bg-secondaryAccent mt-12 md:py-4 md:text-lg md:px-10"
              @click="openEndCampagneModal()"
            >
              <span> Kampagne beenden </span>
              <CloudArrowDownIcon class="ml-4 w-8 h-8"></CloudArrowDownIcon>
            </a>
          </div>
        </div>
      </template>
      <template #progress>
        <div
          v-if="oneInvitationCode == false"
          class="flex items-center justify-start pb-20"
        >
          <div class="flex bg-white rounded shadow p-4">
            <p
              v-if="
                Math.round(
                  (totalNumberOfParticipants / invitationTokens.length).toFixed(
                    2
                  ) * 100
                ) >= 90
              "
              class="mt-3 text-base text-left text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl md:mt-5 md:text-xl lg:mx-0"
            >
              Herzlichen Glückwunsch, Sie haben eine Goldmedaille erhalten.
              <strong
                v-if="invitationTokens.length > 0"
                class="mx-auto text-4xl"
                >{{
                  Math.round(
                    (
                      totalNumberOfParticipants / invitationTokens.length
                    ).toFixed(2) * 100
                  )
                }}
                %</strong
              >
              <br />
              Ihrer Mitarbeiter*innen haben an ITS.Kompetent teilgenommen!
            </p>
            <p
              v-else
              class="mt-3 text-base text-left text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl md:mt-5 md:text-xl lg:mx-0"
            >
              <strong
                v-if="invitationTokens.length > 0"
                class="mx-auto text-4xl"
                >{{
                  Math.round(
                    (
                      totalNumberOfParticipants / invitationTokens.length
                    ).toFixed(2) * 100
                  )
                }}
                %</strong
              >
              <strong v-else class="mx-auto text-4xl">{{ 0 }} %</strong>
              <br />
              Ihrer Mitarbeiter*innen haben an ITS.Kompetent teilgenommen!
            </p>
          </div>
        </div>

        <div
          class="grid grid-cols-1 pt-10 lg:grid-cols-2 xl:grid-cols-3 gap-10 lg:gap-20 2xl:gap-40 mb-10"
          :class="{ 'xl:grid-cols-4': oneInvitationCode === false }"
        >
          <CardBox
            v-if="oneInvitationCode == false"
            header=" Eingeladene Mitarbeiter*innen"
            :number="invitationTokens.length"
          >
            <template #icon>
              <UsersIcon class="h-10 w-10 pb-2 text-primary"></UsersIcon>
            </template>
          </CardBox>
          <CardBox
            header="Teilnehmer*innen Gesamt"
            :number="totalNumberOfParticipants"
          >
            <template #icon>
              <ArrowTrendingUpIcon
                class="h-10 w-10 pb-2 text-secondary"
              ></ArrowTrendingUpIcon>
            </template>
          </CardBox>

          <CardBox header="Anforderungsprofile" :number="5" icon="fas fa-users">
            <template #icon>
              <IdentificationIcon
                class="h-10 w-10 pb-2 text-primary"
              ></IdentificationIcon> </template
          ></CardBox>
          <CardBox
            v-if="trainings"
            header="Trainings"
            :number="trainings.length"
          >
            <template #icon>
              <ChartBarIcon
                class="h-10 w-10 pb-2 text-secondary"
              ></ChartBarIcon>
            </template>
          </CardBox>
        </div>
      </template>
    </Hero>
    <div
      v-if="
        totalNumberOfParticipants >= securityDisplayThreshold &&
        campagneStore.campagneEnded
      "
    >
      <div class="bg-primary py-20">
        <div class="standard-container">
          <h2 class="main-heading pt-5 pb-10 text-white">Filter</h2>

          <div class="flex flex-row justify-center items-center">
            <div
              class="border-b-4 rounded-lg w-14 border-secondary mb-10"
            ></div>
          </div>
          <div class="flex justify-center items-center pb-10">
            <p
              class="mt-3 text-base text-white sm:mt-5 sm:text-lg sm:max-w-xl md:mt-5 md:text-xl lg:mx-0"
            >
              Hier können Sie die Ergebnisse der ITS-Kompetenztests nach
              ITS-Anforderungsprofilen filtern. Dies ist nur möglich, wenn mindestens
              {{ securityDisplayThreshold }} Personen innerhalb eines
              ITS-Anforderungsprofils teilgenommen haben.
            </p>
          </div>
          <div class="flex justify-center items-center">
            <Listbox v-model="selectedProfile">
              <div class="relative mt-1 w-1/2">
                <ListboxButton
                  class="relative w-full cursor-default rounded-lg text-primary pl-2 bg-white py-2 text-left shadow-md focus:outline-none focus-visible:border-indigo-500 focus-visible:ring-2 focus-visible:ring-white focus-visible:ring-opacity-75 focus-visible:ring-offset-2 focus-visible:ring-offset-orange-300 text-sm lg:text-xl"
                >
                  <span class="block truncate">{{
                    selectedProfile.job_profile_name
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
                      v-for="profile in jobProfiles"
                      v-slot="{ selected }"
                      :key="profile.job_profile_name"
                      :value="profile"
                      as="template"
                    >
                      <li
                        :class="[
                          selected
                            ? 'bg-gray-200 text-primary'
                            : 'text-gray-900',
                          'relative cursor-pointer select-none py-2 pl-10 pr-4',
                        ]"
                      >
                        <span
                          :class="[
                            selected ? 'font-medium' : 'font-normal',
                            'block truncate',
                          ]"
                          >{{ profile.job_profile_name }}</span
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
        </div>
      </div>
      <div class="page-background p-4 pb-20">
        <div class="standard-container">
          <h2
            v-if="selectedProfile.job_profile_id === 0"
            class="main-heading pt-5 pb-10"
          >
            Allgemeine Statistiken
          </h2>
          <h2 v-else class="main-heading pt-5 pb-10">
            Statistiken für das ITS-Anforderungsprofil
            {{ selectedProfile.job_profile_name }}
          </h2>
          <div class="flex flex-row justify-center items-center">
            <div
              class="border-b-4 rounded-lg w-14 border-secondary mb-20"
            ></div>
          </div>
          <div
            v-if="
              competenceTestResults &&
              !isLoading &&
              selectedProfile.job_profile_id != 0
            "
          >
            <div class="flex flex-row justify-center items-center">
              <p
                class="mt-3 mb-10 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
              >
                Die ITS-Kompetenz von Mitarbeiter*innen, die sich dem
                ITS-Anforderungsprofil
                {{ selectedProfile.job_profile_name }} zugeordnet haben, wurde
                in
                {{ selectedProfile.number_of_threat_situations }}
                ITS-Bedrohungen getestet. Im Folgenden erhalten Sie eine
                Beschreibung jeder vertesteten ITS-Bedrohung inklusive der
                erzielten prozentualen Punktzahl.
              </p>
            </div>
            <threats-table
              :max-points-per-competence-dimension="
                maxPointsPerCompetenceDimension
              "
              :threats="competenceTestResults[0].total_threat_situation_scores"
              :total-possible-points-per-threat="totalPossiblePointsPerThreat"
              :number-of-participants="selectedProfile.number_of_participants"
            ></threats-table>
          </div>
          <h2
            v-if="selectedProfile.job_profile_id != 0"
            class="main-heading pt-20 pb-10"
          >
            Detaillierte Statistiken
          </h2>
          <div
            v-if="selectedProfile.job_profile_id != 0"
            class="flex flex-row justify-center items-center"
          >
            <div
              class="border-b-4 rounded-lg w-14 border-secondary mb-20"
            ></div>
          </div>

          <div class="flex justify-center">
            <CardBox
              v-if="selectedProfile.job_profile_name != 'Alle'"
              class="w-1/3 mt-10"
              header="Teilnehmer*innen"
              :number="selectedProfile.number_of_participants"
            >
              <template #icon>
                <ArrowTrendingUpIcon
                  class="h-10 w-10 pb-2 text-secondary"
                ></ArrowTrendingUpIcon>
              </template>
            </CardBox>
          </div>

          <div v-if="selectedProfile.job_profile_name === 'Alle'">
            <div v-if="!oneInvitationCode" class="flex justify-center">
              <p
                class="mt-3 mb-10 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
              >
                Es haben insgesamt {{ totalNumberOfParticipants }} von
                {{ invitationTokens.length }} Mitarbeiter*innen den
                ITS-Kompetenztest erfolgreich absolviert. Insgesamt haben sich
                Ihre Mitarbeiter*innen zu
                {{ jobProfileDistribution.length - 1 }} verschiedenen
                ITS-Anforderungsprofilen zugeordnet.
              </p>
            </div>

            <div v-else class="flex justify-center">
              <p
                class="mt-3 mb-10 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
              >
                Es haben insgesamt
                {{ totalNumberOfParticipants }} Mitarbeiter*innen den
                ITS-Kompetenztest erfolgreich absolviert. Insgesamt haben sich
                Ihre Mitarbeiter*innen zu
                {{ jobProfileDistribution.length - 1 }} verschiedenen
                ITS-Anforderungsprofilen zugeordnet.
              </p>
            </div>

            <div
              class="grid grid-cols-1 pt-10 gap-10 lg:gap-20 2xl:gap-40 mb-10"
            >
              <doughnut-chart
                :chart-data="chartDataProfileDistribution"
                :chart-options="chartOptionsProfileDistribution"
                :title="titleProfileDistribution"
              ></doughnut-chart>
            </div>
          </div>
          <div>
            <h2
              v-if="selectedProfile.job_profile_id === 0 && !showAll"
              class="text-2xl tracking-tight font-extrabold text-primary text-center sm:text-3xl md:text-4xl mb-10"
            >
              Aggregierte Ergebnisse für die ITS-Anforderungsprofile <br />
              mit mindestens {{ securityDisplayThreshold }} Teilnehmer*innen
            </h2>
            <div
              v-if="selectedProfile.job_profile_id === 0 && !showAll"
              class="flex flex-row justify-center items-center"
            >
              <div
                class="border-b-4 rounded-lg w-14 border-secondary mb-20"
              ></div>
            </div>
            <div
              v-if="selectedProfile.job_profile_id === 0 && !showAll"
              class="flex flex-col justify-center items-center"
            >
              <p
                class="mt-3 mb-6 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
              >
                Die folgenden Statistiken beziehen sich ausschließlich auf die
                ITS-Anforderungsprofile, bei denen mindestens
                {{ securityDisplayThreshold }} Mitarbeiter*innen den
                ITS-Kompetenztest abgeschlosen haben. <br />
                <br />
                Dies sind die ITS-Anforderungsprofile:
              </p>
              <ul
                v-for="profile in jobProfiles"
                :key="profile"
                class="mb-2 text-base text-gray-500 sm:text-lg sm:max-w-xl sm:mx-auto md:text-xl lg:mx-0"
              >
                <li v-if="profile.job_profile_id != 0" class="font-semibold">
                  {{ profile.job_profile_name }}
                </li>
              </ul>
            </div>
            <div
              class="grid grid-cols-1 pt-10 lg:grid-cols-2 gap-10 lg:gap-20 2xl:gap-40 mb-10"
            >
              <div>
                <doughnut-chart
                  :chart-data="chartDataAllThreats"
                  :chart-options="chartOptionsAllThreats"
                  :title="titleThreats"
                ></doughnut-chart>
                <p
                  class="mt-3 mb-5 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
                >
                  Die Graphik verdeutlicht, wie Ihre Mitarbeiter*innen aus dem
                  ITS- Anforderungsprofil
                  {{ selectedProfile.job_profile_name }} im Allgemeinen
                  abgeschlosssen haben. Das Ergebnis stellt den Durchschnitt
                  über alle vertesteten ITS-Bedrohungen dar. Ein Wert unter 50%
                  verdeutlicht ein hohes Förderungspotential
                </p>
              </div>
              <div>
                <bar-chart
                  ref="barChart"
                  chart-id="bar-chart1"
                  :chart-data="chartDataCompetenceDimensions"
                  :chart-options="chartOptionsCompetenceDimensions"
                  title="Erreichte Punktzahl pro ITS-Kompetenzdimension (in %)"
                ></bar-chart>
                <p
                  class="mt-3 mb-5 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
                >
                  Jede ITS-Bedrohung wurde über 7 verschiedene
                  ITS-Kompetenzdimensionen getestet. Im folgenden erhalten Sie
                  einen Überblick, wie gut sich Ihre Mitarbeiter*innen in den
                  einzelnen ITS-Kompetenzdimensionen geschlagen haben.
                </p>
                <div class="flex flex-col items-center justify-center mb-10">
                  <p
                    v-if="goodResults != 0"
                    class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
                  >
                    <strong>{{ competenceScoreGood }}</strong>
                  </p>
                  <p
                    v-if="mediumResults != 0"
                    class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
                  >
                    <strong>{{ competenceScoreMedium }}</strong>
                  </p>
                  <p
                    class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
                  >
                    <strong>{{ competenceScoreBad }}</strong>
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div v-if="selectedProfile.job_profile_name != 'Alle'">
        <div class="bg-white pt-20 pb-20">
          <div class="standard-container">
            <h1 class="main-heading mb-10">Zusammenfassung & Empfehlungen</h1>
            <div class="flex flex-row justify-center items-center">
              <div
                class="border-b-4 w-14 rounded-lg border-secondary mb-20"
              ></div>
            </div>
            <div class="flex justify-center">
              <p
                class="mt-3 text-base text-center text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl mb-10 lg:mx-0"
              >
                Auf dieser Seite erhalten Sie noch einmal eine Zusammenfassung
                der Ergebnisse Ihrer Mitarbeiter*innen für die einzelnen
                ITS-Bedrohungen, die vertestet wurden. Hier wird auch nochmal
                näher erklärt, was wir unter den ITS-Bedrohungen verstehen.
                Außerdem sprechen wir eine Empfehlung je nach erzieltem Ergebnis
                für die ITS-Bedrohungen aus.
              </p>
            </div>

            <div v-if="competenceTestResults[0].total_threat_situation_scores">
              <div
                class="space-y-4 sm:space-y-0 sm:grid sm:grid-cols-1 sm:gap-6 lg:max-w-4xl lg:mx-auto xl:max-w-none xl:mx-0 xl:grid-cols-2"
              >
                <div
                  v-for="(threat, key) in competenceTestResults[0]
                    .total_threat_situation_scores"
                  :key="key"
                >
                  <recommendation-card
                    :competence-test-results="competenceTestResults[0]"
                    :threat-key="key"
                    :threat="threat"
                    :max-points-per-competence-dimension="
                      maxPointsPerCompetenceDimension
                    "
                    :total-possible-points-per-threat="
                      totalPossiblePointsPerThreat
                    "
                  ></recommendation-card>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-if="competenceTestResults" class="page-background">
        <div class="standard-container mb-10">
          <h1 class="main-heading mb-10">Trainings-Empfehlungen</h1>
          <div class="flex flex-row justify-center items-center">
            <div
              class="border-b-4 w-14 rounded-lg border-secondary mb-10"
            ></div>
          </div>
          <div class="flex flex-col items-center justify-center mb-10">
            <p
              class="mt-3 text-base text-center text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
            >
              Im folgenden werden Ihnen kostenlose Trainings-Angebote in
              absteigender Reihenfolge nach Relevanz für Ihre Mitarbeiter*innen
              angezeigt. Die Reihenfolge der angezeigten Trainings-Angebote
              basiert auf den aggregierten Ergebnissen der ITS-Kompetenztests.
            </p>
          </div>
          <trainings-table
            v-if="trainings && !isLoading"
            :per-page="perPage"
            :total-pages="totalPages"
            :current-page="currentPage"
            :trainings="trainingsFiltered"
            :total-trainings="trainings.length"
            @re-filter-training="reFilterTrainings"
          ></trainings-table>
        </div>
      </div>
    </div>
    <div v-if="endCampagneModal">
      <end-campagne-modal
        :job-profiles="jobProfileDistribution.slice(1)"
        :security-display-threshold="securityDisplayThreshold"
        @close-modal="endCampagneModal = false"
        @end-campaign="endCampaign"
      ></end-campagne-modal>
    </div>
    <PopUp
      v-if="showFailurePopUp"
      :type="popupType"
      :title="popupTitle"
      :content="popupContent"
      @popup-closed="showFailurePopUp = false"
    />
  </template>
</template>

<script>
import CardBox from "@/components/self-service/CardBox.vue";
import ThreatsTable from "@/components/self-service/ThreatsTable.vue";
import DoughnutChart from "@/components/dashboard/DoughnutChart.vue";
import BarChart from "@/components/dashboard/BarChart.vue";
import RecommendationCard from "@/components/self-service/RecommendationCard.vue";
import CampagneService from "../../services/campagne.service.js";
import TrainingsTable from "@/components/training/TrainingsTable.vue";
import { useCampagneStore } from "@/store/CampagneStore";
import { useTrainingsStore } from "@/store/TrainingsStore";
import EndCampagneModal from "@/components/self-service/EndCampagneModal.vue";

import { useAuthStore } from "@/store/AuthStore";

import * as XLSX from "xlsx";
import {
  Listbox,
  ListboxButton,
  ListboxOptions,
  ListboxOption,
} from "@headlessui/vue";
import Hero from "@/components/base/Hero.vue";
export default {
  components: {
    CardBox,
    Hero,
    BarChart,
    RecommendationCard,
    DoughnutChart,
    TrainingsTable,
    ThreatsTable,
    EndCampagneModal,
    Listbox,
    ListboxButton,
    ListboxOptions,
    ListboxOption,
  },
  props: {
    refreshView: {
      type: Boolean,
      default: false,
    },
  },

  /**
   * Initializes and returns the state for the Vue component using composition API.
   *
   * This setup function utilizes the Vuex stores specific to campagne and trainings.
   * It invokes `useCampagneStore` to access and manage the state related to the campagne,
   * and `useCampagneStore` for managing state related to the campagne. The function
   * then returns these stores for use within the Vue component, enabling reactive state management
   * and encapsulation of business logic associated with the campagne and trainings.
   *
   * @returns {Object} An object containing references to `campagneStore` and `trainingsStore`.
   */
  setup() {
    const campagneStore = useCampagneStore();
    const trainingsStore = useTrainingsStore();
    const authStore = useAuthStore();

    return { campagneStore, trainingsStore, authStore };
  },

  data() {
    return {
      titleThreats: "",
      isLoading: false,
      titleProfileDistribution: "",
      invitationTokens: [],
      totalNumberOfParticipants: 0,
      totalPossiblePointsPerThreat: 14,
      maxPointsPerCompetenceDimension: 2,
      pointsScoredPerThreat: 0,
      numberOfThreats: [],
      numberOfCompetenceDImensions: 0,
      jobProfiles: [],
      jobProfileDistribution: [],
      jobProfilesCopy: [],
      trainings: [],
      competenceTestResults: {},
      oneInvitationCode: null,

      selectedProfile: {
        job_profile_id: 0,
        job_profile_name: "Alle",
        number_of_participants: 0,
      },

      securityDisplayThreshold: 0,
      aggregateOverSingleProfiles: false,
      showAll: false,

      mockedThreatData: [],
      mockedCompetenceData: [],
      chartDataAllThreats: {},
      chartOptionsAllThreats: {},

      chartDataProfileDistribution: {},
      chartOptionsProfileDistribution: {},
      chartDataCompetenceDimensions: {},
      chartOptionsCompetenceDimensions: {},

      trainingsFiltered: null,
      totalPages: 0,
      currentPage: 1,
      perPage: 5,

      goodResults: [],
      mediumResults: [],

      competenceScoreSummary: "",
      competenceScoreGood: "",
      competenceScoreMedium: "",
      competenceScoreBad: "",

      endCampagneModal: false,
      showFailurePopUp: false,

      //popup
      popupTitle: "",
      popupType: "",
      popupContent: "",
    };
  },
  /**
   * A Vue watch property.
   *
   */
  watch: {
    /**
     * A Vue watch property.
     * Gets called whenever the selectedProfile changes
     * If so the respecting competence test results for the profile are fetched from the database.
     * Also, the charts and trainings are set up based on the new filter.
     * @param {Object} newProfile The newly selected job profile
     */
    async selectedProfile(newProfile) {
      this.isLoading = true;
      this.selectedProfile = newProfile;
      await this.fetchCompetenceTestResults(newProfile.job_profile_id);
      this.matchTrainings(this.trainings);
      this.trainings = this.sortAndShuffleTrainings(this.trainings);
      this.filterTrainingsPerPage(this.trainings);

      this.setUpThreats(newProfile);
      this.setUpCompetenceBarChart(newProfile);
      this.goodResults = [];
      this.mediumResults = [];
      this.setCompetenceScores();
    },
    /**
     * A Vue watch property.
     * Gets called when the dahboard mounts or when the user clicks the refresh button in SelfServicePortal
     * @param {Object} newValue The new state of refresh
     * @param {Object} oldValue The old state of refresh

     */
    refreshView(newValue, oldValue) {
      if (newValue !== oldValue) {
        this.refreshData();
      }
    },
  },
  /**
   * A Vue component lifecycle method that runs once the component is mounted to the DOM.
   * It basically fecthes the data on scored points and prepares all chart data that is displayed including the results of the aggregated test results.
   */
  async mounted() {
    // const response = await this.authStore.getUserProfile();
    const campagneData = await this.campagneStore.getCampagne();
    if (campagneData.campaign_ended) {
      this.campagneStore.setCampagneEnded();
    }
    this.refreshData();

    // this.securityDisplayThreshold = response.security_display_threshold;
  },
  methods: {
    async endCampaign(aggregateOverAllProfiles) {
      this.aggregateOverSingleProfiles = !aggregateOverAllProfiles;

      this.campagneStore.setCampagneEnded();
      this.isLoading = true;
      await this.campagneStore.endCampaign({
        aggregateOverSingleProfiles: this.aggregateOverSingleProfiles,
      });
      await this.campagneStore.invalidateInvitationTokens();
      this.$nextTick(async () => {
        await this.refreshData();
      });
    },
     openEndCampagneModal() {
      if (this.totalNumberOfParticipants >= this.securityDisplayThreshold) {
        this.endCampagneModal = true;
      } else {
        this.popupType = "danger";
        this.popupTitle = "Kampagne beenden";
        this.popupContent = `Die Kampagne kann nur beendet werden, wenn mindestens ${this.securityDisplayThreshold} Mitarbeiter*innen teilgenommen haben.`;

        this.showFailurePopUp = true;
      }
    },
    async refreshData() {
      this.isLoading = true;
      this.trainings = await this.trainingsStore.getTrainings();

      const campagneData = await this.campagneStore.getCampagne();
      this.oneInvitationCode = campagneData.one_token_mode;
      this.securityDisplayThreshold = campagneData.security_display_threshold;
      this.aggregateOverSingleProfiles =
        campagneData.aggregate_over_single_profiles;

      this.invitationTokens = await CampagneService.getInvitedEmployees();
      // if each employee gets a separate invitation code
      if (this.oneInvitationCode == false) {
        this.totalNumberOfParticipants = this.invitationTokens.reduce(
          (count, token) => {
            return token.is_participated ? count + 1 : count;
          },
          0
        );
        // if one invitation code is used for all participants
      } else {
        this.totalNumberOfParticipants = this.invitationTokens[0].tokenCounter;
      }

      this.jobProfiles = await CampagneService.getParticipantsPerProfile();
      this.jobProfileDistribution = Object.values(this.jobProfiles).filter(
        (obj) => obj.number_of_participants > 0
      );
      this.jobProfiles = Object.values(this.jobProfileDistribution).filter(
        (obj) => obj.number_of_participants >= this.securityDisplayThreshold
      );

      if (!this.aggregateOverSingleProfiles) {
        this.jobProfilesCopy = Object.values(this.jobProfiles);
        this.jobProfiles = this.jobProfiles.slice(0, 1);
        this.showAll = true;
      }
      if (this.jobProfiles.length > 0) {
        this.selectedProfile = this.jobProfiles[0];
      } else {
        setTimeout(() => (this.isLoading = false), 500);
        return;
      }

      if (
        this.selectedProfile.number_of_participants >=
        this.securityDisplayThreshold
      ) {
        await this.fetchCompetenceTestResults(
          this.selectedProfile.job_profile_id
        );
        this.setUpThreats();
        this.setUpProfileDistribution();
        this.setUpCompetenceBarChart();
        this.setCompetenceScores();

        this.matchTrainings(this.trainings);
        this.trainings = this.sortAndShuffleTrainings(this.trainings);
        this.filterTrainingsPerPage(this.trainings);

        this.totalPages = Math.ceil(this.trainings.length / this.perPage);
      }
      setTimeout(() => (this.isLoading = false), 500);
    },
    /**
     * A method to export a management report including the aggregated results from the competence tests.
     * @throws {Error} Throws an error when no management report could be created and shows a failure popup.
     */
    async exportManagementReport() {
      try {
        this.isLoading = true;
        const response = await this.campagneStore.getManagementReport();

        const file = new Blob([response.data], { type: "application/pdf" });

        // Create a URL for the blob
        const fileURL = URL.createObjectURL(file);

        // window.open(fileURL, "_blank");
        // setTimeout(() => URL.revokeObjectURL(fileURL), 100);

        // Create an anchor (<a>) element to trigger the download
        const link = document.createElement("a");
        link.href = fileURL;
        link.setAttribute("download", "management_report.pdf"); // Specify a filename for the download
        document.body.appendChild(link);
        link.click();

        // Clean up by removing the link and revoking the URL
        document.body.removeChild(link);
        URL.revokeObjectURL(fileURL);
        this.popupType = "success";
        this.popupTitle = "Management-Report downloaden";
        this.popupContent = "Eine PDF-Datei wurde erstellt und heruntergeladen";
        this.showSuccessPopUp = true;
      } catch (error) {
        console.error("Error fetching or downloading the PDF:", error);
        this.popupType = "danger";
        this.popupTitle = "Management-Report downloaden";
        this.popupContent = "Eine PDF-Datei konnte nicht erzeugt werden.";
        this.showFailurePopUp = true;
      }
      this.isLoading = false;
    },
    /**
     * A helper method to filter training proograms on their assigned page.
     * Creates a second array holding trainings (trainingsFiltered) changes per page.
     * @param {Array} trainings The original unfiltered array of training programs.
     */
    filterTrainingsPerPage(trainings) {
      this.trainingsFiltered = trainings.filter(
        (item) => item.pageNumber === this.currentPage
      );
    },
    /**
     * A helper method to add the property pageNumber to each training
     * @param {Array} trainings The original array of training programs.
     * @return {Array} The array of trainings with page numbers.
     */
    mapPageNumbers(trainings) {
      trainings = trainings.map((item, index) => ({
        ...item,
        pageNumber: Math.floor(index / this.perPage + 1),
      }));
      return trainings;
    },
    /**
     * Base method to calcualate a matching score for each training program based on the aggregated competence test results of each job profile.
     * Calls a method to sort and shuffle trainings
     * @param {Array} trainings The array of trainings before adding the matching score.
     */
    matchTrainings(trainings) {
      let matchingScore = 0;
      let tempArray = [];
      let totalCompetenceDimensionScores = Object.values(
        this.competenceTestResults[0].total_competence_dimension_scores
      );
      for (let i = 0; i < trainings.length; i++) {
        for (let j = 0; j < totalCompetenceDimensionScores.length; j++) {
          let competenceDimensionMatchingScore = 0;
          let trainingCompetence = 0;
          let trainingFocus = 0;
          let inverseCompetenceDimensionScore = 0;
          if (
            this.isCompetenceDimensionInTraining(
              totalCompetenceDimensionScores[j].description,
              trainings[i]
            )
          ) {
            trainingCompetence = 1;
          }
          inverseCompetenceDimensionScore =
            totalCompetenceDimensionScores[j].total_scoredPoints /
            (this.selectedProfile.number_of_participants *
              2 *
              this.numberOfThreats);

          inverseCompetenceDimensionScore =
            (1 - inverseCompetenceDimensionScore) * 10;

          trainingFocus =
            totalCompetenceDimensionScores.length /
            trainings[i].competence_dimension_count;

          competenceDimensionMatchingScore =
            inverseCompetenceDimensionScore *
            (trainingCompetence * trainingFocus);

          matchingScore += competenceDimensionMatchingScore;
          tempArray.push(competenceDimensionMatchingScore);
        }
        trainings[i].matchingScore = Math.round(matchingScore);
        trainings[i].tempArray = tempArray;
        tempArray = [];
        matchingScore = 0;
      }
      this.sortAndShuffleTrainings(trainings);
    },
    /**
     * Method to assign ranks to the training program based on the matching score.
     * The lower the rank, the better the match.
     * @param {Array} trainings The array of trainings before assigning ranks.
     * @return {Array} The array of trainings with assigned ranks.
     */
    assignRanks(trainings) {
      let rank = 1; // Start ranking from 1
      let lastScore = trainings[0].matchingScore; // Score of the first item for comparison
      trainings[0].rank = rank; // Assign first rank manually

      // Counter for items with the same score

      for (let i = 1; i < trainings.length; i++) {
        if (trainings[i].matchingScore !== lastScore) {
          // Increment rank by the number of items with the previous score
          rank += 1;
        }

        trainings[i].rank = rank;
        lastScore = trainings[i].matchingScore; // Update lastScore for comparison
      }
      return trainings;
    },
    /**
     * Emits current page when the user paginates and sets the new page.
     * Calls filterTrainignsPerPage to filter for the trainings assigned with the corresponding page number
     * @param {Number} pageNumber The page number of the emitted page.
     */
    reFilterTrainings(pageNumber) {
      this.currentPage = pageNumber;
      this.filterTrainingsPerPage(this.trainings);
    },

    /**
     * Helper method to check whether a specific competence dimension is conveyed in a training program
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
     * Method to sort the training programs by matchingScore in descending order.
     * Calls shuffleArray to shuffle training programs with equal matching score.
     * @param {Array} trainings The array of trainings before sorting and shuffling.

     */
    sortAndShuffleTrainings(trainings) {
      // Initial sort by matchingScore in descending order
      trainings.sort((a, b) => b.matchingScore - a.matchingScore);

      // Group by matchingScore
      const groupedByScore = trainings.reduce((acc, curr) => {
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
        const trainingsTemp = groupedByScore[score];

        // Group by training_group.id within each matchingScore
        const groupedByTrainingGroup = trainingsTemp.reduce((acc, curr) => {
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
      trainings = sortedAndShuffled;
      trainings = this.mapPageNumbers(trainings);
      trainings = this.assignRanks(trainings);
      return trainings;
    },
    /**
     * Loops through all job profile, gets the related competence test results for each job profile
     * Then fetches trainings, calculates a matching score and pushes the array into a trainingsList
     * @return {Array} An array including an array of training programs for each job profile in different order based on the matching score.
     */
    async generateTrainingsExport() {
      let trainingsList = [];
      let trainingsExport = [];

      var i = 0;
      for (i; i < this.jobProfiles.length; i++) {
        trainingsExport = JSON.parse(JSON.stringify(this.trainings));

        if (
          this.selectedProfile.job_profile_id !=
          this.jobProfiles[i].job_profile_id
        ) {
          await this.fetchCompetenceTestResults(
            this.jobProfiles[i].job_profile_id
          );
          this.matchTrainings(trainingsExport);
          trainingsExport = this.sortAndShuffleTrainings(trainingsExport);
        }

        trainingsList.push(JSON.parse(JSON.stringify(trainingsExport)));
        trainingsExport = [];
      }
      return trainingsList;
    },
    /**
     * Method to prepare the data before exporting to excel.
     * @param {Array} dataArray The training programs.
     * @return {Array} Returns the updated array with renamend columns for better readibility.
     */
    prepareDataForExport(dataArray) {
      return dataArray.map((subArray) =>
        subArray.map((item) => ({
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
        }))
      );
    },
    /**
     * Method to generate an excel file including the training programs sorted by matching score.
     * @throws {Error} Throws an error when an excel file cannot be created.
     */
    async exportTrainingsToExcel() {
      let dataToExport = await this.generateTrainingsExport();
      dataToExport = this.prepareDataForExport(dataToExport);
      var i = 0;

      // Continue with the SheetJS export process
      const workbook = XLSX.utils.book_new();

      for (i; i < dataToExport.length; i++) {
        const worksheet = XLSX.utils.json_to_sheet(dataToExport[i]);
        XLSX.utils.book_append_sheet(
          workbook,
          worksheet,
          `${this.jobProfiles[i].job_profile_name}`
        );
      }
      // Trigger download
      try {
        XLSX.writeFile(workbook, "ITS-Trainingsempfehlungen.xlsx");
        this.popupType = "success";
        this.popupTitle = "Excel exportieren";
        this.popupContent = "Ein Excel-File wurde erstellt und heruntergeladen";
        this.showSuccessPopUp = true;
      } catch (err) {
        console.error("Could not copy text: ", err);
        this.popupType = "danger";
        this.popupTitle = "Text kopieren";
        this.popupContent = "Der Text konnte nicht kopiert werden.";
        this.showFailurePopUp = true;
      }
    },
    async fetchCompetenceTestResults(newProfile) {
      try {
        // ... fetch data logic ...
        this.competenceTestResults =
          await CampagneService.getCompetenceTestResults(newProfile);

        if (newProfile != 0) {
          this.numberOfThreats = Object.values(
            this.competenceTestResults[0].total_threat_situation_scores
          ).length;
        } else {
          this.numberOfThreats =
            this.competenceTestResults[0].number_of_threats;
        }

        this.numberOfCompetenceDimensions = Object.values(
          this.competenceTestResults[0].total_competence_dimension_scores
        ).length;
        this.selectedProfile.number_of_participants =
          this.competenceTestResults[0].number_of_participants;
      } catch (error) {
        console.error("Error fetching data:", error);
      } finally {
        setTimeout(() => (this.isLoading = false), 500);
      }
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
        i < this.chartDataCompetenceDimensions.datasets[0].data.length;
        i++
      ) {
        if (this.chartDataCompetenceDimensions.datasets[0].data[i] >= 66) {
          this.goodResults.push(
            ` ${this.chartDataCompetenceDimensions.labels[i]}`
          );
        } else if (
          this.chartDataCompetenceDimensions.datasets[0].data[i] >= 50
        ) {
          this.mediumResults.push(
            ` ${this.chartDataCompetenceDimensions.labels[i]}`
          );
        } else {
          badResults.push(` ${this.chartDataCompetenceDimensions.labels[i]}`);
        }
      }
      this.competenceScoreGood = `Die Ergebnisse Ihrer Mitarbeiter*innen sind außerordentlich gut in den ITS-Kompetenzdimensionen: ${this.goodResults} `;
      this.competenceScoreMedium = `In den folgenden ITS-Kompetenzdimensionen konnten Ihre Mitarbeiter*innen gute Ergebnisse erzielen: ${this.mediumResults}`;
      this.competenceScoreBad = `In diesen ITS-Kompetenzdimensionen besteht noch Verbesserungspotential:${badResults}`;
    },
    /**
     * Sets up a bar chart where each bar represents the percentage score for a competence dimension.
     * Shows the aggregated score over all threat vectors.
     * Gets called in mounted hook
     * @param {object} label The labels for each competence dimension
     * @param {object} data The percentagee score per competence dimension over all threat vectors
     */
    setUpCompetenceBarChart() {
      let competenceScoreData = [];
      let competenceDimensionData = [];
      let maxPoints = 0;
      let array = [];
      if (this.showAll) {
        array = this.jobProfileDistribution;
      } else {
        array = this.jobProfiles;
      }
      if (this.selectedProfile.job_profile_id == 0) {
        for (const element of array) {
          if (element.job_profile_id != 0) {
          
            maxPoints +=
              element.number_of_participants *
              this.maxPointsPerCompetenceDimension *
              element.number_of_threat_situations;
          }
        }
      }

      for (const element of Object.values(
        this.competenceTestResults[0].total_competence_dimension_scores
      )) {
        if (this.selectedProfile.job_profile_id != 0) {
          competenceScoreData.push(
            Math.round(
              (element.total_scoredPoints /
                (this.numberOfThreats *
                  this.maxPointsPerCompetenceDimension *
                  this.competenceTestResults[0].number_of_participants)) *
                100
            )
          );
        } else {
          competenceScoreData.push(
            Math.round((element.total_scoredPoints / maxPoints) * 100)
          );
        }
        competenceDimensionData.push(element.description);
      }

      this.chartDataCompetenceDimensions = {
        labels: competenceDimensionData,
        datasets: [
          {
            data: competenceScoreData,
            backgroundColor: ["#303e7a"],
            label: "Score",
          },
        ],
      };
      this.chartOptionsCompetenceDimensions = {
        plugins: {
          title: {
            display: false,
            text: "Erreichte Punktzahl über alle Bedrohungsereignisse (in %)",
            font: {
              size: 20,
            },
          },
        },
        maintainAspectRatio: false,
        legend: {
          display: false,
        },
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
        scales: {
          y: {
            max: 100, // Set the maximum value of the y-axis to 100
            beginAtZero: true, // Ensures the y-axis starts at 0
            grid: {
              display: false,
            },
          },
          x: {
            grid: {
              display: false,
            },
          },
        },
      };
    },
    /**
     * Sets up a doughnut chart where each bar represents the percentage of the distribution of participants per job profile.
     * Gets called in mounted hook
     */
    setUpProfileDistribution() {
      let profileDistributionData = [];
      let profileJobNameData = [];
      for (const profileData of Object.values(this.jobProfileDistribution)) {
        if (profileData.job_profile_id != 0) {
          profileDistributionData.push(
            Math.round(
              (profileData.number_of_participants /
                this.totalNumberOfParticipants) *
                100
            )
          );
          profileJobNameData.push(profileData.job_profile_name);
        }
      }
      this.titleProfileDistribution =
        "Verteilung der Teilnehmenden aus den ITS-Anforderungsprofilen (in %)";
      this.chartDataProfileDistribution = {
        labels: profileJobNameData,
        datasets: [
          {
            data: profileDistributionData,
            backgroundColor: [
              "#1f2c5a",
              "#f06666",
              "#683d87",
              "#303e7a",
              "#EB5757",
            ],
          },
        ],
      };
      this.chartOptionsProfileDistribution = {
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
    /**
     * Sets up a bar chart where each bar represents the percentage score for a threat vector.
     *
     */
    setUpThreats() {
      let totalPoints = 0;
      let maxPoints = 0;
      let array = [];
      if (this.showAll) {
        array = this.jobProfileDistribution;
      } else {
        array = this.jobProfiles;
      }
      if (this.selectedProfile.job_profile_id != 0) {
        for (const element of Object.values(
          this.competenceTestResults[0].total_threat_situation_scores
        )) {
          totalPoints += element.total_scoredPoints;
        }
        if (this.selectedProfile.job_profile_id != 0) {
          maxPoints =
            this.competenceTestResults[0].number_of_participants *
            (this.totalPossiblePointsPerThreat * this.numberOfThreats);
        } else {
          for (const element of array) {
            if (element.job_profile_id != 0) {
              maxPoints +=
                element.number_of_participants *
                this.totalPossiblePointsPerThreat *
                element.number_of_threat_situations;
            }
          }
        }
      } else {
        totalPoints =
          this.competenceTestResults[0].total_threat_situation_scores
            .total_scoredPoints;
        for (const element of array) {
          if (element.job_profile_id != 0) {
            maxPoints +=
              element.number_of_participants *
              this.totalPossiblePointsPerThreat *
              element.number_of_threat_situations;
          }
        }
      }
      this.pointsScoredPerThreat = Math.round((totalPoints / maxPoints) * 100);

      this.titleThreats =
        "Erreichte Punktzahl über alle ITS-Bedrohungen (in %)";
      this.chartDataAllThreats = {
        labels: ["Korrekt beantwortet", "Falsch beantwortet"],
        datasets: [
          {
            data: [
              this.pointsScoredPerThreat,
              100 - this.pointsScoredPerThreat,
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
          centerText: {
            display: true,
            text: "56",
            font: {
              size: 40,
              weight: "bold",
            },
            color: "#303e7a",
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
.fade-enter-from {
  opacity: 0;
}
.fade-enter-active {
  transition: all 2s ease;
}
</style>
