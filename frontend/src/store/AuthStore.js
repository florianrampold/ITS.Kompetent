// src/stores/auth.js
import { defineStore } from "pinia";

import authService from "../services/auth.service";
import router from "../router/index.js";

export const useAuthStore = defineStore({
  id: "auth",

  state: () => ({
    user: "",
    lastInteraction: new Date().toISOString(),
    isLoggedIn: false,
    refreshInterval: null,
    isInitializing: true,
    authPromise: null,
  }),

  actions: {
    /**
     * Sets the last interaction timestamp between the logged in user and the web tool
     * @param {string} lastInteraction The timestamp as string of the last interaction (clicking, mousing mouse etc.)
     */
    setLastInteraction(lastInteraction) {
      this.lastInteraction = lastInteraction;
    },
    setIsLoggedIn(loggedIn) {
      this.isLoggedIn = loggedIn;
    },
    /**
     * Initializes the authentication state. Is called whenever the app mounts and also when the access token expires.
     * @param {Boolean} expired True when the token expired, false else
     */
    async init(expired) {
      this.authPromise = new Promise((resolve) => {
        authService
          .getStatus()
          .then((response) => {
            if (response.status === "authenticated") {
              this.isLoggedIn = true;
              this.user = response.user;
              this.startTokenExpiryTimer();
            } else {
              // Logic for protected routes
              this.logout(expired);
            }
            this.isInitializing = false; // set it to false once done
            resolve();
          })
          .catch((error) => {
            console.log("Error:", error);

            this.logout(expired);

            this.isInitializing = false;
            resolve();
          });
      });
    },
    /**
    * Ensures CSRF token is set by making a simple request.
    */
    async ensureCsrfToken() {
      try {
        // This request will trigger the middleware and set the CSRF token in the cookies
        await authService.ensureCsrfToken();  // A simple API endpoint that just triggers the middleware
      } catch (error) {
        console.error("Error ensuring CSRF token:", error);
      }
    },

    /**
     * Logs the user in. Uses a username and a password to authenticate
     * @param {string} username The username
     * @param {string} password The password of the user
     * @throws {Error} Throws an error if crendetials are wrong
     */
    async login({ username, password }) {
      try {
        const response = await authService.login({ username, password });
        //this.user = response.user; // adjust as necessary based on your API's response structure
        this.isLoggedIn = true;
        this.user = response.user;

        this.startTokenExpiryTimer();
      } catch (error) {
        console.error("Error during login:", error);
        throw error;
      }
    },
    /**
     * Logs the user out and routes to the login page
     * @param {Boolean} expired True when the token expired, false else
     * @throws {Error} Throws an error if logout was not possible.
     */
    async logout(expired) {
      const currentRoute = router.currentRoute.value;
      try {
        // Call backend endpoint to invalidate the token
        await authService.logout();
        this.stopTokenExpiryTimer();

        // Clear frontend state
        this.isLoggedIn = false;
        this.user = null;

        // Redirect to the login page.
        if (currentRoute.matched.some((record) => record.meta.requiresAuth)) {
          if (expired) {
            router.push("/login/expired");
          } else {
            router.push("/login");
          }
        }
      } catch (error) {
        router.push("/login");

        console.error("Error during logout:", error);
      }
    },

    /**
     * Starts a counter until the access token stored as HTTPOnlyCookie becomes invalid. The interval should be set to repeat shortly before the access token lifetime expires.
     * Calls refreshToken to make an API call to refresh access and refresh token.
     */
    startTokenExpiryTimer() {
      // Clear any existing interval
      this.stopTokenExpiryTimer();

      this.refreshInterval = setInterval(() => {
        this.refreshToken();
      }, 280000); // Refresh every 250 seconds
    },
    /**
     * Stops the interval to make an API call to refresk tokens.
     */
    stopTokenExpiryTimer() {
      if (this.refreshInterval) {
        clearInterval(this.refreshInterval);
        this.refreshInterval = null;
      }
    },
    /**
     * Method to check if the acces token and the refresh token are still valid
     * @param {string} lastInteraction The timestamp of the last interaction of the user with the web app.
     * @throws {Error} Thrwos an error if in the backend access token or/and refresh token could not be validated and logs out the user.
     */
    async refreshToken() {
      try {
        await authService.refreshToken(this.lastInteraction);
        //console.log("Token refreshed:", response);
      } catch (error) {
        console.error("Error during token refresh:", error);
        if (
          error.response &&
          error.response.data.error === "Session expired. Please log in again."
        ) {
          await this.logout(true);
          this.stopTokenExpiryTimer();
        }
      }
    },
    /**
     * Chekcs whether the user has to change the password.
     */
    async checkPasswordChange() {
      try {
        const response = await authService.checkPasswordChange();
        return response;

      } catch (error) {
        console.error("Error during password change:", error);
      }
    }
  },
});
