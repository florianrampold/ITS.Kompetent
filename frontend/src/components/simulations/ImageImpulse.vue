<template>
  <div v-if="filterIndex == -1">
    <div
      v-for="(image, index) in imageImpulseItems"
      :key="image"
      class="grid grid-cols-6"
    >
      <image-item
        class="mt-10 lg:col-start-2 lg:col-span-4 col-start-0 col-span-6"
        :image="image"
        :current-index="index + 1"
      ></image-item>
    </div>
  </div>
  <div v-else>
    <div
      v-for="image in imageImpulseItems"
      :key="image"
      class="grid grid-cols-6"
    >
      <image-item
        class="mt-10 lg:col-start-2 lg:col-span-4 col-start-0 col-span-6"
        :image="image"
        :current-index="currentIndex"
      ></image-item>
    </div>
  </div>
</template>

<script>
import ImageItem from "@/components/simulations/ImageItem.vue";

export default {
  components: {
    ImageItem,
  },
  props: {
    images: {
      type: Array,
      default: null,
    },
    filterIndex: {
      type: Number,
      default: -1,
    },
  },
  data() {
    return {
      imageImpulseItems: [],
      currentIndex: 1,
    };
  },
  /**
   * A Vue component lifecycle method that runs once the component is mounted to the DOM.
   * If filterIndex is not -1 (Threat Awareness) shoe the image which is the most threatining.
   */
  mounted() {
    this.imageImpulseItems = this.images;
    if (this.filterIndex != -1) {
      this.imageImpulseItems = [];
      this.imageImpulseItems[0] = this.images[this.filterIndex];
      this.currentIndex = this.filterIndex + 1;
    }
  },
};
</script>
