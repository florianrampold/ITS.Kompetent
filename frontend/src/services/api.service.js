import axios from "axios";

const APIService = {
  _401interceptor: null,

  /**
   * Retrieves the CSRF token from the browser cookies.
   * @returns {string|null} The CSRF token if found, otherwise null.
   */
  getCsrfToken() {
    let csrfToken = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, "csrfauthtoken".length + 1) === "csrfauthtoken" + "=") {
          csrfToken = decodeURIComponent(
            cookie.substring("csrfauthtoken".length + 1)
          );
          break;
        }
      }
    }
    return csrfToken;
  },

  /**
   * Initializes the Axios request configuration with a base URL and credentials flag.
   * @param {string} baseURL - The base URL to set for all Axios requests.
   */
  init(baseURL) {
    axios.defaults.baseURL = baseURL;
    axios.defaults.withCredentials = true;
  },

  /**
   * Sets common headers for all Axios requests, including CSRF token, content type, and accepted response type.
   */
  setHeader() {
    axios.defaults.headers.common["Content-Type"] = "application/json";
    axios.defaults.headers.common["Accept"] = "application/json";
    axios.defaults.headers.common["X-CSRFToken"] = this.getCsrfToken();
  },

  /**
   * Removes all custom headers set in the Axios default headers.
   */
  removeHeader() {
    axios.defaults.headers.common = {};
  },

  /**
   * Performs a GET request to the specified resource with optional configuration.
   * @param {string} resource - The endpoint to send the GET request to.
   * @param {Object} config - Optional configuration to enhance the request.
   * @returns {Promise} A promise that resolves to the response of the GET request.
   */
  get(resource, config = {}) {
    return axios.get(resource, config);
  },

  /**
   * Performs a POST request to the specified resource with the given data and optional configuration.
   * @param {string} resource - The endpoint to send the POST request to.
   * @param {Object} data - The data to be sent in the request body.
   * @param {Object} config - Optional configuration to enhance the request.
   * @returns {Promise} A promise that resolves to the response of the POST request.
   */
  post(resource, data, config = {}) {
    return axios.post(resource, data, config);
  },

  /**
   * Performs a PUT request to update resources at the specified endpoint.
   * @param {string} resource - The endpoint to send the PUT request to.
   * @param {Object} data - The data to update in the resource.
   * @returns {Promise} A promise that resolves to the response of the PUT request.
   */
  put(resource, data) {
    return axios.put(resource, data);
  },

  /**
   * Performs a DELETE request to remove resources at the specified endpoint.
   * @param {string} resource - The endpoint to send the DELETE request to.
   * @returns {Promise} A promise that resolves to the response of the DELETE request.
   */
  delete(resource) {
    return axios.delete(resource);
  },
};

export default APIService;
