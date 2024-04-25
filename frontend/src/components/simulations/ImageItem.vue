<template>
  <div class="xl:relative bg-white rounded-lg shadow-lg border border-gray-200">
    <div
      ref="imageContainer"
      class="w-full flex justify-center items-center overflow-hidden"
      style="max-height: 70vh"
    >
      <image-impulse-skeleton
        v-if="isLoading"
        class="w-full m-4"
        style="height: 100% max-height"
      />
      <img
        v-show="!isLoading"
        ref="image"
        class="w-full h-auto cursor-pointer"
        :src="image.image_field"
        alt=""
        @load="imageLoaded"
        @error="imageError"
        @click="openModal"
      />
    </div>
    <div class="p-5 text-left">
      <h5
        class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
      >
        Szenario {{ currentIndex }}
      </h5>
      <p class="text-xl font-normal text-gray-700 dark:text-gray-400">
        {{ image.image_description }}
      </p>
    </div>
    <div
      v-if="isModalOpen"
      class="fixed inset-0 bg-black bg-opacity-80 flex items-center justify-center p-4 z-50"
      @click.self="closeModal()"
    >
      <div
        class="bg-white rounded-lg shadow-xl overflow-auto max-w-4xl max-h-full"
      >
        <span
          class="absolute top-4 right-4 text-white text-3xl cursor-pointer"
          @click="closeModal"
          >&times;</span
        >
        <img
          :src="image.image_field"
          alt="Full size image"
          class="max-w-full max-h-full"
        />
      </div>
    </div>
  </div>
</template>

<script>
import ImageImpulseSkeleton from "@/components/base/ImageImpulseSkeleton.vue";

export default {
  components: {
    ImageImpulseSkeleton,
  },
  props: {
    image: {
      type: Object,
      default: null,
    },
    currentIndex: {
      type: Number,
      default: 0,
    },
  },
  data() {
    return {
      isLoading: true, // Initial state is loading
      isModalOpen: false,
    };
  },
  mounted() {
    window.addEventListener("resize", this.handleResize);
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.handleResize);
  },
  methods: {
    openModal() {
      this.isModalOpen = true;
    },
    closeModal() {
      this.isModalOpen = false;
    },
    adjustImageSize() {
      const img = this.$refs.image;
      const container = this.$refs.imageContainer;

      // Set initial full width
      img.style.width = "100%";
      img.style.height = "auto";

      // Wait for the next DOM update cycle to ensure the image is fully rendered
      this.$nextTick(() => {
        const heightAfterWidthAdjustment = img.offsetHeight;

        if (heightAfterWidthAdjustment > container.clientHeight) {
          // The height exceeds the maximum, so adjust the width to shrink the image proportionally
          const aspectRatio = img.naturalWidth / img.naturalHeight;
          const adjustedWidth = container.clientHeight * aspectRatio;
          img.style.width = `${adjustedWidth}px`;
          img.style.height = `${container.clientHeight}px`; // Explicitly set the height to max height
        }
      });
    },
    imageLoaded() {
      this.$nextTick().then(this.adjustImageSize); // Ensures the DOM is updated before adjustment
      this.isLoading = false; // Set loading to false when the image has loaded
    },
    imageError() {
      this.isLoading = false; // Also set loading to false if the image fails to load
    },
    handleResize() {
      this.adjustImageSize(); // Re-apply image adjustment on window resize
    },
  },
};
</script>
