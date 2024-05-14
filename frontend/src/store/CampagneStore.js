import { defineStore } from "pinia";
import campagneService from "../services/campagne.service";
//import { useStorage } from "@vueuse/core";
import { useAuthStore } from "./AuthStore";
export const useCampagneStore = defineStore("campagne", {
  state: () => {
    return {
      campagneStarted: false,
      campagneEnded: false,
    };
  },
  getters: {
    /**
     * Getter to retrieve a boolean value if a campagne has been started
     * @return {Boolean} True if yes, False if not.
     */
    getCampagneStarted() {
      return this.campagneStarted;
    },
  },
  actions: {
    /**
     * Removes campagne state
     */
    removeCampagneStarted() {
      this.campagneStarted = false;
    },
    /**
     * Removes campagne state
     */
    setCampagneStarted(value) {
      this.campagneStarted = Boolean(value);
    },
    /**
     * Ends a campaign
     */
    setCampagneEnded() {
      this.campagneEnded = true;
    },
    /**
     * Ends a campaign
     */
    setCampagneEndedBack() {
      this.campagneEnded = false;
    },

    /**
     * Generates invitation tokens and calls the campagneService to perform the action
     */
    async generateInvitationTokens({ emails = [] }) {
      const payload = {};
      const auth = useAuthStore();

      // Include emails only if it's provided and not empty
      if (emails && emails.length > 0) {
        payload.emails = emails;
      }

      try {
        const response = await campagneService.generateInvitationTokens({
          payload,
        });
        return response.data;
      } catch (error) {
        if (error.response && error.response.status === 403) {
          auth.logout();
        } else {
          throw error;
        }
      }
    },
    /**
     * Asynchronously posts competence test results.
     * @param {Object} results - The results object to be posted.
     * @throws {Error} If posting the results fails.
     */
    async postCompetenceTestResults(results) {
      try {
        await campagneService.postCompetenceTestResults(results);
      } catch (error) {
        console.error("Error during posting the competence test result", error);
        throw error;
      }
    },

    /**
     * Asynchronously retrieves competence test results for a specified profile ID.
     * @param {string} profileID - The ID of the profile to fetch results for.
     * @returns {Promise<Object>} A promise that resolves to the fetched test results.
     */
    async getCompetenceTestResults(profileID) {
      const auth = useAuthStore();

      try {
        return await campagneService.getCompetenceTestResults(profileID);
      } catch (error) {
        if (
          (error.response && error.response.status === 403) ||
          error.response.status === 401
        ) {
          auth.logout();
        }
      }
    },

    /**
     * Asynchronously fetches participants per profile.
     * @returns {Promise<Object>} A promise that resolves to the list of participants per profile.
     */
    async getParticipantsPerProfile() {
      const auth = useAuthStore();
      try {
        return await campagneService.getParticipantsPerProfile();
      } catch (error) {
        if (
          (error.response && error.response.status === 403) ||
          error.response.status === 401
        ) {
          auth.logout();
        }
      }
    },

    /**
     * Asynchronously retrieves a list of invited employees.
     * @returns {Promise<Object>} A promise that resolves to the list of invited employees.
     */
    async getInvitedEmployees() {
      const auth = useAuthStore();
      try {
        return await campagneService.getInvitedEmployees();
      } catch (error) {
        if (
          (error.response && error.response.status === 403) ||
          error.response.status === 401
        ) {
          auth.logout();
        }
      }
    },

    /**
     * Validates an invitation token asynchronously.
     * @param {string} token - The invitation token to validate.
     * @returns {Promise<Object>} A promise that resolves to the validation result.
     */
    async validateInvitationToken(token) {
      const auth = useAuthStore();
      try {
        return await campagneService.validateInvitationToken(token);
      } catch (error) {
        if (
          (error.response && error.response.status === 403) ||
          error.response.status === 401
        ) {
          auth.logout();
        }
      }
    },

    /**
     * Asynchronously deletes a campaign.
     * @throws {Error} If the deletion fails.
     */
    async deleteCampagne() {
      const auth = useAuthStore();

      try {
        await campagneService.deleteCampagne();
      } catch (error) {
        if (
          (error.response && error.response.status === 403) ||
          error.response.status === 401
        ) {
          auth.logout();
        } else {
          throw error;
        }
      }
    },

    /**
     * Asynchronously posts a new campaign with a specified invitation token.
     * @param {string} oneInvitationToken - The token to use for the new campaign.
     * @throws {Error} If posting the campaign fails.
     */
    async postCampagne(data) {
      const auth = useAuthStore();
      try {
        await campagneService.postCampagne(data);
      } catch (error) {
        if (
          (error.response && error.response.status === 403) ||
          error.response.status === 401
        ) {
          auth.logout();
        } else {
          throw error;
        }
      }
    },

    /**
     * Asynchronously removes a security key.
     * @throws {Error} If removing the security key fails.
     */
    async removeSecurityKey() {
      const auth = useAuthStore();

      try {
        await campagneService.removeSecurityKey();
      } catch (error) {
        if (
          (error.response && error.response.status === 403) ||
          error.response.status === 401
        ) {
          auth.logout();
        } else {
          throw error;
        }
      }
    },
    /**
     * Asynchronously ends the campaign.
     * @throws {Error} If ending the campaign fails.
     */
    async endCampaign(data) {
      const auth = useAuthStore();

      try {
        await campagneService.endCampaign(data);
      } catch (error) {
        if (
          (error.response && error.response.status === 403) ||
          error.response.status === 401
        ) {
          auth.logout();
        } else {
          throw error;
        }
      }
    },
    /**
     * Asynchronously ends the campaign.
     * @throws {Error} If ending the campaign fails.
     */
    async invalidateInvitationTokens() {
      const auth = useAuthStore();

      try {
        await campagneService.invalidateInvitationTokens();
      } catch (error) {
        if (
          (error.response && error.response.status === 403) ||
          error.response.status === 401
        ) {
          auth.logout();
        } else {
          throw error;
        }
      }
    },

    /**
     * Asynchronously retrieves campaign details.
     * @returns {Promise<Object>} A promise that resolves to the campaign details.
     */
    async getCampagne() {
      const auth = useAuthStore();

      try {
        return await campagneService.getCampagne();
      } catch (error) {
        if (error.response && error.response.status === 401) {
          auth.logout();
        }
      }
    },

    /**
     * Asynchronously generates a security key.
     * @returns {Promise<Object>} A promise that resolves to the generated security key.
     */
    async generateSecurityKey() {
      const auth = useAuthStore();

      try {
        return await campagneService.generateSecurityKey();
      } catch (error) {
        if (error.response && error.response.status === 401) {
          auth.logout();
        }
      }
    },

    /**
     * Asynchronously decrypts emails with provided data.
     * @param {Object} data - The data needed for decryption.
     * @returns {Promise<Object>} A promise that resolves to the decrypted emails.
     * @throws {Error} If decryption fails.
     */
    async decryptEmails(data) {
      const auth = useAuthStore();

      try {
        const response = await campagneService.decryptEmails(data);
        return response;
      } catch (error) {
        if (
          (error.response && error.response.status === 403) ||
          error.response.status === 401
        ) {
          auth.logout();
        } else {
          throw error;
        }
      }
    },

    /**
     * Asynchronously fetches the management report.
     * @returns {Promise<Object>} A promise that resolves to the management report.
     */
    async getManagementReport() {
      const auth = useAuthStore();

      try {
        return await campagneService.getManagementReport();
      } catch (error) {
        if (
          (error.response && error.response.status === 403) ||
          error.response.status === 401
        ) {
          auth.logout();
        }
      }
    },
  },
});
