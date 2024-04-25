<template>
  <div class="py-12 excludeFromHTML">
    <nav
      :class="{ scrolled: !view.atTopOfPage }"
      class="fixed w-full pb-4 bg-white z-50 items-center top-0 animated"
    >
      <div
        class="bg-white lg:container w-full lg:mx-auto flex flex-wrap justify-between items-center z-50 top-0 animated px-2"
      >
        <div
          class="w-3/4 sm:w-3/5 md:w-1/2 lg:w-1/3 pt-2 lg:items-center lg:px-0"
        >
          <div class="cursor-pointer" @click="checkTestMode()">
            <img
              width="350"
              class="logo"
              src="@/assets/ITS_Kompetent_Logo.svg"
              alt="Logo"
            />
          </div>
        </div>

        <div
          id="burger"
          class="lg:hidden px-6"
          :class="{ active: open }"
          @click.prevent="toggle"
        >
          <slot>
            <button type="button" class="burger-button" title="Menu">
              <span class="burger-bar burger-bar--1" />
              <span class="burger-bar burger-bar--2" />
              <span class="burger-bar burger-bar--3" />
            </button>
          </slot>
        </div>

        <div
          id="menu"
          class="w-full lg:flex lg:items-center lg:w-auto"
          :class="open ? 'block' : 'hidden'"
        >
          <ul
            class="w-full pt-3 bg-white text-xl text-gray-500 lg:flex lg:justify-between lg:items-center pt-0 divide-y divide-gray-200 lg:divide-none"
          >
            <li
              v-if="!competenceTestStore.getTestButtonActive"
              class="flex justify-center lg:flex-none lg:justify-none h-14 lg:h-auto"
            >
              <router-link
                class="lg:p-4 py-2 hover:text-primary lg:shadow-none"
                to="/"
                @click="toggle"
              >
                Home
              </router-link>
            </li>
            <li
              v-if="!competenceTestStore.getTestButtonActive"
              class="flex justify-center lg:flex-none lg:justify-none h-14 lg:h-auto"
            >
              <router-link
                class="lg:p-4 py-2 hover:text-primary lg:shadow-none"
                to="/about"
                @click="toggle"
              >
                Über Uns
              </router-link>
            </li>
            <li
              v-if="!competenceTestStore.getTestButtonActive"
              class="flex justify-center lg:flex-none lg:justify-none h-14 lg:h-auto"
            >
              <router-link
                class="lg:p-4 py-2 hover:text-primary lg:shadow-none"
                to="/contact"
                @click="toggle"
              >
                Kontakt
              </router-link>
            </li>
            <li
              v-if="!competenceTestStore.getTestButtonActive"
              class="flex justify-center lg:flex-none lg:justify-none h-14 lg:h-auto"
            >
              <router-link
                class="lg:p-4 py-2 hover:text-primary lg:shadow-none"
                :class="{
                  'active-started':
                    competenceTestStore.getGetStartedButtonActive,
                }"
                to="/getstarted"
                @click="toggle"
              >
                Los geht's
              </router-link>
            </li>
            <li
              v-if="competenceTestStore.getTestButtonActive"
              class="h-14 flex text-primary justify-center lg:items-center lg:h-auto lg:justify-none shadow-xl lg:shadow-none"
            >
              <router-link v-slot="{ href }" to="/competence-tests">
                <button
                  :href="href"
                  :class="{
                    'active-link': competenceTestStore.getTestButtonActive,
                  }"
                  class="w-40 transform disabled:opacity-50 hover:scale-105 duration-500 border-primary border-2 my-2 py-1 px-4 mx-2 rounded hover:text-white hover:bg-primary"
                  :disabled="competenceTestStore.getTestButtonActive"
                  @click="toggleButton"
                >
                  Tests
                </button>
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <base-modal
      v-if="showModal"
      :show="showModal"
      :title="'Test beenden'"
      :content="'Möchten Sie fortfahren? Wenn sie Fortfahren klicken, wird der ITS-Kompetenztest beendet und Ihr aktueller Fortschritt geht verloren.'"
      @close="showModal = false"
      @confirm="pushToStart()"
    ></base-modal>
  </div>
