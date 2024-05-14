<template>
  <!-- Modal -->
  <div
    class="fixed inset-0 flex items-center justify-center z-10"
    @click="closeModal"
  >
    <div
      class="bg-white w-2/3 md:w-1/2 rounded shadow-lg"
      style="max-height: calc(100vh - 4rem); overflow-y: auto"
      @click.stop
    >
      <div class="p-6">
        <!-- Modal header -->
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-2xl font-bold">{{ modalTitle }}</h2>
          <button class="text-gray-600 hover:text-gray-800" @click="closeModal">
            <XMarkIcon class="h-6 w-6 text-gray-500"></XMarkIcon>
          </button>
        </div>

        <!-- Tabs -->
        <div class="flex mb-4">
          <button
            class="px-4 py-2 mr-2 bg-gray-200 font-bold rounded-tl rounded-bl focus:outline-none"
            :class="{
              'bg-primary text-white': activeTab === 'upload',
            }"
            @click="activeTab = 'upload'"
          >
            Upload
          </button>
          <button
            class="px-4 py-2 bg-gray-200 font-bold rounded-tr rounded-br focus:outline-none"
            :class="{
              'bg-primary text-white': activeTab === 'verification',
            }"
            :disabled="uploadedEmails.length === 0"
            @click="activeTab = 'verification'"
          >
            Überprüfung
          </button>
        </div>

        <!-- Upload Tab Content -->
        <div v-if="activeTab === 'upload'">
          <div
            class="flex flex-col items-center justify-center w-full"
            @dragover.prevent
            @dragenter.prevent
            @drop.prevent="handleDrop"
          >
            <div
              class="border-2 border-dashed border-gray-300 rounded-lg p-6 w-full max-w-lg cursor-pointer hover:border-blue-500 hover:bg-blue-50 transition-all"
              :class="{ 'bg-blue-50 border-blue-500': isDragOver }"
              @click="openFileDialog"
              @dragover="dragOver"
              @dragleave="dragLeave"
            >
              <div class="flex flex-col items-center justify-center">
                <XMarkIcon class="w-12 h-12 text-gray-500"></XMarkIcon>
                <p class="mt-2 text-gray-500">
                  Ziehen Sie Ihre Datei per Drag & Drop hierher, oder
                  <span class="text-blue-600 underline"
                    >wählen Sie eine lokale CSV-Datei aus.</span
                  >
                  <br />
                  <br />
                  <strong> Achtung: </strong> Stellen Sie sicher, dass die
                  E-Mail-Adressen per Semikolon und nicht per Komma voneinander
                  getrennt sin in der CSV-Datei!
                </p>
                <input
                  ref="fileInput"
                  type="file"
                  class="hidden"
                  accept=".csv"
                  @change="handleFiles"
                />
              </div>
            </div>
            <div v-if="selectedFile" class="mt-4">
              <p class="text-gray-700">
                Selected file:
                <span class="font-semibold">{{ selectedFile.name }}</span>
              </p>
            </div>
          </div>
        </div>

        <!-- Verification Tab Content -->
        <div v-if="activeTab === 'verification'">
          <div v-if="activeTab === 'verification'">
            <table class="mt-4 w-full">
              <thead>
                <tr>
                  <th
                    class="py-4 px-6 bg-gray-100 font-bold uppercase text-sm text-gray-600 border-b"
                  >
                    Email-Addressen
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(emailTemp, index) in paginatedEmails" :key="index">
                  <td class="py-4 px-6 border-b">{{ emailTemp }}</td>
                </tr>
              </tbody>
            </table>

            <!-- Pagination -->
            <nav class="mt-4 flex items-center justify-center">
              <ul class="flex space-x-2">
                <li>
                  <button
                    class="py-2 px-4 bg-secondary text-white rounded focus:outline-none"
                    :disabled="currentPage === 1"
                    @click="prevPage"
                  >
                    Vorherige
                  </button>
                </li>
                <li>
                  <button
                    class="py-2 px-4 bg-secondary text-white rounded focus:outline-none"
                    :disabled="currentPage === pageCount"
                    @click="nextPage"
                  >
                    Nächste
                  </button>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </div>

      <!-- Modal footer -->
      <div class="px-6 py-4 bg-gray-100 flex justify-center">
        <button
          v-if="activeTab === 'verification'"
          class="bg-primary hover:bg-primaryAccent text-white font-bold py-2 px-4 rounded"
          :disabled="!fileData"
          @click="saveResults"
        >
          Bestätigen
        </button>
        <button
          v-else
          class="text-white font-bold py-2 px-4 rounded"
          :class="{
            'bg-gray-200': isDisabled,
            'bg-primary hover:bg-primaryAccent': !isDisabled,
          }"
          :disabled="!fileData"
          @click="saveData"
        >
          Hochladen
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    show: Boolean,
    title: {
      type: String,
      default: "",
    },
    content: {
      type: String,
      default: "",
    },
  },
  emits: ["close", "upload"],
  data() {
    return {
      isModalOpen: false,
      modalTitle: "Email-Adressen Upload",
      fileData: null,
      activeTab: "upload",
      uploadedEmails: [],
      uploadCount: 0,
      approvedUpload: false,
      // Pagination
      currentPage: 1,
      itemsPerPage: 5,
      isDragOver: false,
      selectedFile: null,
    };
  },
  computed: {
    /**
     * A computed property that set upload button to disabled if there is no file data
     */
    isDisabled() {
      return !this.fileData;
    },
    /**
     * A computed property to only retrieve the e-mail uplaoded on the respective page
     */
    paginatedEmails() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      const endIndex = startIndex + this.itemsPerPage;
      return this.uploadedEmails.slice(startIndex, endIndex);
    },
    /**
     * A computed property to track how many total pages exist.
     */
    pageCount() {
      return Math.ceil(this.uploadedEmails.length / this.itemsPerPage);
    },
  },

  methods: {
    /**
     * A method that handles pagination to the previous page.
     */
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    /**
     * A method that handles pagination to the next page.
     */
    nextPage() {
      if (this.currentPage < this.pageCount) {
        this.currentPage++;
      }
    },
    /**
     * A method that closes the upload modal
     */
    closeModal() {
      this.$emit("close");
      this.email = "";
      this.fileData = null;
      this.activeTab = "upload";
      this.uploadedEmails = [];
      this.approvedUpload = false;
    },
    /**
     * Opens the native upload component of the device
     */
    openFileDialog() {
      this.$refs.fileInput.click();
    },
    /**
     * Handles dropping a file into the upload window.
     */
    handleDrop(event) {
      this.isDragOver = false;
      this.handleFiles(event);
    },
    /**
     * Handles dragging of the file
     */
    dragOver() {
      this.isDragOver = true;
    },
    /**
     * Handles stop dragging of the file
     */
    dragLeave() {
      this.isDragOver = false;
    },
    /**
     * Main method to handle the file upload
     */
    handleFiles(event) {
      const files = event.target.files || event.dataTransfer.files;
      if (!files.length) return;
      this.selectedFile = files[0];
      const reader = new FileReader();

      reader.onload = () => {
        this.fileData = reader.result;
      };

      reader.readAsText(this.selectedFile);
    },
    /**
     * Pushes the file data from csv into an array of e-mail adresses.
     */
    saveData() {
      const emails = [];

      if (this.fileData) {
        const lines = this.fileData.split("\n");
        for (const line of lines) {
          const cssFiles = line.split(";");
          for (const cssFile of cssFiles) {
            const cssEmail = cssFile.trim();
            if (cssEmail.includes("@")) {
              emails.push(cssEmail);
              this.uploadCount += 1;
            }
          }
        }
      }

      // Update uploadedEmails with the new emails
      this.uploadedEmails = emails;

      // Open the verification tab
      this.setActiveTab("verification");

      // Enable the Bestätigen button
      this.approvedUpload = false;
    },
    /**
     * Method to keep track of the active tab (upload or verification)
     * @param {string} tab The active tab.
     */
    setActiveTab(tab) {
      this.activeTab = tab;
    },
    /**
     * After saving the file this method emits the results back to the parent compoennt.
     */
    saveResults() {
      // Save the results
      // Emit the emails array to the parent component
      this.$emit("upload", {
        uploadName: this.uploadName,
        uploadCount: this.uploadCount,
        uploadedEmails: this.uploadedEmails,
      });

      // Close the modal
      this.closeModal();
    },
  },
};
</script>
