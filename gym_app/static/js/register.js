const registerButton = document.getElementById("register-button");
const signInButton = document.getElementById("sign-in-button");

registerButton.addEventListener("click", (event) => {
    event.preventDefault();
    window.location.href = "/profile/self/"; // Redirects to profile_self view
});

signInButton.addEventListener("click", (event) => {
    event.preventDefault();
    window.location.href = "/signin/"; // Redirects to signin view
});
