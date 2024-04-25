<template>
  <Hero
    ><template #title>
      <div
        class="flex justify-center items-center lg:items-start lg:justify-start"
      >
        <h1 class="main-heading">
          <span class="text-primary font-semibold">Willkommen bei <br /> </span>
          {{ " " }}
          <span class="text-secondary xl:inline">ITS.Kompetent</span>
        </h1>
      </div>
    </template>
    <template #content>
      <h2 class="mt-5">
        <span
          class="text-gray-500 text-xl sm:text-2xl md:text-3xl font-semibold"
        >
          IT-gestützte Messung von Informationssicherheitskompetenzen
          (ITS-Kompetenzen). <br />
        </span>
      </h2>
      <div
        class="flex justify-center items-center lg:items-start lg:justify-start"
      >
        <p
          class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl md:mt-5 md:text-xl lg:mx-0"
        >
          ITS.Kompetent bestimmt die individuellen ITS-Kompetenzen Ihrer
          Mitarbeiter*innen, ausgerichtet auf individuelle
          ITS-Anforderungsprofile. Sie haben bereits eine Kampagne für Ihr KMU
          initiiert? Dann können Sie sich hier einloggen.
        </p>
      </div>
    </template>
    <template #buttons>
      <div
        class="flex justify-center items-center lg:items-start lg:justify-start"
      >
        <div class="sm:w-2/5 md:w-2/5 w-3/5 2xl:w-2/6">
          <a
            v-if="!loggedIn"
            href="#"
            class="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-secondary hover:bg-secondaryAccent mt-12 md:py-4 md:text-lg md:px-10"
            @click="goToSelfServiceLogin"
          >
            Einloggen
          </a>
          <a
            v-if="loggedIn"
            href="#"
            class="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-secondary hover:bg-secondaryAccent mt-12 md:py-4 md:text-lg md:px-10"
            @click="goToSelfServiceLogin"
          >
            KMU-Management Portal
          </a>
        </div>
      </div>
    </template>
    <template #image>
      <transition appear name="fade">
        <div class="grow-0 shrink-1 md:shrink-0 basis-auto mb-12 md:mb-0">
          <img
            src="@/assets/home.jpg"
            class="w-full"
            alt="Sample image"
          /></div></transition
    ></template>
  </Hero>
  <main class="bg-white pt-40 pb-20">
    <h1 class="main-heading pb-20">Unser Ansatz</h1>
    <div class="flex flex-row justify-center items-center">
      <div class="border-b-4 rounded-lg w-14 border-secondary mb-40"></div>
    </div>

    <div class="standard-container">
      <div
        class="flex flex-col sm:flex-row justify-center lg:justify-start flex-wrap"
      >
        <div class="w-full lg:w-1/2 text-center lg:text-left divide-secondary">
          <h1 class="main-heading">
            <span class="text-primary xl:inline">Beschreibung<br /> </span>
          </h1>
          <p
            class="pt-8 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
          >
            Das Projekt ITS.Kompetent unterstützt KMUs dabei, die Kompetenzen
            der Mitarbeiter*innen im Bereich der Informationstechnischen
            Sicherheit (ITS-Kompetenzen) realitätsnah zu messen und mit den
            berufsbezogenen Anforderungen abzugleichen. Mit Hilfe von
            ITS.Kompetent können KMUs ihren unternehmensspezifischen
            Qualifizierungsbedarf ermitteln und geeignete Schulungsangebote
            ausarbeiten. Dazu wurde ein online-gestütztes ITS-Analysetool mit
            Hilfe von wissenschaftlichen Methoden entwickelt und hiermit KMUs
            zur Verfügung gestellt. Das Tool integriert Anforderungen, Methoden
            zur Kompetenzmessung und Vorschläge für Weiterbildungsmaßnahmen.
          </p>
        </div>
        <transition appear name="fade">
          <div
            class="grow-0 shrink-1 md:shrink-0 basis-auto xl:w-6/12 lg:w-6/12 md:w-6/12 mt-10 mb-12 md:mb-0"
          >
            <img
              src="@/assets/lifecycle.svg"
              class="w-full"
              alt="Matching of ITS-competencies"
            /></div
        ></transition>
      </div>

      <div class="flex sm:flex-row justify-center flex-wrap"></div>
    </div>
  </main>
  <div class="page-background pb-40">
    <div class="grid grid-cols-1">
      <h1 class="main-heading pb-20 pt-40">Unsere Services</h1>
      <div class="flex flex-row justify-center items-center">
        <div class="border-b-4 rounded-lg w-14 border-secondary mb-40"></div>
      </div>
      <h1
        class="text-xl tracking-tight font-extrabold text-secondary flex items-center justify-center sm:text-3xl md:text-4xl py-20"
      >
        Für KMUs
      </h1>
    </div>
    <div class="standard-container">
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-10 lg:gap-20 xl:gap-40">
        <IconCard
          ><template #title
            >Analyse der ITS-Kompetenzen Ihrer Mitarbeiter*innen
          </template>
          <template #icon>
            <MagnifyingGlassIcon
              class="h-32 w-32 text-secondary hover:text-secondaryAccent"
            >
            </MagnifyingGlassIcon>
          </template>
        </IconCard>
        <IconCard
          ><template #title
            >Abruf von ITS-Kompetenzen der Mitarbeiter*innen auf freiwilliger
            Basis
          </template>
          <template #icon>
            <ChartBarIcon
              class="h-32 w-32 text-secondary hover:text-secondaryAccent"
            >
            </ChartBarIcon>
          </template>
        </IconCard>
      </div>
      <h1
        class="text-xl tracking-tight font-extrabold text-secondary flex items-center justify-center sm:text-3xl md:text-4xl py-20"
      >
        Für KMU-Mitarbeiter*innen
      </h1>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-10 lg:gap-20 xl:gap-40">
        <IconCard
          ><template #title
            >Erhalten Sie umfassende Statistiken zu ihren
            ITS-Fertigkeiten</template
          >
          <template #icon>
            <DocumentChartBarIcon
              class="h-32 w-32 text-secondary hover:text-secondaryAccent"
            >
            </DocumentChartBarIcon>
          </template>
        </IconCard>
        <IconCard
          ><template #title>Ermitteln Sie Ihre ITS-Kompetenzen </template>
          <template #icon>
            <ShieldCheckIcon
              class="h-32 w-32 text-secondary hover:text-secondaryAccent"
            >
            </ShieldCheckIcon>
          </template>
        </IconCard>
      </div>
    </div>
  </div>

  <main class="bg-white pt-40 pb-20">
    <div class="standard-container">
      <h1 class="main-heading pb-20">Nutzen für KMUs</h1>
      <div class="flex flex-row justify-center items-center">
        <div class="border-b-4 rounded-lg w-14 border-secondary mb-40"></div>
      </div>
      <div
        class="flex flex-col sm:flex-row justify-center lg:justify-start flex-wrap"
      >
        <div class="w-full lg:w-1/2 text-center lg:text-left divide-secondary">
          <h1 class="main-heading">
            <span class="text-primary xl:inline"
              >Matching von Anforderungsprofilen mit ITS-Kompetenzen<br />
            </span>
          </h1>
          <p
            class="pt-8 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
          >
            ITS.Kompetent ermöglicht die Identifizierung des KMU-spezifischen
            ITS-Qualifizierungsbedarfs durch einen Stellenprofilvergleich und
            die anschließende Auswahl passgenauer ITS-Ausbildungsangebote. Mit
            Hilfe von ITS.Kompetent gewinnen KMU Transparenz hinsichtlich der
            drei Fragen: Welche ITS-Kompetenzen werden bei welchen Mitarbeitern
            benötigt (Was?), wo liegt der berufsspezifische und
            unternehmensweite ITS-Qualifizierungsbedarf (Wo?) und wie können die
            fehlenden Kompetenzen effektiv aufgebaut werden (Wie?).
          </p>
        </div>
        <transition appear name="fade">
          <div
            class="grow-0 shrink-1 md:shrink-0 basis-auto xl:w-6/12 lg:w-6/12 md:w-6/12 mb-12 md:mb-0"
          >
            <img
              :src="require('@/assets/matching.jpg')"
              class="w-full"
              alt="Matching of ITS-competencies"
            /></div
        ></transition>
      </div>
      <div
        class="flex flex-col sm:flex-row justify-center lg:justify-end flex-wrap pt-40"
      >
        <transition appear name="fade">
          <div
            class="grow-0 shrink-1 md:shrink-0 basis-auto xl:w-6/12 lg:w-6/12 md:w-6/12 mb-12 md:mb-0"
          >
            <img
              src="@/assets/analytics.jpg"
              class="w-full"
              alt="ITS.kompetent analytics"
            /></div
        ></transition>
        <div class="w-full lg:w-1/2 text-center lg:text-left divide-secondary">
          <h1 class="main-heading">
            <span class="text-primary xl:inline"
              >Detaillierte Statistiken über Mitarbeiter*innen-Kompetenzen
              <br />
            </span>
          </h1>
          <p
            class="pt-8 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
          >
            ITS.Kompetent stellt Ihren Mitarbeiter*innen ein
            benutzerfreundliches Dashboard zur Verfügung, das Informationen über
            den IST-Zustand der ITS-Kompetenzen für Mitarbeiter*innen aus
            verschiedenen Stellenprofilen enthält.
          </p>
        </div>
      </div>
      <div class="flex sm:flex-row justify-center flex-wrap"></div>
    </div>
  </main>
