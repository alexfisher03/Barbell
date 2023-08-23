// Assume user data from the backend has been retrieved
const userData = {
    benchPressMax: 225, // This is an example value, replace with actual user data
    // ... other user data fields
  };

  // Update the table cell content with user data
const benchPressMaxCell = document.getElementById('userBenchPressMax');
benchPressMaxCell.textContent = userData.benchPressMax;


//for back button
document.getElementById("back-button").addEventListener("click", function(event){
    event.preventDefault();
    history.back();
});