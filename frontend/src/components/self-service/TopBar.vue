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
