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
              >Mitarbeiter*innen <br />
            </span>
            {{ " " }}
            <span class="text-secondary xl:inline"
              >zu ITS.Kompetent einladen</span
            >
          </h1>
        </div>
      </template>
      <template #content>
        <div
          class="flex justify-center items-center lg:items-start lg:justify-start"
        >
          <p
            v-if="oneInvitationCode == true"
            class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl md:mt-5 md:text-xl lg:mx-0"
          >
            In dieser Ansicht können Sie zunächst Mitarbeiter*innen einladen an
            ITS.Kompetent teilzunehmen. Sie haben sich dazu entschieden einen
            Einladungs-Code für alle Mitarbeiter*innen zu generieren.
          </p>
          <div v-else-if="oneInvitationCode == false">
            <p
              class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl md:mt-5 md:text-xl lg:mx-0"
            >
              In dieser Ansicht können Sie zunächst Mitarbeiter*innen einladen
              an ITS.Kompetent teilzunehmen. Sie haben sich dazu entschieden
              einen Einladungs-Code pro Mitarbeiter*in zu generieren. <br />
              <br />

              <span v-if="securityKeyActivated && invitationObjects.length > 0">
                <br />
                <br />Sie können weitere Einladungs-Codes generieren. Dazu
                benötigen sie den Sicherheits-Code den Sie bei Erstellung der
                Kampagne erhalten haben.</span
              >
            </p>
            <p
              v-if="securityKey && invitationObjects.length < 1"
              class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl md:mt-5 md:text-xl lg:mx-0"
            >
              Dazu erhalten Sie den folgenden Sicherheits-Code.
              <strong>Bewahren Sie den Code </strong> gut auf, da er verloren
              geht, sobald Sie diese Seite verlassen oder aktualisieren.
              Zusätzlich sollte ein Download gestartet haben, der den
              Sicherheits-Code in einer Text-Datei enthält. <br />
              <br />
              <strong>{{ securityKey }}</strong>
              <br />
              <br />
              Sie können nun Einladungs-Codes genrierien lassen, indem Sie eine
              CSV-Datei hochladen, die die E-Mail-Adressen der Teilnehmer*innen
              enthält.
            </p>
          </div>
          <div v-else>
            <p
              class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl md:mt-5 md:text-xl lg:mx-0"
            >
              In dieser Ansicht können Sie zunächst Mitarbeiter*innen einladen
              an ITS.Kompetent teilzunehmen. Sie können sich zunächst
              entscheiden, ob sie einen Einladungs-Code, den alle
              Mitarbeiter*innen nutzen oder einen Einladungs-Code pro
              Mitarbeiter*in generieren möchten. <br />
              <br />

              Sie müssen sich an dieser Stelle zudem festlegen, ab wie vielen
              Teilnehmenden aus einem ITS-Anforderungsprofil Ergebnisse
              angezeigt werden sollen. Der Minimum-Wert liegt aus
              Datenschutzgründen bei 5 Teilnehmenden.
            </p>
            <div class="py-5 max-w-lg">
              <!-- Field for securityDisplayThreshold -->
              <div class="mb-4">
                <label
                  for="securityDisplayThreshold"
                  class="block text-gray-700 text-sm font-bold mb-2"
                >
                  Minimum Teilnehmende für die Datenaggregation (Minimum 5)
                </label>
                <input
                  id="securityDisplayThreshold"
                  v-model.number="form.securityDisplayThreshold"
                  type="number"
                  class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  @input="validateThreshold"
                />
              </div>
            </div>
          </div>
        </div>
      </template>
      <template #buttons>
        <div
          class="flex flex-col justify-center items-center lg:items-start lg:justify-start"
        >
          <div
            v-if="oneInvitationCode == true && invitationObjects.length < 1"
            class="sm:w-2/5 md:w-2/5 w-3/5 2xl:w-2/6"
          >
            <a
              href="#"
              class="w-full flex justify-between font-semibold items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-secondary hover:bg-secondaryAccent mt-12 md:py-4 md:text-lg md:px-10"
              @click="generateInvitationTokens"
            >
              Code generieren
              <CloudArrowUpIcon class="w-8 h-8"></CloudArrowUpIcon>
            </a>
          </div>
          <div
            v-if="oneInvitationCode == true && invitationObjects.length == 1"
          >
            <p
              class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl md:mt-5 md:text-xl lg:mx-0"
            >
              Ein Einladungs-Code wurde generiert. Sie können diesen kopieren
              und per E-Mail an Ihre Mitarbeiter*innen versenden. Ihre
              Mitarbeiter*innen können entweder über folgenden Link an
              ITS.kompetent teilnehmen:<br />
              <br />
              <a
                v-if="invitationObjects[0]"
                :href="`${domainURL}/competence-tests/introduction/${invitationObjects[0].token}`"
                target="_blank"
              >
                <strong>
                  {{ domainURL }}/competence-tests/introduction/{{
                    invitationObjects[0].token
                  }}
                </strong>
              </a>
              <br />
              <br />
              Alternativ können Ihre Mitarbeiter*innen den Einladungs-Code
              selbständig auf der Kampagnenseite eingeben.
            </p>
          </div>
          <div
            v-if="oneInvitationCode == false && invitationObjects.length < 1"
            class="sm:w-2/5 md:w-2/5 w-3/5 2xl:w-2/6"
          >
            <a
              href="#"
              class="w-full flex justify-between cursor-pointer font-semibold items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-secondary hover:bg-secondaryAccent mt-12 md:py-4 md:text-lg md:px-10"
              @click="openInvitationTokenGeneration"
            >
              Codes generieren
              <CloudArrowUpIcon class="w-8 h-8"></CloudArrowUpIcon>
            </a>
          </div>
          <div
            v-if="
              oneInvitationCode == false &&
              securityKeyActivated &&
              invitationObjects.length > 0
            "
          >
            <input
              v-model="securityKey"
              type="text"
              class="w-full sm:w-96 border-2 px-2 mt-5 border-white bg-gray-100 h-12 rounded-lg text-lg focus:outline-none"
              placeholder="Sicherheits-Code"
            />
          </div>
          <div
            v-if="oneInvitationCode == false && invitationObjects.length > 0"
            class="sm:w-2/5 md:w-2/5 w-3/5 2xl:w-2/6"
          >
            <a
              class="w-full flex justify-between cursor-pointer font-semibold items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-secondary hover:bg-secondaryAccent mt-12 md:py-4 md:text-lg md:px-10"
              @click="openInvitationTokenGeneration"
            >
              Codes hinzufügen
              <CloudArrowUpIcon class="w-8 h-8"></CloudArrowUpIcon>
            </a>
          </div>
        </div>
      </template>

      
    </Hero>
    <div v-if="oneInvitationCode == null && !campagneStore.campagneStarted">
      <div class="page-background">
        <div class="standard-container">
          <div
            class="grid grid-cols-1 xl:grid-cols-2 gap-10 gap-y-20 lg:gap-x-20 xl:gap-x-40"
          >
            <div
              v-for="invitationMode in invitationModeOptions"
              :key="invitationMode.id"
            >
              <transition appear name="fade">
                <invitation-mode-card
                  :id="invitationMode.id"
                  :name="invitationMode.name"
                  :description="invitationMode.description"
                  :benefits="invitationMode.benefits"
                  :disadvantages="invitationMode.disadvantages"
                  @change="applyInvitationChoice(invitationMode.id)"
                ></invitation-mode-card>
              </transition>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-if="oneInvitationCode != null && campagneStore.campagneStarted">
      <div class="page-background">
        <div class="standard-container">
          <h1
            class="text-2xl tracking-tight font-extrabold text-primary text-center sm:text-3xl md:text-4xl mb-10"
          >
            Generierte Einladungs-Codes
          </h1>
          <div class="flex flex-row justify-center items-center">
            <div
              class="border-b-4 w-14 rounded-lg border-secondary mb-10"
            ></div>
          </div>
          <div
            v-if="oneInvitationCode == false"
            class="flex justify-center pb-10"
          >
            <p
              v-if="securityKeyActivated"
              class="mt-3 text-base text-gray-500 text-center sm:mt-5 sm:text-lg sm:max-w-xl md:mt-5 md:text-xl lg:mx-0"
            >
              Im Folgenden erhalten Sie die Anzahl an Einladungs-Codes, die Sie
              generiert haben. Sie können diese als Excel-Liste exportieren und
              Mitarbeiter*innen zuordnen. Alternativ haben Sie die Möglichkeit
              die E-Mail-Adressen mittels des Sicherheits-Codes in Klartext
              umzuwandeln. Dies ermöglicht es Ihnen einen E-Mail-Serienbrief
              anzulegen, um das Einladungs-Management noch einfacher zu
              gestalten. <br />
              <br />
              Weiter unten stellen wir Ihnen einen Beispieltext zur Einladung
              Ihrer Mitarbeiter*innen zu Ihrer ITS.kompetent Kampagne dar. Sie
              können diesen kopieren und die Platzhalter durch den Export aus
              der Excel-Liste mit den Meta-Informationen ersetzen.
            </p>
            <p
              v-else
              class="mt-3 text-base text-gray-500 text-center sm:mt-5 sm:text-lg sm:max-w-xl md:mt-5 md:text-xl lg:mx-0"
            >
              Im Folgenden erhalten Sie die Anzahl an Einladungs-Codes, die Sie
              generiert haben. Sie können diese als Excel-Liste exportieren und
              Mitarbeiter*innen zuordnen. <br />
              <br />
              Weiter unten stellen wir Ihnen einen Beispieltext zur Einladung
              Ihrer Mitarbeiter*innen zu Ihrer ITS.kompetent Kampagne dar. Sie
              können diesen kopieren und die Platzhalter durch den Export aus
              der Excel-Liste mit den Meta-Informationen ersetzen.
            </p>
          </div>
          <div
            v-if="oneInvitationCode == true"
            class="flex justify-center pb-10"
          >
            <p
              class="mt-3 text-base text-gray-500 text-center sm:mt-5 sm:text-lg sm:max-w-xl md:mt-5 md:text-xl lg:mx-0"
            >
              Im Folgenden erhalten Sie die den Einladungs-Codes, den Sie
              generiert haben. <br />
              <br />
              Weiter unten stellen wir Ihnen einen Beispieltext zur Einladung
              Ihrer Mitarbeiter*innen zu Ihrer ITS.kompetent Kampagne dar. Sie
              können diesen kopieren und die Platzhalter ersetzen, um den
              Einladungs-Code an Ihrer Mitarbeiter*innen zu distributieren.
            </p>
          </div>
          <div
            class="text-md lg:text-xl max-w-2xl text-left mx-auto my-8 p-6 bg-white shadow-md rounded-lg"
          >
            <div class="text-gray-600 mb-4">
              Liebe/r Kolleg*in<span class="font-semibold"></span>,
            </div>
            <div class="text-gray-600">
              unser Unternehmen nimmt derzeit an ITS.kompetent teil. Das Projekt
              ITS.kompetent unterstützt KMUs dabei, die Kompetenzen der
              Mitarbeiter:innen im Bereich der Informationstechnischen
              Sicherheit (ITS-Kompetenzen) realitätsnah zu messen und mit den
              berufsbezogenen Anforderungen abzugleichen. Mit Hilfe von
              ITS.kompetent können KMUs ihren unternehmensspezifischen
              Qualifizierungsbedarf ermitteln und geeignete
              ITS-Schulungsangebote ausarbeiten.
              <br />
              <br />
              Ich bitte Sie an der bestehenden Kampagne teilzunehmen. Ihr
              Einladungs-Code lautet:
              <strong>[Einladungs-Code]</strong>
              <br />
              <br />
              Sie erreichen unsere ITS-Kampagne unter
              <a href="frontendURL"><strong>[URL]</strong></a>
            </div>
            <div class="mt-4">
              Viele Grüße,<br />
              <span class="font-semibold">[Ihr Name]</span>
            </div>
            <button
              class="flex justify-between font-semibold mt-6 px-4 py-2 bg-primary text-white rounded hover:bg-primaryAccent focus:outline-none"
              @click="copyEmailText"
            >
              Text kopieren
              <DocumentDuplicateIcon
                class="ml-2 w-6 h-6"
              ></DocumentDuplicateIcon>
            </button>
          </div>
        </div>
        <div v-if="oneInvitationCode == false">
          <div v-if="securityKeyActivated" class="bg-primary pt-10 pb-20">
            <div class="standard-container">
              <h2
                class="text-2xl tracking-tight font-extrabold text-white text-center sm:text-3xl md:text-4xl pt-10 mb-10"
              >
                Sicherheits-Code
              </h2>
              <div class="flex justify-center mb-10">
                <p
                  class="mt-3 text-base text-white text-center sm:mt-5 sm:text-lg sm:max-w-xl md:mt-5 md:text-xl lg:mx-0"
                >
                  Über den für Sie generierten Sicherheits-Code können sie die
                  E-Mail-Adressen entschlüsseln.
                </p>
              </div>
              <div class="flex justify-center">
                <div class="mx-5">
                  <input
                    v-model="securityKey"
                    type="text"
                    class="w-full sm:w-96 border-2 border-white bg-white h-10 px-2 rounded-lg text-lg focus:outline-none"
                    placeholder="Sicherheits-Code"
                  />
                  <div
                    class="flex mt-2 justfiy-center underline text-white cursor-pointer"
                  >
                    <span @click="openRemoveSecurityKeyModal"
                      >Sicherheits-Code vergessen?</span
                    >
                  </div>
                </div>
                <div class="mx-5">
                  <div
                    v-if="
                      oneInvitationCode == false && decryptedEmails.length < 1
                    "
                    class="flex justify-between items-center"
                  >
                    <a
                      class="w-full flex items-center justify-center px-4 h-10 border border-transparent text-base cursor-pointer font-semibold rounded-md text-primary bg-white hover:bg-gray-300 md:text-lg md:px-2"
                      @click="decryptEmails"
                    >
                      Entschlüsseln
                      <KeyIcon class="text-primary ml-2 w-6 h-6"></KeyIcon>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="bg-white">
            <div class="standard-container">
              <h2
                class="text-2xl tracking-tight font-extrabold text-primary text-center sm:text-3xl md:text-4xl pt-10 mb-10"
              >
                Filter
              </h2>

              <div class="flex flex-row justify-center items-center">
                <div
                  class="border-b-4 rounded-lg w-14 border-secondary mb-10"
                ></div>
              </div>
              <div class="flex justify-center mb-10">
                <p
                  class="mt-3 text-base text-center text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl md:mt-5 md:text-xl lg:mx-0"
                >
                  In dieser Ansicht können Sie Teilnehmer*innen nach Teilnahme
                  an ITS.kompetent filtern. Eine Excel-Datei als Datenquelle für
                  einen E-Mail-Serienbrief kann über einen Klick auf den Button
                  Exportieren generiert werden.
                </p>
              </div>
              <div class="flex justify-center items-center gap-x-5 pb-10">
                <FilterDropDown
                  class="w-64"
                  :filter-options="participationOptions"
                  @changeOption="changeParticipationOption"
                >
                  <template #title>
                    <h3>Teilgenommen</h3>
                  </template>
                </FilterDropDown>
                <div v-if="oneInvitationCode == false" class="">
                  <a
                    class="w-40 mt-6 flex justify-between items-center px-4 h-10 border border-transparent text-base cursor-pointer font-semibold rounded-md text-white bg-primary hover:bg-primaryAccent md:text-lg md:px-2"
                    @click="exportToExcel"
                  >
                    Exportieren
                    <DocumentArrowDownIcon
                      class="text-white ml-2 w-6 h-6"
                    ></DocumentArrowDownIcon>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="page-background">
          <div class="standard-container">
            <div class="overflow-x-auto">
              <table class="min-w-full bg-white rounded-lg">
                <thead>
                  <tr>
                    <th class="py-3 px-6 bg-primary text-white border-b">
                      Einladungs-Code
                    </th>
                    <th
                      v-if="oneInvitationCode == false"
                      class="py-3 px-6 bg-primary text-white border-b"
                    >
                      E-Mail
                    </th>
                    <th
                      v-if="oneInvitationCode == false"
                      class="py-3 px-6 bg-primary text-white border-b"
                    >
                      Generiert am
                    </th>
                    <th
                      v-if="oneInvitationCode == false"
                      class="py-3 px-6 bg-primary text-white border-b"
                    >
                      Teilgenommen
                    </th>
                    <th
                      v-if="oneInvitationCode == true"
                      class="py-3 px-6 bg-primary text-white border-b"
                    >
                      Teilnahmen
                    </th>
                  </tr>
                </thead>
                <tbody
                  v-for="(resource, index) in filteredInvitationObjects"
                  :key="resource.id"
                >
                  <tr v-if="oneInvitationCode == false" class="">
                    <td class="py-4 px-6 border-b">{{ resource.token }}</td>
                    <td
                      v-if="decryptedEmails.length < 1"
                      class="py-4 px-6 border-b text-center"
                    >
                      <div class="flex justify-center items-center h-full">
                        <LockClosedIcon
                          class="w-6 h-6 text-center text-primary"
                        ></LockClosedIcon>
                      </div>
                    </td>
                    <td
                      v-if="decryptedEmails.length > 0"
                      class="py-4 px-6 border-b text-center"
                    >
                      {{ decryptedEmails[index] }}
                    </td>

                    <td class="py-4 px-6 border-b">
                      {{ formatGermanDate(resource.date_created) }} Uhr
                    </td>

                    <!-- Cell for Participation Status -->
                    <td class="py-4 px-6 border-b text-center">
                      <div class="flex justify-center items-center h-full">
                        <div
                          v-if="resource.is_participated"
                          class="bg-green-100 w-14 h-12 rounded-lg flex justify-center items-center"
                        >
                          Ja
                        </div>
                        <div
                          v-else
                          class="bg-red-100 w-14 h-12 rounded-lg flex justify-center items-center"
                        >
                          Nein
                        </div>
                      </div>
                    </td>
                  </tr>
                  <tr v-if="oneInvitationCode == true">
                    <td class="py-4 px-6 border-b">{{ resource.token }}</td>
                    <td class="py-4 px-6 border-b">
                      {{ resource.tokenCounter }}
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div>
      <!-- Modal section -->
      <div
        v-if="uploadModalOpen"
        class="fixed inset-0 flex items-center justify-center bg-gray-500 bg-opacity-75"
      >
        <upload-modal
          @close="uploadModalOpen = false"
          @upload="handleEmails"
        ></upload-modal>
      </div>
      <div v-if="confirmationModalOpen">
        <confirmation-modal
          @close-modal="confirmationModalOpen = false"
          @save-decision="saveInvitationChoice"
        ></confirmation-modal>
      </div>
      <div v-if="removeSecurityKeyModalOpen">
        <remove-security-key-modal
          @close-modal="removeSecurityKeyModalOpen = false"
          @remove-security-key="removeSecurityKey"
        ></remove-security-key-modal>
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
    </div>
  </template>
