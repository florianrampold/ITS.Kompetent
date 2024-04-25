<template>
  <div class="standard-container">
    <steps :activestate="activeStep" linecolor="gray" class="pt-5"></steps>
  </div>
  <template v-if="loading">
    <spinner></spinner>
    <!-- here use a loaded you prefer -->
  </template>
  <template v-else>
    <div>
      <Hero>
        <template #title>
          <h1 v-if="activeStep == 1" class="main-heading">
            <span class="text-primary xl:inline"
              >Wählen Sie zunächst<br />
            </span>
            {{ " " }}
            <span class="text-secondary xl:inline"
              >Ihr ITS-Anforderungsprofil</span
            >
          </h1>
        </template>
        <template #content>
          <p
            v-if="activeStep == 1"
            class="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0"
          >
            Sie haben nun bereits die Arneo GmbH kennengelernt und sind mit den
            Tätigkeiten und der Struktur des KMU vertraut. Wir stellen Ihnen nun
            verschiedene Mitarbeiter*innen der Arneo GmbH vor, die
            unterschiedliche Tätigkeiten im KMU übernehmen. Schauen Sie sich
            bitte alle ITS-Anforderungssprofile an und wählen Sie dann bitte das
            passendste ITS-Anforderungprofil aus, dass Ihren Tätigkeiten im KMU
            am meisten ähnelt.
          </p>
        </template>

        <template #image>
          <transition appear name="fade">
            <div
              v-if="activeStep == 1"
              class="flex items-center justify-center grow-0 shrink-1 md:shrink-0 basis-auto mb-12 md:mb-0"
            >
              <img
                :src="require('@/assets/profile.jpg')"
                class="w-2/3 lg:w-full"
                alt="Sample image"
              />
            </div>
          </transition>
        </template>

        ></Hero
      >
      <div v-show="activeStep == 1">
        <div class="page-background">
          <div class="standard-container">
            <div
              class="grid grid-cols-1 lg:grid-cols-2 gap-10 gap-y-20 lg:gap-x-20 xl:gap-x-40"
            >
              <div v-for="jobProfile in jobProfiles" :key="jobProfile.id">
                <transition appear name="fade">
                  <job-profile-card
                    :id="jobProfile.id"
                    :name="jobProfile.job_name"
                    :tasks="jobProfile.job_tasks"
                    :description="jobProfile.job_description"
                    :label="jobProfile.id"
                    :value="selectedValue"
                    :choosing-mode="true"
                    @change="changeSelectedJobProfile"
                  />
                </transition>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
</template>

<script>
import Steps from "@/components/base/Steps.vue";
import Hero from "@/components/base/Hero.vue";
import JobProfileCard from "@/components/profile/JobProfileCard.vue";
import JobProfileService from "../../services/job_profile.service.js";
import { useJobProfileStore } from "@/store/JobProfileStore";

export default {
  components: {
    Steps,
    Hero,
    JobProfileCard,
  },
  setup() {
    const jobProfileStore = useJobProfileStore();

    return { jobProfileStore };
  },
  data() {
    return {
      loading: false,
      selectedValue: 0,
      profileSelected: false,
      showPopUp: false,
      profile: "",
      profileID: 0,
      activeStep: 1,
      jobProfiles: [],
    };
  },

  /**
   * Is called when page is mounted
   * Performs an asynchronous call to the API to get the job profiles of the database
   *
   */
  async mounted() {
    this.loading = true;
    await this.getJobProfiles();
  },
  methods: {
    /**
     * Is called when page is mounted
     * Performs an asynchronous call to the API to get the job profiles of the database
     *
     */
    async getJobProfiles() {
      try {
        this.jobProfiles = await JobProfileService.getJobProfiles();
        this.jobProfiles = this.jobProfiles.filter(
          (profile) => profile.show_job_profile === true
        );
        setTimeout(() => (this.loading = false), 500);
      } catch (error) {
        console.log(error);
      }
    },
    /**
     * Changes the selected job profile. Calls a method to route to the competence test introductio page.
     *
     * @param {object} newJobProfileID The updated ID  of the job profile .
     * @param {object} profile The updated name of the job profile

     */
    changeSelectedJobProfile(newJobProfileID, profile, profileID) {
      this.selectedValue = newJobProfileID;
      this.profile = profile;
      this.profileID = profileID;
      this.profileSelected = true;
      this.navigateToCompetenceTest();
    },

    /**
     * Routes to competence test introduction page
     *
     */
    navigateToCompetenceTest() {
      if (this.profileSelected) {
        this.activeStep += 1;

        if (this.profile != "Privatperson" && this.profile != "Consumer") {
          this.$router.push({
            name: "TestLanding",
            params: { invitationToken: this.$route.params.invitationToken },
          });
        } else {
          console.log("here");
          this.$router.push({
            name: "Test",
            params: { invitationToken: this.$route.params.invitationToken },
          });
        }

        this.jobProfileStore.setProfile(this.profile);
        this.jobProfileStore.setProfileID(this.profileID);

        window.scrollTo({ top: 0, behavior: "smooth" });
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
</style>
