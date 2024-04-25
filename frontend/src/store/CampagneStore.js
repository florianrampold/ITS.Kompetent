import { defineStore } from "pinia";
import campagneService from "../services/campagne.service";
import { useStorage } from "@vueuse/core";

export const useCampagneStore = defineStore("campagne", {
  state: () => {
    return {
      campagneStarted: useStorage("campagneStarted", false),
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
     * Generates invitation tokens and calls the campagneService to perform the action
     */
    async generateInvitationTokens({ emails = [] }) {
      const payload = {};

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
        console.error("Error during generating invitation tokens:", error);
        throw error;
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
      return await campagneService.getCompetenceTestResults(profileID);
    },

    /**
     * Asynchronously fetches participants per profile.
     * @returns {Promise<Object>} A promise that resolves to the list of participants per profile.
     */
    async getParticipantsPerProfile() {
      return await campagneService.getParticipantsPerProfile();
    },

    /**
     * Asynchronously retrieves a list of invited employees.
     * @returns {Promise<Object>} A promise that resolves to the list of invited employees.
     */
    async getInvitedEmployees() {
      return await campagneService.getInvitedEmployees();
    },

    /**
     * Validates an invitation token asynchronously.
     * @param {string} token - The invitation token to validate.
     * @returns {Promise<Object>} A promise that resolves to the validation result.
     */
    async validateInvitationToken(token) {
      return await campagneService.validateInvitationToken(token);
    },

    /**
     * Asynchronously deletes a campaign.
     * @throws {Error} If the deletion fails.
     */
    async deleteCampagne() {
      try {
        await campagneService.deleteCampagne();
      } catch (error) {
        console.error("Error during deleting attempt:", error);
        throw error;
      }
    },

    /**
     * Asynchronously posts a new campaign with a specified invitation token.
     * @param {string} oneInvitationToken - The token to use for the new campaign.
     * @throws {Error} If posting the campaign fails.
     */
    async postCampagne(oneInvitationToken) {
      console.log(oneInvitationToken, " the mode");
      try {
        await campagneService.postCampagne(oneInvitationToken);
      } catch (error) {
        console.error("Error during posting attempt", error);
        throw error;
      }
    },

    /**
     * Asynchronously removes a security key.
     * @throws {Error} If removing the security key fails.
     */
    async removeSecurityKey() {
      try {
        await campagneService.removeSecurityKey();
      } catch (error) {
        console.error("Error during removing attempt", error);
        throw error;
      }
    },

    /**
     * Asynchronously retrieves campaign details.
     * @returns {Promise<Object>} A promise that resolves to the campaign details.
     */
    async getCampagne() {
      return await campagneService.getCampagne();
    },

    /**
     * Asynchronously generates a security key.
     * @returns {Promise<Object>} A promise that resolves to the generated security key.
     */
    async generateSecurityKey() {
      return await campagneService.generateSecurityKey();
    },

    /**
     * Asynchronously decrypts emails with provided data.
     * @param {Object} data - The data needed for decryption.
     * @returns {Promise<Object>} A promise that resolves to the decrypted emails.
     * @throws {Error} If decryption fails.
     */
    async decryptEmails(data) {
      try {
        const response = await campagneService.decryptEmails(data);
        return response;
      } catch (error) {
        console.error("Error during decrypting attempt", error);
        throw error;
      }
    },

    /**
     * Asynchronously fetches the management report.
     * @returns {Promise<Object>} A promise that resolves to the management report.
     */
    async getManagementReport() {
      return await campagneService.getManagementReport();
    },
  },
});
