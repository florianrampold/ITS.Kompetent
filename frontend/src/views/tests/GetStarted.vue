<template>
  <PopUp
    v-if="showPopUp"
    type="danger"
    title="Ungültiger Einladungs-Code"
    content="Dieser Einladungs-Code ist ungültig. Bitte geben Sie einen gültigen Einladungs-Code ein."
    @popup-closed="closePopUp"
  />
  <Hero
    ><template #title>
      <div
        class="flex justify-center items-center lg:items-start lg:justify-start"
      >
        <h1 class="main-heading">
          <span class="text-primary xl:inline">ITS.Kompetent<br /> </span>
          {{ " " }}
          <span class="text-secondary xl:inline">erklärt</span>
        </h1>
      </div>
    </template>

    <template #content>
      <div
        class="flex justify-center items-center lg:items-start lg:justify-start"
      >
        <p
          class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
        >
          ITS.Kompetent ist ein Analyse-Tool zur Bestimmung der ITS-Kompetenzen
          von Mitarbeiter*innen in KMUs. Dazu ist ITS.Kompetent in 4 Schritte
          untergliedert, die weiter unten auf dieser Seite näher erklärt werden.
        </p>
      </div>
    </template>
    <template #buttons> </template>

    <template #image>
      <transition appear name="fade">
        <div class="grow-0 shrink-1 md:shrink-0 basis-auto mb-12 md:mb-0">
          <img
            :src="require('@/assets/test_overview.jpg')"
            class="w-full"
            alt="Sample image"
          /></div></transition
    ></template>
    <template #progress> </template>
  </Hero>

  <div class="page-background">
    <div class="standard-container flex flex-col justify-center">
      <h1 class="main-heading pb-20">
        <span class="text-primary xl:inline">In 4 Schritten</span>
        {{ " " }}
        <span class="text-secondary xl:inline">zum Ergebnis</span>
      </h1>
      <div class="flex flex-row justify-center items-center">
        <div class="border-b-4 rounded-lg w-14 border-secondary mb-10"></div>
      </div>
      <div class="flex justify-center items-center mb-20">
        <p
          class="mt-3 text-left text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
        >
          ITS.kompetent ist in 4 Schritte untergliedert. Im ersten Schritt
          wählen Sie Ihr ITS-Anforderungsprofil aus. Danach werden Ihre
          ITS-Kompetenzen basierend auf dem ausgewählten ITS-Anforderungsprofil
          bestimmt. Im dritten Schritt zeigen wir Ihnen umfassende Statistiken
          zu den Ergebnissen Ihrer ITS-Kompetenzmessung. Zuletzt erhalten Sie
          ITS-Trainingsempfehlungen, die Ihre bisherigen ITS-Kenntnisse
          verbessern können.
        </p>
      </div>

      <Steps class="mb-40" linecolor="white"></Steps>
    </div>
  </div>
  <div class="standard-container pb-20 flex flex-col justify-center">
    <h1 class="main-heading pt-20 pb-20">
      <span class="text-primary xl:inline">Teilnahme</span>
      {{ " " }}
      <span class="text-secondary xl:inline">an ITS.Kompetent</span>
    </h1>
    <div class="flex flex-row justify-center items-center">
      <div class="border-b-4 rounded-lg w-14 border-secondary mb-10"></div>
    </div>
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 gap-y-20 lg:gap-x-20">
      <test-mode
        :value="selectedValue"
        :label="2"
        :invitation-token="invitationToken"
        description="Haben Sie bereits eine Einladung erhalten an ITS.Kompetent teilzunehmen? Dann sind Sie hier genau richtig. Geben Sie ihren Einladungs-Code in das entsprechende Feld ein und beginnen Sie mit Ihrem ITS-Kompetenztest noch heute."
        name="An einer bestehenden Kampagne teilnehmen"
        @change="changeTestMode"
        @input="checkInvitationToken"
      ></test-mode>
      <test-mode
        :value="selectedValue"
        :label="1"
        description="Sie haben Interesse, dass Ihr KMU an ITS.Kompetent teilnimmt oder möchten im Voraus einen Einblick in unsere ITS-Kompetenztests erhalten? Dann wählen Sie diese Option und nehmen erfolgreich an ITS.Kompetent teil!"
        name="ITS.Kompetent als Testversion ausprobieren"
        @change="changeTestMode"
      ></test-mode>
    </div>
  </div>
</template>

<script>
import { useCompetenceTestStore } from "@/store/CompetenceTestStore";
import { useCampagneStore } from "@/store/CampagneStore";
import Hero from "@/components/base/Hero.vue";
import Steps from "@/components/base/Steps.vue";
import TestMode from "@/components/campagne/TestMode.vue";

export default {
  components: {
    Hero,
    TestMode,
    Steps,
  },
  setup() {
    const competenceTestStore = useCompetenceTestStore();
    const campagneStore = useCampagneStore();

    return { competenceTestStore, campagneStore };
  },
  data() {
    return {
      selectedValue: 1,
      invitationToken: null,
      invitationTokenValid: false,
      showPopUp: false,
    };
  },

  methods: {
    /**
     * Starts the test by routing to TestIntroduction.
     * Before it checks if selectedValue is 1 or 2 (1 for ITS.kompetent as a test version, 2 for saving the results with invitation token to a campagne)
     */
    async startTest() {
      if (this.selectedValue == 1) {
        this.$router.push({
          name: "TestIntroduction",
        });
        this.competenceTestStore.setTestButtonActive();
      } else if (this.selectedValue == 2) {
        this.invitationTokenValid =
          await this.campagneStore.validateInvitationToken(
            this.invitationToken
          );

        if (!this.invitationTokenValid) {
          this.showPopUp = true;
        } else {
          this.$router.push({
            name: "TestIntroduction",
            params: { invitationToken: this.invitationToken },
          });
        }

        this.competenceTestStore.setGetStartedButtonActive();
      }
    },
    /**
     * Changes the TestMode. TestMode component emits the new value. Then it calls startTest.
     * @param {Number} newValue The updated value emited from TestMode.
     */
    changeTestMode(newValue) {
      this.selectedValue = newValue;
      this.startTest();
    },
    /**
     * On input the invitationToken is set to the user input
     * @param {string} invitationToken The invitationToken input by the user
     */
    async checkInvitationToken(invitationToken) {
      this.invitationToken = invitationToken;
    },
    /**
     * Closes the PopUp component on click.
     */
    closePopUp() {
      this.showPopUp = false;
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
.coming-soon-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5); /* semi-transparent black overlay */
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-weight: bold;
  z-index: 1; /* ensure it's above the card content */
  pointer-events: none;
}
</style>
