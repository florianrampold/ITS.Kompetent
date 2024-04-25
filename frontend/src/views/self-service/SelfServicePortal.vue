<template>
  <template v-if="loading">
    <spinner></spinner>
    <!-- here use a loaded you prefer -->
  </template>
  <template v-else>
    <div class="flex">
      <!-- Sidebar -->
      <div class="bg-gray-800 text-white w-64 min-h-screen">
        <div class="p-4">
          <h2 class="text-2xl font-semibold">KMU Management</h2>
        </div>
        <nav class="mt-6 w-64">
          <a
            href="#"
            class="block py-2 px-4 text-sm hover:bg-gray-900"
            :class="{ 'bg-gray-900': activeTab === 'FAQ' }"
            @click="activeTab = 'FAQ'"
          >
            FAQ
          </a>
          <a
            href="#"
            class="block py-2 px-4 text-sm hover:bg-gray-900"
            :class="{ 'bg-gray-900': activeTab === 'Einladungs-Management' }"
            @click="activeTab = 'Einladungs-Management'"
          >
            Einladungs-Management
          </a>

          <a
            href="#"
            class="block py-2 px-4 text-sm hover:bg-gray-900"
            :class="{
              'bg-gray-900': activeTab === 'Dashboard',
              'cursor-not-allowed opacity-50': !campagneStarted,
            }"
            @click="navigateToDashBoard"
          >
            Dashboard
          </a>
        </nav>
      </div>

      <!-- Main Content -->
      <div class="flex-grow mb-16">
        <TopBar></TopBar>

        <header
          class="bg-white shadow p-4 flex items-center h-20 justify-between"
        >
          <h1 class="text-xl font-semibold">{{ activeTab }}</h1>

          <div class="ml-auto flex items-center">
            <button
              :class="{ hidden: activeTab != 'Dashboard' }"
              class="text-white bg-primary font-semibold rounded-md px-4 py-2 flex items-center"
              @click="refreshData"
            >
              Aktualisieren
              <ArrowPathIcon class="ml-2 w-6 h-6"></ArrowPathIcon>
            </button>
            <button
              v-if="campagneStarted"
              :class="{ hidden: activeTab != 'Einladungs-Management' }"
              class="text-white bg-primary rounded-md font-semibold px-2 py-2 flex justify-between items-center"
              @click="openDeleteCampagneModal"
            >
              <span class="hidden md:block">Kampagne löschen</span>
              <TrashIcon class="md:ml-2 w-6 h-6"></TrashIcon>
            </button>
          </div>
        </header>

        <main class="">
          <div v-if="activeTab === 'Dashboard'">
            <dashboard-view :refresh-view="refresh"></dashboard-view>
          </div>
          <div v-if="activeTab === 'Einladungs-Management'">
            <invitation-view></invitation-view>
          </div>
          <div v-if="activeTab === 'FAQ'">
            <FAQ-view></FAQ-view>
          </div>
        </main>
        <div v-if="deleteCampagneModal">
          <confirmation-modal
            @close-modal="deleteCampagneModal = false"
            @save-decision="deleteCampagne"
          ></confirmation-modal>
        </div>
        <div class="fixed bottom-0 h-16 bg-white shadow-2xl w-full">
          <div
            class="text-primary text-center p-4 flex justify-start items-center"
          >
            <p>© {{ currentYear }} ITS.Kompetent</p>
          </div>
        </div>
      </div>
    </div>
  </template>
</template>

<script>
import TopBar from "@/components/self-service/TopBar.vue";
import InvitationView from "@/views/self-service/InvitationView.vue";
import DashboardView from "@/views/self-service/DashboardView.vue";
import FAQView from "@/views/self-service/FAQView.vue";
import ConfirmationModal from "@/components/self-service/ConfirmationModal.vue";

import { useCampagneStore } from "@/store/CampagneStore";

export default {
  components: {
    TopBar,
    InvitationView,
    DashboardView,
    FAQView,
    ConfirmationModal,
  },
  /**
   * Initializes and returns the state for the Vue component using composition API.
   *
   * This setup function utilizes the Vuex stores specific to job profiles and competence tests.
   * It invokes `useCampagneStore` to access and manage the state related to job profiles,
   * and `useCompetenceTestStore` for managing state related to competence tests. The function
   * then returns these stores for use within the Vue component, enabling reactive state management
   * and encapsulation of business logic associated with job profiles and competence tests.
   *
   * @returns {Object} An object containing references to `campagneStore` and `userStore`.
   */
  setup() {
    const campagneStore = useCampagneStore();

    return {
      campagneStore,
    };
  },
  data() {
    return {
      loading: false,
      deleteCampagneModal: false,
      activeTab: "",
      currentYear: new Date().getFullYear(),
      refresh: false,
    };
  },
  /**
   * A Vue computed property. Listens for changes in the campagne started property.
   */
  computed: {
    campagneStarted() {
      return this.campagneStore.campagneStarted;
    },
  },
  /**
   * A Vue component lifecycle method that runs once the component is mounted to the DOM.
   * Sets the active tab to FAQ if campagne was not started else set to Einladungs-Management.
   */
  mounted() {
    if (this.campagneStore.campagneStarted) {
      this.activeTab = "Einladungs-Management";
    } else {
      this.activeTab = "FAQ";
    }
    this.refreshData();
  },
  methods: {
    /**
     * Navigates to the dashboard component inside the self-service portal. Prevents navigating if a campagne was not started, yet.
     *
     */
    navigateToDashBoard(event) {
      if (!this.campagneStore.campagneStarted) {
        event.preventDefault(); // Prevent default link behavior
        return; // Do nothing if the link is disabled
      }
      this.activeTab = "Dashboard";
    },
    // TO BE IMPLEMENTED
    refreshData() {
      //this.loading = true;
      //
      this.refresh = true;
      setTimeout(() => (this.refresh = false), 500);
    },
    /**
     * Opens a modal that asks the user whether he or she is sure to delete the campagne.
     */
    openDeleteCampagneModal() {
      this.deleteCampagneModal = true;
    },
    /**
     * Method to delete a campagne. Wait for the async call and triggers loading screen until the campagne is deleted.
     */
    async deleteCampagne() {
      this.campagneStore.removeCampagneStarted();
      this.loading = true;
      await this.campagneStore.deleteCampagne();
      setTimeout(() => (this.loading = false), 500);
    },
  },
};
</script>
