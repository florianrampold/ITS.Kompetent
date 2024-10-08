import APIService from "./api.service";

const JobProfileService = {
  /**
   * Asynchronously gets the plain jo profiles
   * @returns {Promise<Object>} A promise that resolves to the data of the get response
   * @throws {Error} Rethrows any error encountered during the API request.
   */
  getJobProfiles: async function () {
    const response = await APIService.get(`job_profiles`);
    return response.data;
  },
};

export default JobProfileService;
