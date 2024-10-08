import API from "./api.service";
import router from "../router/index.js";

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
  async logout(intercepted) {
    // eslint-disable-next-line no-useless-catch
    try {
      const response = await API.get("/logout/");
      if (intercepted) {
        router.push("/login");
      } else {
        return response.data;
      }
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
      }
    }
  },
  async checkPasswordChange() {
    // eslint-disable-next-line no-useless-catch
    try {
      const response = await API.get("/check_password_change/");
      return response.data;
    } catch (error) {
      throw error;
    }
  },
  /**
   * Ensures CSRF token is set by making a simple request before the user tries to login.
   */
  async ensureCsrfToken() {
    // eslint-disable-next-line no-useless-catch
    try {
      await API.get("/ping/");
    } catch (error) {
      throw error;
    }
  },
};
