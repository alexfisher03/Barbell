const registerButton = document.getElementById("register-button");
const signInButton = document.getElementById("sign-in-button");

registerButton.addEventListener("click", (event) => {
    event.preventDefault();
    window.location.href = "profile_self_screen.html";
});

signInButton.addEventListener("click", (event) => {
    event.preventDefault();
    window.location.href = "signin_screen.html";
});