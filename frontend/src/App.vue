<template>
  <NavBar v-if="!requiresAuth" />
  <router-view />
  <Footer v-if="!requiresAuth" />
</template>

<script>
import NavBar from "@/components/base/NavBar.vue";
import Footer from "@/components/base/Footer.vue";
import { useAuthStore } from "@/store/AuthStore";

export default {
  name: "App",
  components: {
    NavBar,
    Footer,
  },
  setup() {
    const authStore = useAuthStore();

    return { authStore };
  },

  computed: {
    /**
     * A computed property to find out if the current route is the login page
     * @return {Boolean} True if route is the login page
     */
    isLoginPage() {
      return this.$route.name === "Login";
    },
    /**
     * A computed property to check whether the route requires authentication
     * @return {Boolean} True if route requires authentication.
     */
    requiresAuth() {
      return this.$route.matched.some((record) => record.meta.requiresAuth);
    },
  },
  /**
   * A Vue component lifecycle method that runs once the component is unmounted to the DOM.
   * Handles removing event listeners for user interaction and sleep mode of the application
   * Also handles checking authentication state
   */
  beforeUnmount() {
    window.removeEventListener("mousemove", this.setInteractionTime);
    window.removeEventListener("keypress", this.setInteractionTime);
    window.removeEventListener("click", this.setInteractionTime);
    document.removeEventListener(
      "visibilitychange",
      this.handleVisibilityChange
    );
  },

  /**
   * A Vue component lifecycle method that runs once the component is mounted to the DOM.
   * Handles loading screen when app is refreshed
   * Handles adding event listeners for user interaction and sleep mode of the application
   * Also handles checking authentication state
   */
  mounted() {
    window.addEventListener("mousemove", this.setInteractionTime);
    window.addEventListener("keypress", this.setInteractionTime);
    window.addEventListener("click", this.setInteractionTime);
    document.addEventListener("visibilitychange", this.handleVisibilityChange);
    const splashScreen = document.getElementById("splash-screen");
    if (splashScreen) {
      splashScreen.style.opacity = "0";
      setTimeout(() => splashScreen.remove(), 500); // Fade out and then remove the splash screen
    }
    const auth = useAuthStore();

    auth.init();
  },
  methods: {
    /**
     * A method to set the last interaction time of the suer with the web app.
     * Only executed if the user is logged in
     */
    setInteractionTime() {
      if (this.authStore.isLoggedIn) {
        this.authStore.setLastInteraction(new Date().toISOString()); // Store the current time as ISO string
      }
    },
    /**
     * Gets called when the app was sleeping and the user comes back.
     * Subsequently checks the access and refresh token and then start a token expiry timer for periodically checking lifetime of the tokens.
     */
    handleVisibilityChange() {
      if (document.visibilityState === "visible" && this.authStore.isLoggedIn) {
        this.authStore.refreshToken();
        this.authStore.startTokenExpiryTimer();
      }
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
