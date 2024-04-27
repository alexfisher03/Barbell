document.addEventListener('DOMContentLoaded', (event) => {
  const theme = getCookie('theme') || 'light';
  applyTheme(theme);

  const fadeInElements = [
    document.getElementById('fade-in-element'),
    document.getElementById('fade-in-element2'),
    document.getElementById('fade-in-element3')
  ];
  fadeInElements.forEach((element, index) => {
    if (element) {
      setTimeout(() => {
        element.classList.remove('opacity-0');
        element.classList.add('opacity-100', 'transition', 'duration-700');
        element.style.transitionDelay = `${500 * (index + 1)}ms`;
      }, 10);
    }
  });
});

function applyTheme(theme) {
  const body = document.body;
  body.classList.remove('light', 'dark');
  body.classList.add(theme);
  updateBackgroundImage(theme);
}

function updateBackgroundImage(theme) {
  const bgImage = theme === 'dark' ? '/static/images/dark-mesh-gradient.png' : '/static/images/meshgradientbg2.png';
  document.querySelector('.page-wrapper').style.backgroundImage = `url("${bgImage}")`;
}

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

document.getElementById('theme-toggle')?.addEventListener('click', function() {
  const currentTheme = document.body.classList.contains('dark') ? 'dark' : 'light';
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  document.cookie = "theme=" + newTheme + ";path=/;max-age=" + (60 * 60 * 24 * 30);
  applyTheme(newTheme);
});