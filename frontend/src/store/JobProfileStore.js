import { defineStore } from "pinia";
import jobProfileService from "../services/job_profile.service";
export const useJobProfileStore = defineStore("JobProfileStore", {
  state: () => {
    return {
      profile: "",
      profileID: undefined,
    };
  },

  getters: {
    /**
     * Getter to retrieve the profile.
     * @return {Object} The profile
     */
    getProfile() {
      return this.profile;
    },
    /**
     * Getter to retrieve the profile ID.
     * @return {Number} The profile ID
     */
    getProfileID() {
      return this.profileID;
    },
  },
  actions: {
    /**
     * Sets the profile
     * @param {Object} profile The job profile
     */
    setProfile(profile) {
      this.profile = profile;
    },
    /**
     * Sets the profile ID
     * @param {Object} profileID The job profile ID
     */
    setProfileID(profileID) {
      this.profileID = profileID;
    },
    /**
     * Gets the job profiles form the AOI
     * @returns {Promise<Object>} A promise that resolves to the job profiles.
     */
    async getJobProfiles() {
      try {
        const response = await jobProfileService.getJobProfiles();
        return response;
      } catch (error) {
        console.log(error);
      }
    },
  },
});
