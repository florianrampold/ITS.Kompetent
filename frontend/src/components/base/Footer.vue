<template>
  <footer class="text-left text-lg">
    <div class="bg-gray-200">
      <div class="standard-container">
        <div class="flex justify-between flex-col lg:flex-row py-14">
          <div class="text-primary max-w-lg">
            <img
              class="w-4/5 pb-5 exportImages"
              src="@/assets/ITS_Kompetent_Logo.svg"
              alt="Logo"
            />
            <p class="text-left">
              ITS.Kompetent bietet Mitarbeiter:innen in KMUs an ihre
              ITS-Kompetenzen zu messen. Daraufhin werden Trainingsempfehlungen
              und Statistiken zu den Ergebnissen dargestellt.
            </p>
          </div>

          <div class="mt-10">
            <h5 class="uppercase font-bold mb-2.5 text-primary">
              ITS.kompetent
            </h5>

            <ul class="list-none mb-0">
              <li>
                <router-link
                  class="text-primary"
                  to="/contact"
                  @click="checkTestMode()"
                >
                  Kontakt
                </router-link>
              </li>
              <li>
                <router-link
                  class="text-primary"
                  to="/about"
                  @click="checkTestMode()"
                >
                  Über uns
                </router-link>
              </li>
              <!--  <li>
              <a
                href="https://www.uni-goettingen.de/de/3240.html"
                target="_blank"
                class="text-primary"
                >News</a
              >
            </li> -->
            </ul>
          </div>

          <div class="mt-10">
            <h5 class="uppercase font-bold mb-2.5 text-primary">Partner</h5>

            <ul class="list-none mb-0">
              <li>
                <a
                  href="https://www.bmwi.de/Navigation/DE/Home/home.html"
                  target="_blank"
                  class="text-primary"
                  >BMWK</a
                >
              </li>
              <li>
                <a
                  href="https://www.it-sicherheit-in-der-wirtschaft.de/ITS/Navigation/DE/Home/home.html"
                  target="_blank"
                  class="text-primary"
                  >IT-Sicherheit in der Wirtschaft</a
                >
              </li>
              <li>
                <a
                  href="https://www.mittelstand-digital.de/MD/Navigation/DE/Home/home.html"
                  target="_blank"
                  class="text-primary"
                  >Mittelstand Digital</a
                >
              </li>
              <li>
                <a
                  href="https://www.uni-goettingen.de"
                  target="_blank"
                  class="text-primary"
                  >Universität Göttingen</a
                >
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <div class="text-primary text-center p-4 bg-white flex justify-evenly">
      <p>© {{ currentYear }} ITS.Kompetent</p>
      <div>
        <router-link class="font-bold" to="/impressum" @click="checkTestMode()">
          Impressum </router-link
        >|
        <router-link
          class="font-bold"
          to="/datenschutz"
          @click="checkTestMode()"
        >
          Datenschutz
        </router-link>
      </div>
    </div>
    <div class="fixed bottom-0 w-screen">
      <cookie-banner></cookie-banner>
      <!-- <vue-cookie-comply
        :preferences="preferences"
        :accept-all-label="acceptAllLabel"
        :preferences-label="preferencesLabel"
        @on-accept-all-cookies="onAccept"
        @on-save-cookie-preferences="onSavePreferences"
      >
        <template #header>
          <header>Cookie Einstellungen</header>
          <p>
            Wir verwenden Cookies und ähnliche Technologien, um Inhalte zu
            personalisieren und ein besseres Erlebnis zu bieten. Sie können sie
            anpassen, indem Sie auf die Schaltfläche Einstellungen klicken.
          </p>
        </template>

        <template #modal-header>
          <h3 class="text-center mb-2">Ihre Cookie Einstellungen</h3>
        </template>

        <template #modal-body="{ preference }">
          <div class="font-bold text-lg mb-4 mt-2">{{ preference.title }}</div>
          <p>{{ preference.description }}</p>
        </template>

        <template #modal-footer>
          <footer>My custom modal footer</footer>
        </template>
      </vue-cookie-comply> -->
    </div>
  </footer>
  <base-modal
    v-if="showModal"
    :show="showModal"
    :title="'Test beenden'"
    :content="'Möchten Sie fortfahren? Wenn sie Fortfahren klicken, wird der ITS-Kompetenztest beendet und Ihr aktueller Fortschritt geht verloren.'"
    @close="showModal = false"
    @confirm="pushToStart()"
  ></base-modal>
</template>

<script>
import { useCompetenceTestStore } from "@/store/CompetenceTestStore";
import { mapState } from "pinia";
import BaseModal from "@/components/base/BaseModal";
import CookieBanner from "@/components/base/CookieBanner";
export default {
  components: {
    BaseModal,
    CookieBanner,
  },
  setup() {
    const competenceTestStore = useCompetenceTestStore();

    return { competenceTestStore };
  },
  data() {
    return {
      showModal: false,
      currentYear: new Date().getFullYear(),
      preferences: [
        {
          title: "Technisch notwendige Cookies",
          description:
            "Cookies zur Gewährleistung der Betriebsbereitschaft können nicht deaktiviert werden, soweit wir sie verwenden, um unsere Dienste bereitzustellen. Um den Betrieb von ITS.kompetent zu gewährleisten speichern wir die Ergebnisse Ihres ITS-Kompetenztests temporär im Local Storage Ihres Browsers. Dies ist zwingend notwendig, um Ihnen die Ergebnisse der Messung zu präsentieren. Dabei werden keine persönlichen Daten verarbeitet, die Rückschluss auf Ihre Person geben. Wenn Sie dies nicht wünschen, können Sie nicht an ITS.kompetent teilnehmen. In diesem Fall schließen Sie bitte die Webseite. Wir bitten um Ihr Verständnis.",
          items: [{ label: "Aktiv", value: "performance", isRequired: true }],
        },
      ],
      headerTitle: "Cookie Einstellungen",
      preferencesLabel: "Einstellungen",
      acceptAllLabel: "Akzeptieren",
      headerDescription:
        "Wir verwenden Cookies und ähnliche Technologien, um Inhalte zu personalisieren und ein besseres Erlebnis zu bieten. Sie können sie anpassen, indem Sie auf die Schaltfläche Einstellungen klicken.",
    };
  },
  methods: {
    /**
     * Utilizes Vuex's `mapState` to bind the `getTestStarted` state from the `useCompetenceTestStore` to local component data.
     * This mapping allows the component to access `getTestStarted` directly from the component's computed properties.
     */
    ...mapState(useCompetenceTestStore, ["getTestStarted"]),
    /**
     * Ends the competence test state and removes it from local storage
     * Sets the test button to inactive.
     *
     */
    pushToStart() {
      this.competenceTestStore.endTest();
      this.competenceTestStore.setTestButtonInactive();
    },
    /**
     * Shows a modal if test has started to make the user conform to really end the competence test.
     * Sets the test button to inactive.
     *
     */
    checkTestMode() {
      if (this.competenceTestStore.testStarted) {
        this.showModal = true;
      } else {
        this.competenceTestStore.setTestButtonInactive();
      }
    },
  },
};
</script>
