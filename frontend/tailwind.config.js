// tailwind.config.js
const colors = require("tailwindcss/colors");
module.exports = {
  purge: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  darkMode: false,
  theme: {
    extend: {
      keyframes: {
        shimmer: {
          "0%": { backgroundPosition: "-500px 0" },
          "100%": { backgroundPosition: "500px 0" },
        },
      },
      animation: {
        shimmer: "shimmer 2s infinite linear",
      },
      height: {
        18: "70px",
        26: "100px",
        34: "132px",
        66: "30rem",
        128: "32rem",
        150: "38rem",
        200: "48rem",
        220: "54rem",
        256: "60rem",
        300: "78rem",
      },
      width: {
        18: "70px",
        26: "100px",
        34: "132px",
        50: "18rem",
        52: "22rem",
        65: "14rem",
        66: "30rem",
        67: "38rem",
        128: "32rem",
        150: "38rem",
        200: "40rem",
        220: "48rem",
        256: "60rem",
        300: "78rem",
      },
      gap: {
        26: "98px",
      },
      minHeight: {
        "1/2": "50%",
      },
      colors: {
        primary: "#303e7a", //blue
        primaryAccent: "#3E519F",
        secondary: "#EB5757", //red
        secondaryAccent: "#E62929",
        action: "#2ecc71", //green
        green: colors.green,
        slate: colors.slate,
      },
      fontWeight: {
        button: 550,
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
