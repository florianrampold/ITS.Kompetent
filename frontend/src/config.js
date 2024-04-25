// src/config.js

let frontendUrl;

if (process.env.NODE_ENV === "development") {
  frontendUrl = "http://localhost:8080";
} else {
  frontendUrl = "https://itskompetent.uni-goettingen.de";
}

// Export the variable after its value has been set
export { frontendUrl };
