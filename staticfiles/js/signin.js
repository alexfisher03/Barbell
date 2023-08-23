document.addEventListener('DOMContentLoaded', function() {
    const forgotPasswordLink = document.querySelector('.forgot-password-link');

    if (forgotPasswordLink) {
        forgotPasswordLink.addEventListener('click', function(event) {
            event.preventDefault();
            window.location.href = 'forgotpassword_screen.html';
        });
    }
});

const signInButton = document.getElementById("sign-in-button");
const signUpButton = document.getElementById("sign-up-button");

signInButton.addEventListener("click", (event) => {
    event.preventDefault();
    window.location.href = "profile_self_screen.html";
});

signUpButton.addEventListener("click", (event) => {
    event.preventDefault();
    window.location.href = "register_screen.html";
});


