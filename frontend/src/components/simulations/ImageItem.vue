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
      class="fixed inset-0 bg-black bg-opacity-80 flex items-center justify-center z-50"
      @click="closeModal()"
    >
      <div class="relative w-full h-full flex items-center justify-center">
        <span
          class="absolute top-4 right-4 text-white text-3xl cursor-pointer z-50"
          @click="closeModal"
          >&times;</span
        >
        <img
          :src="image.image_field"
          alt="Full size image"
          class="object-contain m-4 max-w-full max-h-full w-full h-full"
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
      isLoading: true, 
      isModalOpen: false,
    };
  },
  /**
   * A Vue component lifecycle method that runs once the component is mounted to the DOM.
   * Handles resizing of images.
   */
  mounted() {
    window.addEventListener("resize", this.handleResize);
  },
  /**
   * A Vue component lifecycle method that runs before the component is unmounted to the DOM.
   * Removes the event listener to handle resizing.
   */
  beforeUnmount() {
    window.removeEventListener("resize", this.handleResize);
  },
  methods: {
  /**
   * Opens the modal
   */
    openModal() {
      this.isModalOpen = true;
    },
    /**
    * Closes the modal
     */
    closeModal() {
      this.isModalOpen = false;
    },
    /**
    * Adjust the image size to the optimal width and heght of the container.
    */
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
    /**
    * Calls adjusting of image size when imae is loaded.
    */
    imageLoaded() {
      this.$nextTick().then(this.adjustImageSize); // Ensures the DOM is updated before adjustment
      this.isLoading = false; // Set loading to false when the image has loaded
    },
    /**
     * Throws an error when image cannot be loaded
     */
    imageError() {
      this.isLoading = false; // Also set loading to false if the image fails to load
    },
     /**
     * Handles resizing of the image
     */
    handleResize() {
      this.adjustImageSize(); 
    },
  },
};
</script>
