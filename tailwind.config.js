/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: ["./gym_app/templates/**/*.html",
],
  theme: {
    extend: {},
  },
  plugins: [
    require("@tailwindcss/aspect-ratio"),
],
};
