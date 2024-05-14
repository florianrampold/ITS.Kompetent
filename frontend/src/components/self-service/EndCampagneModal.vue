<template>
  <div
    class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto overflow-x-auto h-screen w-full flex items-center justify-center"
    @click="closeModal"
  >
    <div
      class="relative mx-auto md:p-5 border w-11/12 sm:w-2/3 xl:w-1/2 overflow-y-auto overflow-x-auto shadow-lg xl:mb-20 rounded-md bg-white"
      style="max-height: calc(100vh - 4rem); overflow-y: auto"
      @click.stop
    >
      <div class="text-center">
        <!-- Header -->
        <div
          class="flex justify-between items-center border-b border-gray-200 p-3"
        >
          <h3 class="text-lg leading-6 font-medium text-gray-900">
            Kampagne beenden
          </h3>
          <button
            class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center"
            @click="closeModal"
          >
            <XMarkIcon class="h-6 w-6 text-gray-500"></XMarkIcon>
          </button>
        </div>
        <!-- Body -->
        <div class="mt-2 px-7 py-3 overflow-y-auto">
          <p class="text-left">
            Sie können sich nun dazu entscheiden die Kampagne zu beenden. Sobald
            Sie eine Kampagne beenden, können
            <strong>
              keine weiteren Personen den oder die Einladungs-Codes nutzen </strong
            >.<br />
            <br />

            Damit Ihnen Ergebnisse zu den einzelnen ITS-Anforderungsprofilen
            angezeigt werden, müssen sich aus Datenschutzgründen mindestens
            <strong> {{ securityDisplayThreshold }} </strong> Mitarbeiter*innen
            sich dem jweiligen ITS-Anforderungsprofil zugeordnet und den
            ITS-Kompetenztest abgeschlossen haben.

            <br />
            <br />
            Für die ITS-Anforderungsprofile, die grün hinterlegt sind, können
            wir einzelne Statistiken anzeigen. Für in rot hinterlegten
            ITS-Anforderungsprofile können keine spezifischen Statistiken
            generiert werden. Die aktuelle Verteilung der Teilnehmenden
            innerhalb der ITS-Anforderungsprofile können Sie der Tabelle
            entnehmen:
          </p>
          <table
            class="rounded-lg w-full text-md text-left mt-4 mb-4 px-4 bg-white"
          >
            <thead
              class="border-b pl-6 bg-primary rounded-lg text-white uppercase h-8"
            >
              <tr class="h-10">
                <th class="pl-2 w-4/12">ITS-Anforderungsprofil</th>
                <th class="px-2 w-6/12">Teilnehmende</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="profile in jobProfiles"
                :key="profile"
                class="my-4 border-b break-words"
                :class="{
                  'bg-green-100':
                    profile.number_of_participants >= securityDisplayThreshold,
                  'bg-red-100':
                    profile.number_of_participants < securityDisplayThreshold,
                }"
              >
                <td class="max-w-xs px-4 break-words">
                  {{ profile.job_profile_name }}
                </td>
                <td class="max-w-xs px-4 my-4 break-words">
                  {{ profile.number_of_participants }}
                </td>
              </tr>
            </tbody>
          </table>
          <p class="text-left">
            Alternativ haben Sie die Möglichkeit die Ergebnisse Ihrer Kampagne
            aggregiert über alle ITS-Anforderungsprofile zu erhalten.
            <br />
            <strong
              >Dies ist nur notwendig, wenn in einzelnen
              ITS-Anforderungsprofilen weniger als
              {{ securityDisplayThreshold }} Personen teilgenommen haben und sie
              die Daten auch von diesen ITS-Anforderungsprofilen in der
              Auswertung berücksichtigen möchten.
              <span v-if="isDisabled" class="font-semibold"
                >Dies trifft in diesem Fall zu!</span
              >
              <br />
              Dazu setzen Sie einen Haken bei der unten gelisteten Checkbox.
            </strong>
          </p>

          <div class="col-span-2 flex items-center justify-start mt-5 mb-4">
            <input
              id="consentCheckbox"
              v-model="consentGiven"
              type="checkbox"
              class="mr-5"
            />
            <label for="consentCheckbox" class="pt-2 text-md">
              Ich möchte die Ergebnisse aggregiert über alle
              ITS-Anforderungsprofile erhalten. Ich bin mir bewusst, dass in
              diesem Fall keine einzelnen Statistiken für die
              ITS-Anforderungsprofile mit weniger als
              {{ securityDisplayThreshold }} Teilnehmenden angezeigt werden
              können.
            </label>
          </div>
        </div>
        <!-- Footer -->
        <div class="border-t flex justify-center border-gray-200 px-4 py-3">
          <button
            :class="{
              'bg-gray-200 text-primary cursor-not-allowed': isDisabled,
              'bg-secondary hover:bg-secondaryAccent': !isDisabled,
            }"
            class="px-4 py-2 text-white text-base font-medium rounded-md w-64 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-300"
            :disabled="isDisabled"
            @click="confirm"
          >
            Kampagne beenden
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    jobProfiles: {
      type: Array,
      default: () => [],
    },
    securityDisplayThreshold: {
      type: Number,
      default: 0,
    },
  },
  emits: ["close-modal", "end-campaign"],

  data() {
    return {
      showModal: false,
      consentGiven: false,
    };
  },
  computed: {
    /**
     * A computed property that set upload button to disabled if there is no file data
     */
    isDisabled() {
      let profiles = Object.values(this.jobProfiles).filter(
        (obj) => obj.number_of_participants >= this.securityDisplayThreshold
      );
      if (profiles.length > 0 || this.consentGiven) {
        return false;
      } else {
        return true;
      }
    },
  },


  methods: {
    /**
     * Closes the modal.
     */
    closeModal() {
      this.showModal = false;
      this.$emit("close-modal"); // Emit an event for the parent component
    },
    /**
     * Confirs the decision to remove the security key and emits the event to the parent component.
     */
    confirm() {
      this.$emit("end-campaign", this.consentGiven); // Emit an event for the parent component

      this.closeModal();
    },
  },
};
</script>
