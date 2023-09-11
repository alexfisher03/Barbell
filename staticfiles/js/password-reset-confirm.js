$(document).ready(function() {
    function togglePasswordVisibility(inputElement, toggleButtonElement) {
        const inputType = inputElement.attr('type');
        if (inputType === 'password') {
            inputElement.attr('type', 'text');
            toggleButtonElement.html('Hide');
        } else {
            inputElement.attr('type', 'password');
            toggleButtonElement.html('Show');
        }
    }

    const toggleNewPasswordButton = $('#toggle-new-password');
    const newPasswordInput = $('#new-password');
    toggleNewPasswordButton.click(function(e) {
        e.preventDefault();
        togglePasswordVisibility(newPasswordInput, toggleNewPasswordButton);
    });

    const toggleConfirmPasswordButton = $('#toggle-confirm-password');
    const confirmNewPasswordInput = $('#confirm-password-forgot');
    toggleConfirmPasswordButton.click(function(e) {
        e.preventDefault();
        togglePasswordVisibility(confirmNewPasswordInput, toggleConfirmPasswordButton);
    });
});



