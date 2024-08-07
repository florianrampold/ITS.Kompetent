import APIService from "./api.service";

const TrainingsService = {
  /**
   * Asynchronously gets the training programs stored in the database
   * @returns {Promise<Object>} A promise that resolves to the data of the get response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  getTrainings: async function () {
    try {
      const response = await APIService.get("trainings");
      return response.data;
    } catch (error) {
      console.log(error);
    }
  },
  /**
   * Asynchronously gets the training programs paginated stored in the database
   * @param {Number} page The page number
   * @returns {Promise<Object>} A promise that resolves to the data of the get response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  getPaginatedTrainings: async function (page) {
    try {
      const response = await APIService.get(`trainings/?page=${page}`);
      return response.data;
    } catch (error) {
      console.log(error);
    }
  },
};

export default TrainingsService;
