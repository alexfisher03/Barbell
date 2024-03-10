document.addEventListener('DOMContentLoaded', (event) => {
    const fadeInElement = document.getElementById('fade-in-element');
    const fadeInElement2 = document.getElementById('fade-in-element2');
    const fadeInElement3 = document.getElementById('fade-in-element3');
    if (fadeInElement) {
      setTimeout(() => {
        fadeInElement.classList.remove('opacity-0');
        fadeInElement.classList.add('opacity-100', 'transition', 'duration-700');
        fadeInElement.style.transitionDelay = '300ms';
      }, 1);
    }
    if (fadeInElement2) {
      setTimeout(() => {
        fadeInElement2.classList.remove('opacity-0');
        fadeInElement2.classList.add('opacity-100', 'transition', 'duration-700');
        fadeInElement2.style.transitionDelay = '800ms';
      }, 1);
    }
    if (fadeInElement3) {
      setTimeout(() => {
        fadeInElement3.classList.remove('opacity-0');
        fadeInElement3.classList.add('opacity-100', 'transition', 'duration-700');
        fadeInElement3.style.transitionDelay = '1300ms';
      }, 1);
    }
});