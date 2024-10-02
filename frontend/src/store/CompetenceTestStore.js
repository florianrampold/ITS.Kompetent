import { defineStore } from "pinia";
import competenceTestService from "../services/competence_test.service";

export const useCompetenceTestStore = defineStore("CompetenceTestStore", {
  state: () => {
    return {
      competenceTestResult: {},
    };
  },

  getters: {
    /**
     * Getter to retrieve the competenceTestResult
     * @return {Object} The competence test result
     */
    getCompetenceTestResult() {
      return this.competenceTestResult;
    },
  },

  actions: {
    /**
     * Sets the result of the competence test.
     * @param {Object} testResult - The result object to be set.
     */
    setCompetenceTestResult(testResult) {
      this.competenceTestResult = testResult;
    },

    /**
     * Asynchronously fetches the competence test details for a specified profile ID.
     * @param {string} profileID - The ID of the profile to fetch the test for.
     * @returns {Promise<Object>} A promise that resolves to the test details.
     */
    async getCompetenceTest(profileID) {
      return await competenceTestService.getCompetenceTest(profileID);
    },

    /**
     * Asynchronously retrieves threat situations based on a threat vector and job profile.
     * @param {string} threatVector - The vector of threat to consider.
     * @param {string} jobProfile - The job profile to match against the threats.
     * @returns {Promise<Object[]>} A promise that resolves to an array of threat situations.
     */
    async getThreatSituations(threatVector, jobProfile) {
      return await competenceTestService.getThreatSituations(
        threatVector,
        jobProfile
      );
    },

    /**
     * Asynchronously fetches test items based on a threat situation.
     * @param {string} threatSituation - The threat situation to fetch test items for.
     * @returns {Promise<Object[]>} A promise that resolves to an array of test items.
     */
    async getTestItems(threatSituation) {
      return await competenceTestService.getTestItems(threatSituation);
    },

    /**
     * Asynchronously retrieves impulse items for a given test item.
     * @param {string} testItem - The test item to fetch impulse items for.
     * @returns {Promise<Object[]>} A promise that resolves to an array of impulse items.
     */
    async getImpulseItems(testItem) {
      return await competenceTestService.getImpulseItems(testItem);
    },

    /**
     * Asynchronously fetches answer options for a given question.
     * @param {string} question - The question to fetch answer options for.
     * @returns {Promise<Object[]>} A promise that resolves to an array of answer options.
     */
    async getAnswerOptions(question) {
      return await competenceTestService.getAnswerOptions(question);
    },

    /**
     * Asynchronously generates an individual report based on the test results.
     * @param {Object} results - The test results to generate a report from.
     * @returns {Promise<Object>} A promise that resolves to the generated report.
     * @throws {Error} If generating the report fails.
     */
    async generateIndividualReport(results) {
      return await competenceTestService.generateIndividualReport(results);
    },

    /**
     * Asynchronously retrieves competence dimensions from the service.
     * @returns {Promise<Object[]>} A promise that resolves to an array of competence dimensions.
     * @throws {Error} If fetching the dimensions fails.
     */
    async getCompetenceDimensions() {
      // eslint-disable-next-line no-useless-catch
      try {
        return await competenceTestService.getCompetenceDimensions();
      } catch (error) {
        throw error;
      }
    },
  },
});