</template>
<script>
import Hero from "@/components/base/Hero.vue";
import IconCard from "@/components/base/IconCard.vue";
import { MagnifyingGlassIcon } from "@heroicons/vue/20/solid";
import { ChartBarIcon } from "@heroicons/vue/20/solid";
import { DocumentChartBarIcon } from "@heroicons/vue/20/solid";
import { ShieldCheckIcon } from "@heroicons/vue/20/solid";
import { useCompetenceTestStore } from "@/store/CompetenceTestStore";
import { useAuthStore } from "@/store/AuthStore";

export default {
  components: {
    Hero,
    IconCard,
    MagnifyingGlassIcon,
    ChartBarIcon,
    DocumentChartBarIcon,
    ShieldCheckIcon,
  },
  setup() {
    const competenceTestStore = useCompetenceTestStore();
    const authStore = useAuthStore();

    return { competenceTestStore, authStore };
  },
  data() {
    return {
      loggedIn: false,
      imageLoaded: false,
    };
  },
  /**
   * Performs necessary logic to set information that the competence test ended
   *
   */
  beforeMount() {
    this.competenceTestStore.endTest();
    this.competenceTestStore.setTestButtonInactive();
    this.competenceTestStore.setGetStartedButtonInactive();
    this.competenceTestStore.setCompetenceTestResult({});
  },
  /**
   * Sets loggedIn state when the Home vue mounts
   *
   */
  mounted() {
    this.loggedIn = this.authStore.isLoggedIn;
  },
  methods: {
    /**
     * Navigates to the Login page.
     *
     */
    goToSelfServiceLogin() {
      this.$router.push({ name: "Login" });
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
