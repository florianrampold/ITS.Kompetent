import { defineStore } from "pinia";
import { useStorage } from "@vueuse/core";

export const useCookieStore = defineStore("CookieStore", {
  state: () => {
    return {
      cookieDecision: useStorage("cookie", false),
    };
  },

  getters: {
    /**
     * Getter to retrieve cookie decision
     * @return {Object} The cookie decision
     */
    getCookieDecision() {
      return this.cookieDecision;
    },
  },

  actions: {
    /**
     * Saves the cookie decision
     * @param {Boolean} cookieDecision The cookie decision
     */
    setCookieDecision(cookieDecision) {
      this.cookieDecision = cookieDecision;
    },
  },
});