</template>
<script>
import Hero from "@/components/base/Hero.vue";
import UploadModal from "@/components/self-service/UploadModal.vue";
import ConfirmationModal from "@/components/self-service/ConfirmationModal.vue";
import RemoveSecurityKeyModal from "@/components/self-service/RemoveSecurityKeyModal.vue";
import InvitationModeCard from "@/components/self-service/InvitationModeCard.vue";
import CampagneService from "../../services/campagne.service.js";
import { useCampagneStore } from "@/store/CampagneStore";
import FilterDropDown from "@/components/self-service/FilterDropDown.vue";
import * as XLSX from "xlsx";
import { frontendUrl } from '@/config.js'; // Make sure the path is correct based on your file structure

export default {
  components: {
    Hero,
    UploadModal,
    ConfirmationModal,
    FilterDropDown,
    InvitationModeCard,
    RemoveSecurityKeyModal,
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
    const campagneStore = useCampagneStore();

    return {
      campagneStore,
    };
  },
  data() {
    return {
      domainURL: "",
      //popup
      popupTitle: "",
      popupType: "",
      popupContent: "",

      securityKey: null,
      securityKeyActivated: true,
      form: {
        securityDisplayThreshold: 5,
        securityDisplayProfile: 1,
      },
      maxThreshold: 10, // This could be dynamically determined from other data
      maxProfile: 5, // This could be dynamically determined from other data
      oneInvitationCode: null,
      uploadModalOpen: false,
      confirmationModalOpen: false,
      removeSecurityKeyModalOpen: false,
      editInvitationModalOpen: false,
      activeTab: "upload",
      fileData: null,
      customMessage: "",
      decryptedEmails: [],
      tempDecrpytedEmail: null,
      emails: [],
      filteredInvitationObjects: [],
      invitationObjects: [],
      uploadName: "",
      uploadCount: 0,
      invitationOption: null,
      isLoading: false,
      showFailurePopUp: false,
      showSuccessPopUp: false,
      isDropdownOpen: false,
      selectedParticipationFilter: 0,
      selectedInvitationObject: null,
      participationOptions: [
        {
          id: 0,
          text: "Kein Filter",
        },
        {
          id: 1,
          text: "Ja",
        },
        {
          id: 2,
          text: "Nein",
        },
      ],
      invitationModeOptions: [
        {
          name: "Einen Einladungs-Code generieren",
          description:
            "Bei dieser Option verwenden alle Mitarbeitenden denselben Einladungs-Code, um an Ihrer ITS.kompetent Kampagne teilzunehmen.",
          benefits: [
            {
              text: "Einfache Verwaltung",
              toolTipText:
                "Ein einziger Code vereinfacht das Verwaltungsverfahren, da nur ein Code generiert, verteilt und überwacht werden muss.",
            },
            {
              text: "Verteilung des Einladungs-Codes",
              toolTipText:
                "Bei der Bewerbung der Kampagne kann sich die Kommunikation auf einen klaren Aufruf zum Handeln (Call-to-Action) konzentrieren, da es nur einen Code gibt.",
            },
          ],
          disadvantages: [
            {
              text: "Keine individuelle Nachverfolgung",
              toolTipText:
                "Es kann nicht nachverfolgt werden, wie viele Teilnehmende eingeladen wurden.",
            },
            {
              text: "Keine Erinnerungsfunktion",
              toolTipText:
                "Einzelne Personen können nicht daran erinnert werden an der ITS-Kampagne teilzunehmen.",
            },
            {
              text: "Missbrauchsrisiko",
              toolTipText:
                "Ein einziger Code könnte missbräuchlich verwendet oder übermäßig verbreitet werden.",
            },
          ],
          id: 1,
        },
        {
          name: "Mehrere Einladungs-Codes generieren",
          description:
            "Bei dieser Option bekommen alle eingeladenen Mitarbeitenden einen separaten Einladungs-Code, um an Ihrer ITS.kompetent Kampagne teilzunehmen.",
          benefits: [
            {
              text: "Individualisierte Nachverfolgung",
              toolTipText:
                "Jeder Code kann einer bestimmten Person zugeordnet werden, was eine genaue Teilnahme- und Engagementverfolgung ermöglicht.",
            },
            {
              text: "Erhöhte Sicherheit",
              toolTipText:
                "Individuelle Codes können die Sicherheit erhöhen, da der Zugriff besser kontrolliert werden kann und die Codes nicht so leicht geteilt werden können.",
            },
            {
              text: "Verantwortlichkeit",
              toolTipText:
                "Einzelne Codes fördern das Verantwortungsgefühl und die Verbindlichkeit bei der Teilnahme.",
            },
          ],
          disadvantages: [
            {
              text: "Komplexere Verwaltung",
              toolTipText:
                "Die Erstellung, Verteilung und Überwachung individueller Codes kann aufwendig und ressourcenintensiv sein.",
            },
          ],

          id: 2,
        },
      ],
    };
  },
  /**
   * Watches if selctedParticipationFilter changes
   * If it changes applyFilters is called again
   */
  watch: {
    selectedParticipationFilter() {
      this.applyFilters();
    },
  },
  /**
   * Created hook: When page is created appyFilters is called initally
   *
   */

  /**
   * Mounted hook: Called after created, sets loading state initialy true.
   * Then sets the domain URl based on development or production environment
   * Finally setCampagne and getInvitationTokens are called
   */
  async mounted() {
    this.isLoading = true;
    this.setDomain();
    await this.setCampagne();
    await this.getInvitationTokens();
    this.applyFilters();
  },
  methods: {
    validateThreshold() {
      if (this.form.securityDisplayThreshold < 1) {
        this.form.securityDisplayThreshold = 1; // Reset to min if below 5
      }
    },
    validateProfile() {
      if (this.form.securityDisplayProfile < 1) {
        this.form.securityDisplayProfile = 1;
      } else if (this.form.securityDisplayProfile > this.maxProfile) {
        this.form.securityDisplayProfile = this.maxProfile;
      }
    },
    /**
     * Sets the domainURL. This has the purpose to directly link to the competence tests with a specific invitation token
     *
     */
    setDomain() {
      this.domainURL = frontendUrl;
    },
    /**
     * Sets a campagne. If a campagne has already been created the method initializes oneInvitation code boolean and checks whether the user uses a securityKey for encrypting e-mails in the database
     * If it changes applyFilters is called again
     * @throws {Error} Throws an error when a campagne was not created, yet. In this case the view renders an option were the user can decide to generate one invitation token for all participants or an invitation token each for the participants.

    */
    async setCampagne() {
      try {
        const campagneData = await this.campagneStore.getCampagne();
        this.oneInvitationCode = campagneData.one_token_mode;
        this.securityKeyActivated = campagneData.security_key_activated;
        this.campagneStore.setCampagneStarted(true);
      } catch (error) {
        this.oneInvitationCode = null;
        this.campagneStore.setCampagneStarted(false);
      }
    },
    /**
     * Gets the invitation tokens that have been generated by the user already. If a campagne has already been created the method initializes oneInvitation code boolean and checks whether the user uses a securityKey for encrypting e-mails in the database.
     * @throws {Error} If no invitation tokens exist invitationObjects array is set to be empty.
     */
    async getInvitationTokens() {
      try {
        this.invitationObjects = await CampagneService.getInvitedEmployees();
        this.filteredInvitationObjects = this.invitationObjects;
      } catch (error) {
        this.invitationObjects = [];
      } finally {
        setTimeout(() => (this.isLoading = false), 500);
      }
    },
    /**
     * Gets the invitation tokens that have been generated by the user already. If a campagne has already been created the method initializes oneInvitation code boolean and checks whether the user uses a securityKey for encrypting e-mails in the database.
     * @throws {Error} If no invitation tokens exist invitationObjects array is set to be empty.
     */
    async openInvitationTokenGeneration() {
      if (this.invitationObjects.length > 0 && this.securityKeyActivated) {
        await this.decryptEmails()
          .then(() => {
            this.uploadModalOpen = true; // Only set true if no error occurred
          })
          // IMPLEMENT CATCHING ERROR
          .catch((error) => {
            console.error("Catching error:", error);
          });
      } else {
        this.uploadModalOpen = true;
      }
    },
    /**
     * Sets removeSecurityKeyModalOpen to true
     *
     */
    openRemoveSecurityKeyModal() {
      this.removeSecurityKeyModalOpen = true;
    },
    /**
     * Updates the active tab in the upload modal
     * @param {Object} tab The updated tab in the uploadModal.
     *
     */
    changeTab(tab) {
      this.activeTab = tab;
    },
    /**
     * Is called when the FilterDropdon component receives an updated filter value
     * @param {Object} option The updated filter option
     *
     */
    changeParticipationOption(option) {
      this.selectedParticipationFilter = option.id;
    },
    /**
     * Filters the invitation Objects by tha applied filters on participation state.
     *
     */
    applyFilters() {
      this.filteredInvitationObjects = this.invitationObjects.filter((obj) => {
        return this.checkParticipationFilter(
          obj,
          this.selectedParticipationFilter
        );
      });
      this.filteredInvitationObjects = this.filteredInvitationObjects.sort(
        (a, b) => {
          return b.is_participated === a.is_participated
            ? 0
            : b.is_participated
            ? 1
            : -1;
        }
      );
    },
    /**
     * Checks the state of the participation filter. Returns true or false
     * @param {Object} obj The invitation object.
     * @param {Number} filterValue The selected filter value of the user
     * @returns {Boolean} A boolean indicating if this invitation object has a participation stae or not
     *
     */
    checkParticipationFilter(obj, filterValue) {
      switch (filterValue) {
        case 1:
          return obj.is_participated === true;
        case 2:
          return obj.is_participated === false;
        default:
          return true; // No filtering for case 0
      }
    },
    /**
     * Applies the choice of the user when choosing between generating a campagne where all participants receive the same invitation token (option1) or get a separate invitation token (option2)
     * @param {Number} obj The invitation object.
     *
     */
    applyInvitationChoice(id) {
      this.invitationOption = id;
      if (this.invitationOption == 1 || this.invitationOption == 2) {
        this.confirmationModalOpen = true;
      }
    },
    /**
     * Triggers the saving of the invitation choice inside a confirmation modal. It the generates a security and starts to download the security key as a text file
     *
     */
    async saveInvitationChoice() {
      if (this.invitationOption == 1) {
        this.oneInvitationCode = true;
      } else if (this.invitationOption == 2) {
        this.oneInvitationCode = false;
        this.securityKey = await this.campagneStore.generateSecurityKey();
        this.downloadSecurityKey();
      }
    },
    /**
     * A method to download the security key inside a text file.
     *
     */
    downloadSecurityKey() {
      const blob = new Blob([this.securityKey], {
        type: "text/plain;charset=utf-8",
      }); // Create a blob with the string content
      const url = URL.createObjectURL(blob); // Create a URL for the blob

      // Create a temporary anchor element and trigger the download
      const anchor = document.createElement("a");
      anchor.href = url;
      anchor.download = "key.txt"; // The default filename for the download
      document.body.appendChild(anchor); // Append anchor to body.
      anchor.click(); // Trigger the download

      // Clean up
      document.body.removeChild(anchor);
      URL.revokeObjectURL(url); // Revoke the blob URL to free up resources
    },
    async removeSecurityKey() {
      await this.campagneStore
        .removeSecurityKey()
        .then(() => {
          this.popupType = "success";
          this.popupTitle = "Sicherheits-Code Entfernen";
          this.popupContent =
            "Der Sicherheits-Code wurde erfolgreich gelöscht.";
          this.showSuccessPopUp = true;
          this.securityKeyActivated = false;
          this.securityKey = "";
        })
        .catch((error) => {
          // Handle login error
          console.error(error);
          this.popupType = "danger";
          this.popupTitle = "Sicherheits-Code Entfernen";
          this.popupContent =
            "Der Sicherheits-Code konnte nicht entfernt werden.";

          this.showFailurePopUp = true;
        });
    },

    /**
     * Handles the e-mails that were uploaded to generate invitation tokens
     *
     */
    handleEmails(payload) {
      this.uploadName = payload.uploadName;
      this.uploadCount = payload.uploadCount;
      this.emails = payload.uploadedEmails;

      if (
        this.emails.length < this.form.securityDisplayThreshold &&
        this.invitationObjects < 1
      ) {
        this.popupType = "danger";
        this.popupTitle = "E-Mail hochladen";
        this.popupContent = `Bitte laden Sie mindestens ${this.form.securityDisplayThreshold} E-Mail-Adressen hoch.`;

        this.showFailurePopUp = true;
      } else {
        this.generateInvitationTokens();
      }
    },
    /**
     * A method that generates the invitation tokens
     * @throws {Error} Throws an error when the invitation tokens could not be generated and opens a popup with type danger
     *
     */
    async generateInvitationTokens() {
      // create new campagne if this is the first time the user generates invitation tokens
      if (!this.campagneStore.campagneStarted) {
        await this.campagneStore.postCampagne({
          securityDisplayThreshold: this.form.securityDisplayThreshold,
          securityDisplayProfile: this.form.securityDisplayProfile,
          oneInvitationToken: this.oneInvitationCode,
        });
      }
      if (this.oneInvitationCode == false) {
        await CampagneService.generateInvitationTokens({
          emails: this.emails,
          key: this.securityKey,
        })
          .then((response) => {
            if (this.invitationObjects.length == 0) {
              this.invitationObjects = response.invitations;
              this.popupType = "success";
              this.popupTitle = "Einladungs-Code generiert";
              this.popupContent =
                "Wir haben einen Einladungs-Code erfolgreich generiert.";
              this.showSuccessPopUp = true;
            } else {
              this.invitationObjects.push(...response.invitations);
              this.securityKey = null;
              this.decryptedEmails = [];
            }
            this.popupType = "success";
            this.popupTitle = "Einladungs-Codes generiert";
            this.popupContent =
              "Wir haben " +
              this.emails.length +
              " Einladungs-Codes für jede von Ihnen hochgeladene E-Mail-Adresse erfolgreich generiert.";
            this.showSuccessPopUp = true;
          })
          .catch((error) => {
            console.error(error);
            this.popupType = "danger";
            this.popupTitle = "Einladungs-Codes generiert";
            this.popupContent =
              "Es konnten leider keine Einladungs-Codes generiert werden.";
            this.showSuccessPopUp = true;
          });
      } else if (this.oneInvitationCode == true) {
        await CampagneService.generateInvitationTokens({})
          .then((response) => {
            this.invitationObjects = response.invitations;
          })
          .catch((error) => {
            console.error(error);
          });
      }
      this.filteredInvitationObjects = this.invitationObjects;

      this.campagneStore.setCampagneStarted(true);

      this.applyFilters();
    },
    /**
     * A method that decrypts the e-mail adresses that are stored encrypted in the database.
     * @throws {Error} Throws an error when the decryption process failed.
     *
     */
    async decryptEmails() {
      await this.campagneStore
        .decryptEmails({
          key: this.securityKey,
        })
        .then((response) => {
          this.decryptedEmails = response.decrypted_emails;
        })
        .catch((error) => {
          // Handle decryption error
          this.popupType = "danger";
          this.popupTitle = "Sicherheits-Code Ungültig";
          this.popupContent = "Der Sicherheits-Code ist ungültig.";
          this.showFailurePopUp = true;
          console.error(error);
          throw new Error("Decryption failed");
        });
    },
    /**
     * A method that prepares the data of invitation tokens inot better redable format in an excel file.
     * @return {Array} Returns the mapped array with th new worded fields for excel file generation.
     *
     */
    prepareDataForExport(dataArray) {
      return dataArray.map((item, index) => ({
        "Einladungs-Code": item.token,
        "E-Mail-Adresse": this.decryptedEmails[index],
        Teilgenommen: item.is_participated ? "Ja" : "Nein", // Convert boolean to a readable format
      }));
    },
    /**
     * A method that generates an excel file including the invitation tokens. The file can be used to invite employes to the campagne.
     * @throws {Error} Throws an error when the excel file geneartion failed.
     *
     */
    exportToExcel() {
      const dataToExport = this.prepareDataForExport(
        this.filteredInvitationObjects
      );

      // Continue with the SheetJS export process
      const worksheet = XLSX.utils.json_to_sheet(dataToExport);
      const workbook = XLSX.utils.book_new();
      XLSX.utils.book_append_sheet(workbook, worksheet, "Sheet1");

      // Trigger download
      try {
        XLSX.writeFile(workbook, "Einladungs-Codes.xlsx");
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
    /**
     * A method that formats the date time of the generation of the invitation tokens into german date time.
     * @return {Date} Returns a date in german date time
     *
     */
    formatGermanDate(dateString) {
      const date = new Date(dateString);
      const day = date.getDate().toString().padStart(2, "0");
      const month = (date.getMonth() + 1).toString().padStart(2, "0"); // Months are 0-indexed
      const year = date.getFullYear();
      const hours = date.getHours().toString().padStart(2, "0");
      const minutes = date.getMinutes().toString().padStart(2, "0");

      return `${day}.${month}.${year} ${hours}:${minutes}`;
    },
    /**
     * A method that allows to copy a blueprint e-mail text for the invitation of employees
     * @throws {Error} Throws an error when copying was not successful.
     *
     */
    copyEmailText() {
      const textToCopy = `Liebe/r Kolleg*in,
      unser Unternehmen nimmt derzeit an ITS.kompetent teil. Das Projekt ITS.kompetent unterstützt KMUs dabei, die Kompetenzen der Mitarbeiter:innen im Bereich der Informationstechnischen Sicherheit (ITS-Kompetenzen) realitätsnah zu messen und mit den berufsbezogenen Anforderungen abzugleichen. Mit Hilfe von ITS.kompetent können KMUs ihren unternehmensspezifischen Qualifizierungsbedarf ermitteln und geeignete Schulungsangebote ausarbeiten.
      Ich bitte Sie an der bestehenden Kampagne teilzunehmen. Ihr Einladungs-Code lautet: [Einladungs-Code]

      Sie erreichen unsere ITS-Kampagne unter [URL]
      Viele Grüße,
      [Ihr Name]
      ${this.companyName}`;
      navigator.clipboard.writeText(textToCopy).then(
        () => {
          this.popupType = "success";
          this.popupTitle = "Text kopieren";
          this.popupContent =
            "Der Text wurder erfolgreich in die Zwischenablage kopiert.";
          this.showSuccessPopUp = true;
        },
        (err) => {
          console.error("Could not copy text: ", err);
          this.popupType = "danger";
          this.popupTitle = "Text kopieren";
          this.popupContent = "Der Text konnte nicht kopiert werden.";
          this.showFailurePopUp = true;
        }
      );
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
