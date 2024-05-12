import API from "./api.service";

export default {
  /**
   * Asynchronously retrieves the status from the API.
   * @returns {Promise<Object>} A promise that resolves to the data of the status response.
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  async getStatus() {
    // eslint-disable-next-line no-useless-catch
    try {
      const response = await API.get("/status/");
      return response.data;
    } catch (error) {
      console.log("error");
      throw error;
    }
  },

  /**
   * Asynchronously logs in a user with the provided credentials.
   * @param {Object} data - The login credentials.
   * @returns {Promise<Object>} A promise that resolves to the data of the login response.
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  async login(data) {
    // eslint-disable-next-line no-useless-catch
    try {
      const response = await API.post("/auth/jwt/create/", data);
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Asynchronously logs out the current user.
   * @returns {Promise<Object>} A promise that resolves to the data of the logout response.
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  async logout() {
    // eslint-disable-next-line no-useless-catch
    try {
      const response = await API.get("/logout/");
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  /**
   * Asynchronously refreshes the authentication token using a refresh token.
   * @param {string} refresh - The refresh token.
   * @returns {Promise<Object>} A promise that resolves to the data of the token refresh response.
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  async refreshToken(lastInteraction) {
    try {
      const response = await API.post("/auth/jwt/refresh/", {
        last_interaction: lastInteraction,
      });
      return response.data;
    } catch (error) {
      if (
        error.response &&
        error.response.data.error === "Session expired. Please log in again."
      ) {
        throw error;
        // Handle the session expiration
      }
    }
  },
    /**
   * Asynchronously gets the user profile in the database
   * @returns {Promise<Object>} A promise that resolves to the data of the get response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
     async getUserProfile() {
      try {
        const response = await API.get("/get_user_profile/");
        return response.data;
      } catch (error) {
        console.log(error);
        throw error;
      }
    },
};
