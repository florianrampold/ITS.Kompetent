<template>
  <div class="flex items-center justify-center min-h-screen bg-primary">
    <transition name="fade">
      <div
        v-if="show"
        class="relative z-10 p-8 bg-white shadow-xl rounded-lg w-1/3 transition-transform transform scale-95 hover:scale-100"
      >
        <img
          class="w-full mb-4 object-cover rounded"
          src="@/assets/home.jpg"
          alt="Sitzung abgelaufen"
        />

        <h1 class="text-2xl font-semibold mb-4">Sitzung abgelaufen</h1>
        <p class="text-md mb-6">
          Aus Sicherheitsgründen haben wir Ihre Sitzung beendet. Wir nehmen die
          Sicherheit Ihrer Daten sehr ernst und möchten sicherstellen, dass
          niemand ohne Ihre Zustimmung auf Ihr Konto zugreifen kann.
        </p>

        <button
          class="w-full bg-primary hover:bg-primary-dark text-white font-bold py-2 px-4 rounded-full transition-transform transform scale-95 hover:scale-100"
          @click="relogin"
        >
          Erneut anmelden
        </button>
      </div>
    </transition>
    <div class="absolute inset-0 bg-black opacity-40"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      show: true,
    };
  },
  methods: {
    /**
     * Navigats o the login page
     */
    relogin() {
      this.$router.push("/login");
    },
  },
};
</script>

<style>
/* Smooth fade transition */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
  opacity: 0;
}
</style>
