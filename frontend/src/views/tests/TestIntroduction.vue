<template>
  <Hero
    ><template #title>
      <div
        class="flex justify-center items-center lg:items-start lg:justify-start"
      >
        <h1 class="main-heading">
          <span class="text-primary xl:inline">Beschreibung der<br /> </span>
          {{ " " }}
          <span class="text-secondary xl:inline"> Testumgebung</span>
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
          In dem folgenden ITS-Kompetenztest sind sie Mitarbeiter*in der
          fiktiven Arneo GmbH. Die Arneo GmbH ist ein mittelständisches
          Unternehmen, das smarte Ventilatoren herstellt. Bevor der
          ITS-Kompetenztest losgeht, schauen Sie sich bitte das unten angeführte
          Video zu ihrem fiktiven Arbeitgeber an. Sobald Sie dies getan haben
          und am Ende der Seite auf
          <strong>Weiter</strong> klicken, startet ITS.Kompetent mit der Auswahl
          Ihres ITS-Anforderungsprofils.
        </p>
      </div>
    </template>
    <template #buttons>
      <div
        class="mt-5 w-full sm:mt-8 flex flex-col sm:flex-row justify-center gap-y-4 sm:gap-4 items-center lg:justify-start"
      ></div
    ></template>

    <template #image>
      <transition appear name="fade">
        <div
          class="grow-0 shrink-1 md:shrink-0 basis-auto flex justify-center items-center mb-12 md:mb-0"
        >
          <img
            :src="require('@/assets/test_environment.jpg')"
            class="w-2/3 lg:w-full"
            alt="Sample image"
          /></div></transition
    ></template>
    <template #progress> </template>
  </Hero>
  <div class="page-background">
    <div class="standard-container flex flex-col justify-center">
      <h1 class="main-heading pb-20">Die Arneo GmbH</h1>
      <div class="flex flex-row justify-center items-center">
        <div class="border-b-4 rounded-lg w-14 border-secondary mb-10"></div>
      </div>
      <div class="flex justify-center items-center">
        <p
          class="mt-3 text-left text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
        >
          Im Folgenden sind Sie Mitarbeiter*in der Arneo GmbH. Um zu verstehen,
          wie die Arneo GmbH aufgebaut ist und in welchem Gewerbe sie tätig ist,
          schauen Sie sich bitte das untenstehende Video an, bevor Sie an
          ITS.Kompetent teilnehmen.
        </p>
      </div>
      <div class="mt-20 lg:mb-20">
        <video
          ref="videoPlayer"
          :src="require('@/assets/videos/arneo_introduction.mp4')"
          video
          controls
          @ended="onVideoEnded"
        >
          <p>
            Your browser doesn't support HTML video. Please select a different
            browser.
          </p>
        </video>
      </div>
      <div v-if="showNextButton" class="flex mt-10 justify-center items-center">
        <button
          class="w-40 transform bg-primary text-white lg:hover:scale-105 duration-500 lg:text-primary lg:bg-white border-primary font-button border-2 my-2 py-1 px-4 mx-2 rounded hover:text-white hover:bg-primary"
          @click="startTest()"
        >
          Weiter
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { useCompetenceTestStore } from "@/store/CompetenceTestStore";

import Hero from "@/components/base/Hero.vue";

export default {
  components: {
    Hero,
  },
  /**
   * Initializes and returns the state for the Vue component using composition API.
   *
   * This setup function utilizes the Vuex stores specific to job profiles and competence tests.
   * It invokes `useCompetenceTestStore` for managing state related to competence tests. The function
   * then returns these stores for use within the Vue component, enabling reactive state management
   * and encapsulation of business logic associated with competence tests.
   *
   * @returns {Object} An object containing references `competenceTestStore`.
   */
  setup() {
    const competenceTestStore = useCompetenceTestStore();

    return { competenceTestStore };
  },
  data() {
    return {
      showNextButton: true,
      invitationToken: null,
    };
  },
  /**
   * A Vue component lifecycle method that runs once the component is mounted to the DOM.
   * It asynchronously fetches different elemnts from competence tests from their respective stores.
   *
   * This method is critical for initializing the component with data required for rendering
   * job profiles and competence dimensions, fetched asynchronously from Vuex stores immediately
   * after the component has been rendered to the DOM.
   */
  mounted() {
    this.competenceTestStore.startTest();
    this.invitationToken = this.$route.params.invitationToken;
  },
  methods: {
    /**
     * Routes to ProfileLanding
     */
    startTest() {
      this.$router.push({
        name: "Profile",
        params: { invitationToken: this.invitationToken },
      });
    },
    /**
     * Starts playing the video
     */
    playVideo() {
      this.$refs.videoPlayer.play();
    },
    /**
     * Pauses the video
     */
    pauseVideo() {
      this.$refs.videoPlayer.pause();
    },
    /**
     * Shows 'Weiter' button when the video has ended
     */
    onVideoEnded() {
      this.showNextButton = true;
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
