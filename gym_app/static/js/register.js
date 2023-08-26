document.addEventListener("DOMContentLoaded", function() {
    const registrationForm = document.querySelector('.registration-form');

    registrationForm.addEventListener('submit', function(e) {
        let valid = true;
        const username = document.getElementById('username');
        const email = document.getElementById('email');
        const phone = document.getElementById('phone');
        const password = document.getElementById('password');
        const confirmPassword = document.getElementById('confirm-password');
        
        // Check if fields are empty
        if (!username.value.trim()) {
            alert('Username cannot be empty.');
            valid = false;
        }
        
        if (!email.value.trim()) {
            alert('Email cannot be empty.');
            valid = false;
        }
        
        if (!phone.value.trim()) {
            alert('Phone number cannot be empty.');
            valid = false;
        }

        if (!password.value.trim()) {
            alert('Password cannot be empty.');
            valid = false;
        }

        if (!confirmPassword.value.trim()) {
            alert('Confirm Password cannot be empty.');
            valid = false;
        }

        if (password.value !== confirmPassword.value) {
            alert('Passwords do not match.');
            valid = false;
        }

        // Check if any of the gender radio buttons are selected
        const genderRadios = document.querySelectorAll('input[type="radio"][name="gender"]');
        let genderSelected = false;
        for (const radio of genderRadios) {
            if (radio.checked) {
                genderSelected = true;
                break;
            }
        }
        if (!genderSelected) {
            alert('Please select a gender.');
            valid = false;
        }

        // Prevent form submission if any validation failed
        if (!valid) {
            e.preventDefault();
        }
    });
});

const signInButton = document.getElementById("sign-in-button");

signInButton.addEventListener("click", (event) => {
    event.preventDefault();
    window.location.href = "/signin/"; // Redirects to signin view
});

