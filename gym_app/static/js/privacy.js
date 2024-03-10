document.addEventListener('DOMContentLoaded', function () {
    const expandArrow = document.getElementById('expandArrow');
    const additionalPrivacyInfo = document.getElementById('additionalPrivacyInfo');

    expandArrow.addEventListener('click', function () {
      additionalPrivacyInfo.classList.toggle('hidden');
    });
  });