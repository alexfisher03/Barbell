document.getElementById("back-button").addEventListener("click", function(event){
    event.preventDefault();
    history.back();
});

const confirmButton = document.getElementById("confirm-password");

confirmButton.addEventListener("click", (event) => {
    event.preventDefault();
    window.location.href = "signin_screen.html";
});

const newPasswordInput = document.getElementById('new-password');
const confirmNewPasswordInput = document.getElementById('confirm-password-forgot');
const toggleNewPasswordButton = document.getElementById('toggle-new-password');
const toggleConfirmPasswordButton = document.getElementById('toggle-confirm-password');
const confirmPasswordButton = document.getElementById('confirm-password');

toggleNewPasswordButton.addEventListener('click', (event) => {
    event.preventDefault();
    togglePasswordVisibility(newPasswordInput, toggleNewPasswordButton);
});

toggleConfirmPasswordButton.addEventListener('click', (event) => {
    event.preventDefault();
    togglePasswordVisibility(confirmNewPasswordInput, toggleConfirmPasswordButton);
});

function togglePasswordVisibility(inputElement, toggleButton) {
  const inputType = inputElement.getAttribute('type');
  inputElement.setAttribute('type', inputType === 'password' ? 'text' : 'password');
  toggleButton.textContent = inputType === 'password' ? 'Hide' : 'Show';
}

confirmPasswordButton.addEventListener('click', (event) => {
  event.preventDefault(); 
  
});





