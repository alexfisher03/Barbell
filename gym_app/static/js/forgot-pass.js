$(document).ready(function() {
  
  // Function to toggle password visibility
  function togglePasswordVisibility(inputElement, toggleButtonElement) {
    const inputType = inputElement.attr('type'); // Using jQuery .attr()
    if (inputType === 'password') {
      inputElement.attr('type', 'text'); // Using jQuery .attr()
      toggleButtonElement.html('Hide'); // Using jQuery .html()
    } else {
      inputElement.attr('type', 'password'); // Using jQuery .attr()
      toggleButtonElement.html('Show'); // Using jQuery .html()
    }
  }

  // Event listener for Show/Hide functionality of New Password
  const toggleNewPasswordButton = $('#toggle-new-password'); // Using jQuery
  const newPasswordInput = $('#new-password'); // Using jQuery
  toggleNewPasswordButton.click(function(e) {
    e.preventDefault();
    togglePasswordVisibility(newPasswordInput, toggleNewPasswordButton);
  });

  // Event listener for Show/Hide functionality of Confirm New Password
  const toggleConfirmPasswordButton = $('#toggle-confirm-password'); // Using jQuery
  const confirmNewPasswordInput = $('#confirm-password-forgot'); // Using jQuery
  toggleConfirmPasswordButton.click(function(e) {
    e.preventDefault();
    togglePasswordVisibility(confirmNewPasswordInput, toggleConfirmPasswordButton);
  });

  // Event listener for Confirm button
  const confirmButton = $('#confirm-password'); // Using jQuery
  const usernameInput = $('#username'); // Using jQuery
  
  confirmButton.click(function(e) {
    e.preventDefault();

    const username = usernameInput.val(); // Using jQuery .val()
    const newPassword = newPasswordInput.val(); // Using jQuery .val()
    const confirmPassword = confirmNewPasswordInput.val(); // Using jQuery .val()
    
    if (newPassword !== confirmPassword) {
      alert('Passwords do not match!');
      return;
    }
    
    // Check if username exists
    checkIfUsernameExists(username).then((doesExist) => {
      if(!doesExist) {
        alert('Username does not exist!');
        return;
      }
      
      // Submitting the new password
      $.post("/reset_password/", {
        username: username,
        new_password: newPassword,
        confirm_password: confirmPassword,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
      })
      .done(function() {
        window.location.href = '/profile/self/';
      })
      .fail(function() {
        alert('Failed to reset password.');
      });
    });
  });
});

// Dummy implementation, replace this with a real AJAX request
function checkIfUsernameExists(username) {
  return new Promise((resolve) => {
    resolve(true);
  });
}



