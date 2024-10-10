/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: ["./gym_app/templates/**/*.html",
            "./node_modules/tw-elements/js/**/*.js"
],
  theme: {
    extend: {
      animation: {
        'pulse-fast': 'pulse-fast 1s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
      keyframes: {
        'pulse-fast': {
          '0%, 100%': { opacity: 1, transform: 'scale(1)' },
          '50%': { opacity: 0.5, transform: 'scale(1.1)' },
        },
      },
    },
  },
  plugins: [
    require("@tailwindcss/aspect-ratio"),
    require("tw-elements/plugin.cjs")
],
};
