import APIService from "./api.service";

const CompetenceTestService = {
  /**
   * Asynchronously gets the competence test for a given job profile from the database
   * @param {Number} profileID The profileID of the job profile
   * @returns {Promise<Object>} A promise that resolves to the data of the get response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  getCompetenceTest: async function (profileID) {
    // eslint-disable-next-line no-useless-catch
    try {
      const test = await APIService.get(
        `competence_tests/?job_profile=${profileID}`
      );
      return test.data;
    } catch (error) {
      throw error;
    }
  },
  /**
   * Asynchronously gets the threat situations (should be one) for a given job profile and threat vector
   * @param {Number} profileID The profileID of the job profile
   * @param {Number} threatVectorID The ID of the threat vector
   * @returns {Promise<Object>} A promise that resolves to the data of the get response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  getThreatSituations: async function (threatVectorID, profileID) {
    // eslint-disable-next-line no-useless-catch
    try {
      const threatSituations = await APIService.get(
        `threat_situations/?threat_vector=${threatVectorID}&job_profile=${profileID}`
      );
      return threatSituations.data;
    } catch (error) {
      throw error;
    }
  },
  /**
   * Asynchronously gets the test items for a given threat situation
   * @param {Number} threatSituation The ID of the threat situation
   * @returns {Promise<Object>} A promise that resolves to the data of the get response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  getTestItems: async function (threatSituation) {
    // eslint-disable-next-line no-useless-catch
    try {
      const response = await APIService.get(
        `test_items/?threat_situation=${threatSituation}`
      );
      return response.data;
    } catch (error) {
      throw error;
    }
  },
  /**
   * Asynchronously gets the competence dimensions
   * @returns {Promise<Object>} A promise that resolves to the data of the get response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  getCompetenceDimensions: async function () {
    // eslint-disable-next-line no-useless-catch
    try {
      const response = await APIService.get(`competence_dimensions`);
      return response.data;
    } catch (error) {
      throw error;
    }
  },
  /**
   * Asynchronously gets the impulse for a given test item
   * @param {Number} testItemdID The ID of the testItem
   * @returns {Promise<Object>} A promise that resolves to the data of the get response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  getImpulseItems: async function (testItemID) {
    // eslint-disable-next-line no-useless-catch
    try {
      const response = await APIService.get(
        `impulse_items?id__in=${testItemID}`
      );
      return response.data[0];
    } catch (error) {
      throw error;
    }
  },
  /**
   * Asynchronously gets the answer options for a given question ID
   * @param {Number} questionID The ID of the question
   * @returns {Promise<Object>} A promise that resolves to the data of the get response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  getAnswerOptions: async function (questionID) {
    // eslint-disable-next-line no-useless-catch
    try {
      const response = await APIService.get(
        `choice_items?question=${questionID}`
      );
      return response.data;
    } catch (error) {
      throw error;
    }
  },
  /**
   * Asynchronously generates an indivual report for the competence test result
   * @param {Object} result The competence test result
   * @returns {Promise<Object>} A promise that resolves to the data of the get response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  async generateIndividualReport(result) {
    // eslint-disable-next-line no-useless-catch
    try {
      const response = await APIService.post(
        "/generate_individual_report/",
        result,
        {
          responseType: "blob",
        }
      );
      return response;
    } catch (error) {
      throw error;
    }
  },
};

export default CompetenceTestService;
