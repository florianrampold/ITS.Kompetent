import API from "./api.service";

export default {
  /**
   * Asynchronously gets the invitation tokens.
   * @param {Object} data The data object
   * @returns {Promise<Object>} A promise that resolves to the data of the get response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  async generateInvitationTokens(data) {
    // eslint-disable-next-line no-useless-catch
    try {
      const response = await API.post("/post_invitations/", data);
      return response.data;
    } catch (error) {
      throw error;
    }
  },
  /**
   * Asynchronously posts the e-mail to decrypt them in the data base
   * @param {Object} data The data object
   * @returns {Promise<Object>} A promise that resolves to the data of the post response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  async decryptEmails(data) {
    // eslint-disable-next-line no-useless-catch
    try {
      const response = await API.post("/decrypt_emails/", data);
      return response.data;
    } catch (error) {
      throw error;
    }
  },
  /**
   * Asynchronously posts the competence test results in the database
   * @param {Object} data The data object
   * @returns {Promise<Object>} A promise that resolves to the data of the post response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  async postCompetenceTestResults(data) {
    // eslint-disable-next-line no-useless-catch
    try {
      const response = await API.post("/competence_test_result/", data);
      return response.data;
    } catch (error) {
      throw error;
    }
  },
  /**
   * Asynchronously gets the e-mail to decrypt them in the data base
   * @param {Object} profileID The job profile ID
   * @returns {Promise<Object>} A promise that resolves to the data of the get response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  async getCompetenceTestResults(profileID) {
    let endpoint = "/competence_test_results/";
    if (profileID !== null && profileID !== undefined) {
      endpoint += `${profileID}/`;
    }
    try {
      const response = await API.get(endpoint);
      return response.data;
    } catch (error) {
      console.log(error);
      if (error.response && error.response.data) {
        return [];
      }
      return []; // or throw error;
    }
  },
  /**
   * Asynchronously gets the invitation tokens from the database
   * @returns {Promise<Object>} A promise that resolves to the data of the get response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  async getInvitedEmployees() {
    try {
      const response = await API.get("/get_invitations/");
      return response.data;
    } catch (error) {
      console.log(error);
      if (error.response && error.response.data) {
        return [];
      }
      // If not, handle it in another way (e.g. return a default value or throw an error)
      return []; // or throw error;
    }
  },
  /**
   * Asynchronously gets the result of the competence test per job profile
   * @returns {Promise<Object>} A promise that resolves to the data of the get response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  async getParticipantsPerProfile() {
    try {
      const response = await API.get("/participants_per_profile/");
      return response.data;
    } catch (error) {
      console.log(error);
      if (error.response && error.response.data) {
        return [];
      }
      // If not, handle it in another way (e.g. return a default value or throw an error)
      return []; // or throw error;
    }
  },
  /**
   * Asynchronously gets if the validation token is valid
   * @param {string} invitationToken The invitationToken
   * @returns {Promise<Object>} A promise that resolves to the data of the get response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  async validateInvitationToken(invitationToken) {
    try {
      const response = await API.get(`/invitation_token/${invitationToken}/`);
      return response.data.valid;
    } catch (error) {
      console.log(error);
      if (
        error.response &&
        error.response.data &&
        "valid" in error.response.data
      ) {
        return error.response.data.valid;
      }
      return false; // or throw error;
    }
  },
  /**
   * Asynchronously deletes the campagne and all dependencies in the database
   * @returns {Promise<Object>} A promise that resolves to the data of the post response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  async deleteCampagne() {
    // eslint-disable-next-line no-useless-catch
    try {
      const response = await API.post("/delete_campagne/");
      return response.data;
    } catch (error) {
      throw error;
    }
  },
  /**
   * Asynchronously posts the campaign in the database
   * @param {Boolean} oneInvitationToken A Boolean determining if one invitation token should be used for the campaign or mutliple.
   * @returns {Promise<Object>} A promise that resolves to the data of the post response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  async postCampagne(oneInvitationToken) {
    // eslint-disable-next-line no-useless-catch
    try {
      const response = await API.post("/create_campagne/", oneInvitationToken);
      return response.data;
    } catch (error) {
      throw error;
    }
  },
  /**
   * Asynchronously gets the campaign in the database
   * @returns {Promise<Object>} A promise that resolves to the data of the get response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  async getCampagne() {
    try {
      const response = await API.get("/get_campagne/");
      return response.data;
    } catch (error) {
      console.log(error);
      throw error;
    }
  },
  /**
   * Asynchronously gets the management reported generated in the backend
   * @returns {Promise<Object>} A promise that resolves to the data of the get response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  async getManagementReport() {
    try {
      const response = await API.get("/generate_management_report/", {
        responseType: "blob", // Important for handling PDF data
      });
      return response;
    } catch (error) {
      console.log(error);
      throw error;
    }
  },
  /**
   * Asynchronously removes the security key in the database
   * @returns {Promise<Object>} A promise that resolves to the data of the put response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  async removeSecurityKey() {
    try {
      const response = await API.put("/remove_security_key/");
      return response.data;
    } catch (error) {
      console.log(error);
      if (error.response && error.response.data) {
        return null;
      }
      return []; // or throw error;
    }
  },
  /**
   * Asynchronously generates a security key in the database
   * @returns {Promise<Object>} A promise that resolves to the data of the get response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  async generateSecurityKey() {
    try {
      const response = await API.get("/generate_key/");
      return response.data.key;
    } catch (error) {
      console.log(error);
      if (error.response && error.response.data) {
        return null;
      }
      return []; // or throw error;
    }
  },
};
