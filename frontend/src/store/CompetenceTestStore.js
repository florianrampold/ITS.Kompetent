import { defineStore } from "pinia";
import { useStorage } from "@vueuse/core";
import competenceTestService from "../services/competence_test.service";

export const useCompetenceTestStore = defineStore("CompetenceTestStore", {
  state: () => {
    return {
      competenceTestResult: useStorage("competenceTestResult", {}),
      testStarted: useStorage("testStarted", false),
      testButtonActive: useStorage("testButtonActive", false),
      getStartedButtonActive: useStorage("getStartedButtonActive", false),
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
    /**
     * Getter to retrieve if the competence test started
     * @return {Boolean} True if test started, false else.
     */
    getTestStarted() {
      return this.testStarted;
    },
    /**
     * Getter to retrieve if the test button is active.
     * @return {Boolean} True if yes, false else.
     */
    getTestButtonActive() {
      return this.testButtonActive;
    },
    /**
     * Getter to retrieve if the test button is active.
     * @return {Boolean} True if yes, false else.
     */
    getGetStartedButtonActive() {
      return this.getStartedButtonActive;
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
     * Marks the test as started.
     */
    startTest() {
      this.testStarted = true;
    },

    /**
     * Activates the test button, making it responsive to user interactions.
     */
    setTestButtonActive() {
      this.testButtonActive = true;
    },

    /**
     * Activates the "Get Started" button, making it responsive to user interactions.
     */
    setGetStartedButtonActive() {
      this.getStartedButtonActive = true;
    },

    /**
     * Deactivates the test button, making it unresponsive to user interactions.
     */
    setTestButtonInactive() {
      this.testButtonActive = false;
    },

    /**
     * Deactivates the "Get Started" button, making it unresponsive to user interactions.
     */
    setGetStartedButtonInactive() {
      this.getStartedButtonActive = false;
    },

    /**
     * Marks the test as ended.
     */
    endTest() {
      this.testStarted = false;
    },

    /**
     * Asynchronously fetches the competence test details for a specified profile ID.
     * @param {string} profileID - The ID of the profile to fetch the test for.
     * @returns {Promise<Object>} A promise that resolves to the test details.
     */
    async getCompetenceTest(profileID) {
      try {
        return await competenceTestService.getCompetenceTest(profileID);
      } catch (error) {
        console.log(error);
      }
    },

    /**
     * Asynchronously retrieves threat situations based on a threat vector and job profile.
     * @param {string} threatVector - The vector of threat to consider.
     * @param {string} jobProfile - The job profile to match against the threats.
     * @returns {Promise<Object[]>} A promise that resolves to an array of threat situations.
     */
    async getThreatSituations(threatVector, jobProfile) {
      try {
        return await competenceTestService.getThreatSituations(
          threatVector,
          jobProfile
        );
      } catch (error) {
        console.log(error);
      }
    },

    /**
     * Asynchronously fetches test items based on a threat situation.
     * @param {string} threatSituation - The threat situation to fetch test items for.
     * @returns {Promise<Object[]>} A promise that resolves to an array of test items.
     */
    async getTestItems(threatSituation) {
      try {
        return await competenceTestService.getTestItems(threatSituation);
      } catch (error) {
        console.log(error);
      }
    },

    /**
     * Asynchronously retrieves impulse items for a given test item.
     * @param {string} testItem - The test item to fetch impulse items for.
     * @returns {Promise<Object[]>} A promise that resolves to an array of impulse items.
     */
    async getImpulseItems(testItem) {
      try {
        return await competenceTestService.getImpulseItems(testItem);
      } catch (error) {
        console.log(error);
      }
    },

    /**
     * Asynchronously fetches answer options for a given question.
     * @param {string} question - The question to fetch answer options for.
     * @returns {Promise<Object[]>} A promise that resolves to an array of answer options.
     */
    async getAnswerOptions(question) {
      try {
        return await competenceTestService.getAnswerOptions(question);
      } catch (error) {
        console.log(error);
      }
    },

    /**
     * Asynchronously generates an individual report based on the test results.
     * @param {Object} results - The test results to generate a report from.
     * @returns {Promise<Object>} A promise that resolves to the generated report.
     * @throws {Error} If generating the report fails.
     */
    async generateIndividualReport(results) {
      try {
        return await competenceTestService.generateIndividualReport(results);
      } catch (error) {
        console.error("Error during report generation:", error);
        throw error;
      }
    },

    /**
     * Asynchronously retrieves competence dimensions from the service.
     * @returns {Promise<Object[]>} A promise that resolves to an array of competence dimensions.
     * @throws {Error} If fetching the dimensions fails.
     */
    async getCompetenceDimensions() {
      try {
        return await competenceTestService.getCompetenceDimensions();
      } catch (error) {
        console.error("Error fetching competence dimensions:", error);
        throw error;
      }
    },
    async sendContactRequest(data) {
      try {
        return await competenceTestService.sendContactRequest(data);
      } catch (error) {
        console.log(error);
      }
    },
  },
});
