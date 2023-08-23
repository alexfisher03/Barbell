document.getElementById("back-button").addEventListener("click", function(event){
    event.preventDefault();
    history.back();
});

document.addEventListener('DOMContentLoaded', function() {
    const aboutLink = document.querySelector('.about-link');

    if (aboutLink) {
        aboutLink.addEventListener('click', function(event) {
            event.preventDefault();
            window.location.href = 'about_screen.html';
        });
    }
    const privacyLink = document.querySelector('.privacy-link');

    if (privacyLink){
        privacyLink.addEventListener('click', function(event){
            event.preventDefault();
            window.location.href = 'privacy_screen.html';
        });
    }
});
