<template>
  <div class="bg-primary py-20">
    <h1 class="text-white text-5xl">Datenschutzerklärung ITS.Kompetent</h1>
  </div>
  <div class="bg-white py-20">
    <div class="lg:container lg:mx-auto text-left text-primary">
      Eine Datenschutzerklärung kann hier bei Bedarf eingefügt werden.
    </div>
  </div>
</template>

<script>
export default {
  name: "TrackInfoComponent",

  computed: {
    doNotTrackEnabled() {
      return navigator.doNotTrack === "1" || navigator.doNotTrack === "yes";
    },
  },
  created() {
    this.updateTrackingPreference();
  },

  methods: {
    updateTrackingPreference() {
      if (this.doNotTrackEnabled) {
        console.log("Tracking is disabled per browser setting.");
        // Additional logic to disable tracking scripts
      } else {
        console.log("Tracking is enabled.");
        // Additional logic to enable tracking scripts
      }
    },
  },
};
</script>
