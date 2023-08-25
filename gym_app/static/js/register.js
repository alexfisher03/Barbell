const registerButton = document.getElementById("register-button");
const signInButton = document.getElementById("sign-in-button");

registerButton.addEventListener("click", (event) => {
    event.preventDefault();
    window.location.href = "{% url 'register' %}";
});

signInButton.addEventListener("click", (event) => {
    event.preventDefault();
    window.location.href = "{% url 'signin' %}";
});

