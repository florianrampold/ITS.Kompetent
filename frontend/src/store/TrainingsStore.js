// auth.js

import { defineStore } from "pinia";
//import { useStorage } from "@vueuse/core";
import trainingsService from "../services/trainings.service";

export const useTrainingsStore = defineStore("trainings", {
  actions: {
    /**
     * Getter to retrieve the training programs
     * @returns {Promise<Object>} A promise that resolves to the training programs.
     */
    async getTrainings() {
      const response = await trainingsService.getTrainings();
      return response;
    },
    /**
     * Getter to retrieve the paginated training programs.
     * @returns {Promise<Object>} A promise that resolves to the paginated training programs.
     */
    async getPaginatedTrainings(page) {
      const response = await trainingsService.getPaginatedTrainings(page);
      return response;
    },
    /**
    * Getter to retrieve the threat categories
    * @returns {Promise<Object>} A promise that resolves to the threat categories.
    */
    async getTrainingCategories() {
      const response = await trainingsService.getTrainingCategories();
      return response;
    },
    /**
    * Getter to job profiles with associated training categories
    * @returns {Promise<Object>} A promise that resolves to the threat categories.
    */
    async getJobProfilesByTrainingCategories() {
      const response =
        await trainingsService.getJobProfilesByTrainingCategories();
      return response;
    },
  
  },
});
