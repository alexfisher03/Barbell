document.addEventListener('DOMContentLoaded', function() {
    const forgotPasswordLink = document.querySelector('[data-action="forgotPassword"]');

    if (forgotPasswordLink) {
        forgotPasswordLink.addEventListener('click', function(event) {
            event.preventDefault();
            window.location.href = forgotPasswordLink.getAttribute('data-url');
        });
    }

    const signInButton = document.querySelector('[data-action="signIn"]');
    const signUpButton = document.getElementById("sign-up-button");

    signInButton.addEventListener('click', (event) => {
        event.preventDefault();
        // Check for successful login (need to add login verification logic)
        // if login successful, then:
        window.location.href = signInButton.getAttribute('data-url');
        // otherwise handle login error
    });

    if (signUpButton) {
        signUpButton.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent form submission or button default behavior
            window.location.href = "{% url 'register' %}"; 
        });
    }
});


