document.addEventListener('DOMContentLoaded', function() {
    const forgotPasswordLink = document.querySelector('[data-action="forgotPassword"]');

    if (forgotPasswordLink) {
        forgotPasswordLink.addEventListener('click', function(event) {
            event.preventDefault();
            window.location.href = forgotPasswordLink.getAttribute('data-url');
        });
    }

    const signInButton = document.querySelector('[data-action="signIn"]');
    const signUpButton = document.querySelector('[data-action="signUp"]');

    signInButton.addEventListener('click', (event) => {
        event.preventDefault();
        // Check for successful login (need to add login verification logic)
        // if login successful, then:
        window.location.href = signInButton.getAttribute('data-url');
        // otherwise handle login error
    });

    signUpButton.addEventListener('click', (event) => {
        event.preventDefault();
        window.location.href = signUpButton.getAttribute('data-url');
    });
});


