/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./gym_app/templates/**/*.html",
],
  theme: {
    extend: {},
  },
  plugins: [
    require("@tailwindcss/aspect-ratio"),
],
};
