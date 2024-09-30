<template>
  <div v-if="filterIndex == -1">
    <div v-if="chatInterfaces.length == 1">
      <div
        v-for="chatInterface in chatInterfaces"
        :key="chatInterface"
        class="grid grid-cols-1"
      >
        <chat-interface
          :chat="chatInterface"
          :current-index="index + 1"
        ></chat-interface>
      </div>
    </div>

    <div v-if="chatInterfaces.length == 2">
      <div class="grid grid-cols-2 gap-10">
        <div v-for="chatInterface in chatInterfaces" :key="chatInterface">
          <chat-interface :chat="chatInterface" :current-index="index + 1">{{
            key
          }}</chat-interface>
        </div>
      </div>
    </div>
    <div v-if="chatInterfaces.length == 3">
      <div
        class="grid grid-cols-1 lg:grid-cols-2 2xl:grid-cols-3 xl:gap-x-10 gap-10"
      >
        <div
          v-for="(chatInterface, index) in chatInterfaces"
          :key="chatInterface"
        >
          <chat-interface :chat="chatInterface" :current-index="index + 1">{{
            key
          }}</chat-interface>
        </div>
      </div>
    </div>
  </div>
  <div v-else>
    <div
      v-for="chatInterface in chatImpulseItems"
      :key="chatInterface"
      class="grid grid-cols-6"
    >
      <div class="lg:col-start-2 lg:col-span-4 col-start-0 col-span-6">
        <chat-interface
          :chat="chatInterface"
          :current-index="currentIndex"
        ></chat-interface>
      </div>
    </div>
  </div>
</template>

<script>
import ChatInterface from "@/components/simulations/ChatInterface.vue";

export default {
  components: {
    ChatInterface,
  },
  props: {
    chatInterfaces: {
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
      currentIndex: 1,
      chatImpulseItems: [],
    };
  },
  watch: {
    filterIndex: "updateChatImpulseItems",
  },
  /**
   * A Vue component lifecycle method that runs once the component is mounted to the DOM.
   * If filterIndex is not -1 (Threat Awareness) shoe the chatInterface which is the most threatining.
   */

  mounted() {
    this.updateChatImpulseItems();
  },

  methods: {
    updateChatImpulseItems() {
      if (this.filterIndex !== -1) {
        this.chatImpulseItems = [];
        this.chatImpulseItems[0] = this.chatInterfaces[this.filterIndex];
        this.currentIndex = this.filterIndex + 1;
      } else {
        // Optionally reset chatImpulseItems and currentIndex if filterIndex is -1
        this.chatImpulseItems = this.chatInterfaces;
        this.currentIndex = 0;
      }
    },
  },
};
</script>
