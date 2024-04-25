<template>
  <div class="top-bar bg-white shadow-md flex justify-between items-center p-2">
    <div class="flex items-center">
      <img
        class="logo cursor-pointer"
        width="250"
        src="@/assets/ITS_Kompetent_Logo.svg"
        alt="Company Logo"
        @click="pushtoHome()"
      />
      <div class="company-name ml-2 text-xl font-semibold"></div>
    </div>

    <div class="flex items-start">
      <div class="user-info text-gray-700 mr-4">
        <span class="welcome-message hidden md:block"
          >Willkommen!, {{ userName }}</span
        >
        <button
          class="logout-button bg-red-600 text-white px-4 py-2 rounded"
          @click="handleLogout"
        >
          <ArrowLeftEndOnRectangleIcon
            class="h-6 w-6 text-white"
          ></ArrowLeftEndOnRectangleIcon>
        </button>
      </div>
    </div>
  </div>
</template>
<script>
import { useAuthStore } from "@/store/AuthStore";

export default {
  data: function () {
    return {
      totalSeconds: 0,
      minutes: 0,
      seconds: 0,
      expired: false,
    };
  },
  /**
   * A Vue computed property.
   *
   */
  computed: {
    /**
     * A computed property to track the name of the logged in user.
     * Gets displayed in the right corner of the TopBar.
     */
    userName() {
      const authStore = useAuthStore();
      return authStore.user;
    },
    /**
     * A computed property to track the seconds remaining until the user gets logged out.
     *
     */
    secondsRemaining() {
      let value = localStorage.getItem("timeRemaining");
      return parseInt(value, 10) || 0;
    },
    /**
     * A computed property to track the seconds remaining until the user gets logged out.
     * @return {string} The time string remaining
     */
    displayTime() {
      return `${this.minutes.toString().padStart(2, "0")}:${this.seconds
        .toString()
        .padStart(2, "0")}`;
    },
  },
  /**
   * A Vue component lifecycle method that runs once the component is mounted to the DOM.
   * When the view mount a countdown starts to track the time remaining until logout
   */
  mounted() {
    if (this.secondsRemaining > 0) {
      this.startCountdown();
    }
  },
  methods: {
    /**
     * A method that log the user out.
     */
    handleLogout() {
      const authStore = useAuthStore();
      authStore.logout(this.expired);
    },
    /**
     * Routes the user to the Home view.
     */
    pushtoHome() {
      this.$router.push("/");
    },
    /**
     * Starts the countdown until user will get logged out for safety reasons.
     * Sets the time remaining to session storage.
     */
    startCountdown() {
      this.totalSeconds = this.secondsRemaining; // get the total seconds from localStorage
      this.minutes = Math.floor(this.totalSeconds / 60);
      this.seconds = this.totalSeconds % 60;

      const timerInterval = setInterval(() => {
        if (this.seconds === 0) {
          if (this.minutes === 0) {
            clearInterval(timerInterval); // Stop the countdown
            return;
          } else {
            this.minutes--;
            this.seconds = 59;
          }
        } else {
          this.seconds--;
        }
        this.totalSeconds--;
        localStorage.setItem("timeRemaining", this.totalSeconds); // update localStorage
      }, 1000);
    },
  },
};
</script>

<style scoped>
.logo {
  font-size: 24px;
}

.user-info {
  display: flex;
  align-items: center;
}

.welcome-message {
  margin-right: 12px;
}

.logout-button {
  cursor: pointer;
}
</style>