</template>
<script>
import { useCompetenceTestStore } from "@/store/CompetenceTestStore";
import { mapState } from "pinia";
import BaseModal from "@/components/base/BaseModal";
export default {
  components: {
    BaseModal,
  },
  setup() {
    const competenceTestStore = useCompetenceTestStore();

    return { competenceTestStore };
  },
  data() {
    return {
      open: false,
      showModal: false,
      buttonActive: false,
      view: {
        atTopOfPage: true,
      },
    };
  },
  // a beforeMount call to add a listener to the window
  beforeMount() {
    window.addEventListener("scroll", this.handleScroll);
  },
  mounted() {},
  methods: {
    /**
     * Utilizes Vuex's `mapState` to bind the `getTestStarted` state from the `useCompetenceTestStore` to local component data.
     * This mapping allows the component to access `getTestStarted` directly from the component's computed properties.
     */
    ...mapState(useCompetenceTestStore, ["getTestStarted"]),
    /**
     *
     * Tracks click events in the navigation bar
     *
     */
    toggle() {
      this.open = !this.open;
      this.competenceTestStore.setTestButtonInactive();
      this.competenceTestStore.setGetStartedButtonInactive();
    },
    toggleButton() {
      this.open = !this.open;
      this.competenceTestStore.setTestButtonActive();
      this.competenceTestStore.setGetStartedButtonInactive();
    },
    /**
     * Tracks click events in the navigation bar for the Test Button
     * Sets the test button to inactive.
     *
     */
    checkTestMode() {
      if (this.competenceTestStore.testStarted) {
        this.showModal = true;
      } else {
        this.$router.push("/");
        this.competenceTestStore.setTestButtonInactive();
      }
    },
    /**
     * Ends the competence test state and removes it from local storage
     * Sets the test button to inactive.
     *
     */
    pushToStart() {
      this.competenceTestStore.endTest();
      this.competenceTestStore.setTestButtonInactive();
      this.competenceTestStore.setGetStartedButtonInactive();

      this.$router.push("/");
    },
    /**
     * Checks if the user has scrolled on the page. CSS classes are applied if the user has scrolled
     *
     */
    handleScroll() {
      // when the user scrolls, check the pageYOffset
      if (window.pageYOffset > 0) {
        // user is scrolled
        if (this.view.atTopOfPage) this.view.atTopOfPage = false;
      } else {
        // user is at top of page
        if (!this.view.atTopOfPage) this.view.atTopOfPage = true;
      }
    },
  },
};
</script>
<style>
nav.scrolled {
  @apply shadow-md;
  border-bottom: 0px;
}

.router-link-active {
  text-shadow: -0.04ex 0 currentColor, 0.04ex 0 currentColor;
  @apply text-primary;
}
.active-link {
  @apply text-white;
  @apply bg-primary;
}
.active-started {
  @apply text-primary;
  @apply font-bold;
}
button {
  cursor: pointer;
}

/* remove blue outline */
button:focus {
  outline: 0;
}

.burger-button {
  position: relative;
  height: 30px;
  width: 32px;
  display: block;
  z-index: 999;
  border: 0;
  border-radius: 0;
  background-color: transparent;
  pointer-events: all;
  transition: transform 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.burger-bar {
  background-color: #303e7a;
  position: absolute;
  top: 50%;
  right: 6px;
  left: 6px;
  height: 2px;
  width: auto;
  margin-top: -1px;
  transition: transform 0.6s cubic-bezier(0.165, 0.84, 0.44, 1),
    opacity 0.3s cubic-bezier(0.165, 0.84, 0.44, 1),
    background-color 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.burger-bar--1 {
  -webkit-transform: translateY(-6px);
  transform: translateY(-6px);
}

.burger-bar--2 {
  transform-origin: 100% 50%;
  transform: scaleX(0.8);
}

.burger-button:hover .burger-bar--2 {
  transform: scaleX(1);
}

.no-touchevents .burger-bar--2:hover {
  transform: scaleX(1);
}

.burger-bar--3 {
  transform: translateY(6px);
}

#burger.active .burger-button {
  transform: rotate(-180deg);
}

#burger.active .burger-bar--1 {
  transform: rotate(45deg);
}

#burger.active .burger-bar--2 {
  opacity: 0;
}

#burger.active .burger-bar--3 {
  transform: rotate(-45deg);
}
</style>
