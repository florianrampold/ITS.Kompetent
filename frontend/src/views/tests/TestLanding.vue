<template>
  <div>
    <div class="standard-container mb-5">
      <steps :activestate="activeStep" linecolor="gray" class="pt-10"></steps>
    </div>

    <Hero>
      <template #title>
        <div
          class="flex justify-center items-center lg:justify-start flex-wrap"
        >
          <h1 v-if="activeStep == 2" class="main-heading">
            <span class="text-primary"
              >Willkommen bei dem ITS-Kompetenztest <br />
            </span>
            {{ " " }}
            <span class="text-secondary"
              >für das ITS-Anforderungsprofil {{ profile }}
            </span>
          </h1>
        </div>
      </template>
      <template #content>
        <p
          v-if="activeStep == 2"
          class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
        >
          Sie konnten sich am ehesten mit dem ITS-Anforderungsprofil
          {{ profile }} identifizieren. Der ITS-Kompetenztest basiert auf den
          standardmäßigen Tätigkeiten des von Ihnen gewählten Profils. Damit Sie
          sich bestmöglich in die Situation hineinversetzen können, schauen Sie
          sich bitte das Video weiter unten auf dieser Seite an. Sobald Sie das
          Video bis zum Ende gesehen haben, erscheint ein Button und sie können
          den ITS-Kompetenztest starten!
        </p>

        <p
          v-if="activeStep == 2"
          class="mt-3 text-base text-gray-500 sm:mt-5 font-bold sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
        >
          Achtung: Aus Datenschutzgründen haben Sie keine Möglichkeit den
          ITS-Kompetenztest abzubrechen und wiederaufzunehmen! Wir speichern
          Ihre Eingaben nur temporär, sobald Sie die Seite schließen gehen Ihre
          Ergebnisse verloren. Erst wenn der ITS-Kompetenztest beendet ist, werden ihre Ergebnisse der erstellten ITS-Kampagne zugerodnet und anonymisiert gespeichert.
        </p>
      </template>
      <template #buttons> </template>
      

      ></Hero
    >
    <div class="page-background">
      <div class="standard-container flex flex-col justify-center">
        <h1 class="main-heading pb-20">Ihr Anforderungsprofil</h1>
        <div class="flex flex-row justify-center items-center">
          <div class="border-b-4 rounded-lg w-14 border-secondary mb-10"></div>
        </div>
        <div class="flex justify-center items-center">
          <p
            class="mt-3 text-left text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
          >
            Im Folgenden versetzen Sie sich bitte in die Situation der fiktiven
            Person, die im Video vorgestellt wird. Sie werden im folgenden mit
            verschiedenen ITS-Bedrohungen konfrontiert, in denen Sie variabel
            reagieren müssen. Zu den Szenarien werden Ihnen unterschiedliche
            Fragen gestellt. Beantworten Sie die Fragen bitte so ehrlich wie
            möglich.
          </p>
        </div>
        <div class="mt-20 mb-20">
          <div v-if="profile == 'Außendienst'">
            <video
              ref="videoPlayer"
              :src="require('@/assets/videos/introduction_4.mp4')"
              controls
              @ended="onVideoEnded"
            >
              <p>
                Your browser doesn't support HTML video. Please select a
                different browser.
              </p>
            </video>
          </div>
          <div v-if="profile == 'Innendienst'">
            <video
              ref="videoPlayer"
              :src="require('@/assets/videos/introduction_2.mp4')"
              controls
              @ended="onVideoEnded"
            >
              <p>
                Your browser doesn't support HTML video. Please select a
                different browser.
              </p>
            </video>
          </div>
          <div v-if="profile == 'Führungskraft'">
            <video
              ref="videoPlayer"
              :src="require('@/assets/videos/introduction_3.mp4')"
              controls
              @ended="onVideoEnded"
            >
              <p>
                Your browser doesn't support HTML video. Please select a
                different browser.
              </p>
            </video>
          </div>
          <div v-if="profile == 'IT-Admin'">
            <video
              ref="videoPlayer"
              :src="require('@/assets/videos/introduction_5.mp4')"
              controls
              @ended="onVideoEnded"
            >
              <p>
                Your browser doesn't support HTML video. Please select a
                different browser.
              </p>
            </video>
          </div>
          <div v-if="profile == 'Geschäftsführer*in'">
            <video
              ref="videoPlayer"
              :src="require('@/assets/videos/introduction_1.mp4')"
              controls
              @ended="onVideoEnded"
            >
              <p>
                Your browser doesn't support HTML video. Please select a
                different browser.
              </p>
            </video>
          </div>
        </div>
        <div v-if="showButton" class="flex justify-center items-center">
          <button
            class="w-40 transform bg-primary text-white lg:hover:scale-105 duration-500 lg:text-primary lg:bg-white border-primary font-button border-2 my-2 py-1 px-4 mx-2 rounded hover:text-white hover:bg-primary"
            @click="startTest()"
          >
            Los geht's
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Steps from "@/components/base/Steps.vue";
import Hero from "@/components/base/Hero.vue";
import { useJobProfileStore } from "@/store/JobProfileStore";
import { useCompetenceTestStore } from "@/store/CompetenceTestStore";

import { mapState } from "pinia";
export default {
  components: {
    Steps,
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
      activeStep: 2,
      profile: "",
      profileID: 0,
      showButton: true,
      autoplay: false,
    };
  },
  /**
   * A Vue component lifecycle method that runs once the component is mounted to the DOM.
   */
  mounted() {
    this.profile = this.getProfile();
    this.profileID = this.getProfileID();
    this.catchError(this.profileID);

  },
  methods: {
    /**
     * Utilizes Vuex's `mapState` to bind the `getProfile` state from the `useJobProfileStore` to local component data.
     * This mapping allows the component to access `getProfile` directly from the component's computed properties.
     */
    ...mapState(useJobProfileStore, ["getProfile"]),
    /**
     * Utilizes Vuex's `mapState` to bind the `getProfileID` state from the `useJobProfileStore` to local component data.
     * This mapping allows the component to access `getProfileID` directly from the component's computed properties.
     */
    ...mapState(useJobProfileStore, ["getProfileID"]),
    /**
     * Routes to Test
     */
    startTest() {
      this.$router.push({
        name: "Test",
        params: { invitationToken: this.$route.params.invitationToken },
      });
    },
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
      this.showButton = true;
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
