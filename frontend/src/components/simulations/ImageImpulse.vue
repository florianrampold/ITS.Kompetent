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
  watch: {
    filterIndex: "updateImageImpulseItems",
  },
  /**
   * A Vue component lifecycle method that runs once the component is mounted to the DOM.
   * Calls updateImageImpulseItems when view mounts. 
   */
  mounted() {
    this.updateImageImpulseItems();
  },

  methods: {
    /**
     * Displays either all imaes or only one image when Threat Awareness is the active competence dimension.
     */
    updateImageImpulseItems() {
      this.imageImpulseItems = this.images;
      console.log(this.filterIndex, "filter index");
      if (this.filterIndex !== -1) {
        this.imageImpulseItems = [];
        this.imageImpulseItems[0] = this.images[this.filterIndex];
        this.currentIndex = this.filterIndex + 1;
      }
    },
  },
};
</script>
