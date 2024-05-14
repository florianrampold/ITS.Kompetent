<template>
  <div v-if="!getCookie" class="bg-primary">
    <div class="mx-auto py-3 px-3 sm:px-6 lg:px-8">
      <div class="flex flex-wrap items-center justify-between">
        <div class="flex sm:w-0 sm:flex-1 items-center">
          <span class="flex rounded-lg bg-indigo-800 p-2">
            <MegaphoneIcon class="h-6 w-6 text-white"> </MegaphoneIcon>
          </span>
          <p class="ml-3 truncate font-medium text-white">
            <span class="md:hidden text-sm"
              >Wir verwenden Cookies.
              <a
                class="inline sm:hidden underline cursor-pointer text-sm"
                @click="openModal()"
                >Mehr erfahren</a
              >
            </span>
            <span class="hidden md:inline"
              >Wir verwenden technisch essentielle Cookies. Ein weiterer Cookie
              speichert, dass dieses Banner bereits gesehen wurde; er wird für
              einen Monat gespeichert.
            </span>
          </p>
        </div>
        <div
          class="order-3 mt-2 mx-4 w-full hidden sm:block sm:order-2 sm:mt-0 sm:w-auto"
        >
          <button
            class="flex items-center justify-center rounded-md border border-transparent bg-white px-4 py-2 text-sm font-medium text-primary shadow-sm hover:bg-indigo-50"
            @click="openModal()"
          >
            Einstellungen
          </button>
        </div>
        <div
          class="order-3 mt-2 flex items-center justify-center w-full flex-shrink-0 sm:order-2 sm:mt-0 sm:w-auto"
        >
          <button
            class="rounded-md border border-transparent bg-green-200 px-4 py-2 text-sm font-medium shadow-sm hover:bg-green-500"
            @click="saveCookies()"
          >
            Zur Kenntnis genommen
          </button>
        </div>
      </div>
    </div>
  </div>

  <cookie-modal
    v-if="showModal"
    :show="showModal"
    :title="'Ihre Cookie Einstellungen'"
    :content="'Wenn Sie eine Website besuchen, kann diese Informationen über Ihren Browser abrufen oder speichern. Dies geschieht meist in Form von Cookies. Hierbei kann es sich um Informationen über Sie, Ihre Einstellungen oder Ihr Gerät handeln. Grundfunktionen wie der Login sind ohne sie nicht möglich. Ein weiterer Cookie speichert, dass dieses Banner bereits gesehen wurde; er wird für einen Monat gespeichert. Cookies zur Gewährleistung der Betriebsbereitschaft können nicht deaktiviert werden, soweit wir sie verwenden, um unsere Dienste bereitzustellen. Dabei werden keine persönlichen Daten verarbeitet, die Rückschluss auf Ihre Person geben. Erfahren Sie mehr zu der technisch notwendigen Speicherung von Daten in unserer Datenschutzerklärung '"
    @close="showModal = false"
    @saveCookies="saveCookies()"
  ></cookie-modal>
</template>

<script>
import CookieModal from "@/components/base/CookieModal";
import Cookies from "js-cookie";
export default {
  name: "CookieBanner",
  components: { CookieModal },

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

  data() {
    return {
      showModal: false,
      showBanner: true,
      updateTrigger: false, // This is used to force updates
    };
  },
   /**
     * Determines if user blocks cookies by browser
     *
     */
  computed: {
    getCookie() {
      return !!Cookies.get("dataPolicySet") || this.updateTrigger;
    },
  },

  methods: {
    /**
     * Opens the modal
     *
     */
    openModal() {
      this.showModal = true;
    },
    /**
     * Saves the cookiee decision in the local storage.
     *
     */
    saveCookies() {
      //const expires = 30; // days until the cookie expires
      Cookies.set("dataPolicySet", true);
      this.updateTrigger = !this.updateTrigger; // Toggle to force reactivity
    },
  },
};
</script>
