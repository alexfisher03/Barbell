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
            alert('Please Enter a Username');
            valid = false;
        }
        
        if (!email.value.trim()) {
            alert('Email cannot be empty.');
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
            alert('Please select a gender');
            valid = false;
        }

        // Prevent form submission if any validation failed
        if (!valid) {
            e.preventDefault();
        }
    });
});

// Toggle password visibility for password1
document.getElementById('toggle-password1').addEventListener('click', function () {
    const passwordInput1 = document.getElementById('password');
    if (passwordInput1.type === 'password') {
      passwordInput1.type = 'text';
      this.textContent = 'Hide';
    } else {
      passwordInput1.type = 'password';
      this.textContent = 'Show';
    }
  });
  
  // Toggle password visibility for password2
  document.getElementById('toggle-password2').addEventListener('click', function () {
    const passwordInput2 = document.getElementById('confirm-password');
    if (passwordInput2.type === 'password') {
      passwordInput2.type = 'text';
      this.textContent = 'Hide';
    } else {
      passwordInput2.type = 'password';
      this.textContent = 'Show';
    }
  });