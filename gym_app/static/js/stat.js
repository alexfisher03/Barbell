$.get("/get_stats", function(data){
  var stats = data;
  let table = document.getElementById('custom');
  showTable(table, stats);
}); 

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


function showTable(table, stats){
  let head = table.insertRow();
  let exercise = document.createElement("th");
  let sets = document.createElement("th");
  let reps = document.createElement("th");
  let edit = document.createElement("th");
  head.appendChild(exercise);
  head.appendChild(sets);
  head.appendChild(reps);
  head.appendChild(edit);
  let eText = document.createTextNode("Exercise");
  let sText = document.createTextNode("Sets");
  let rText = document.createTextNode("Reps");
  let edText = document.createTextNode("Delete");
  exercise.appendChild(eText);
  sets.appendChild(sText);
  reps.appendChild(rText);
  edit.appendChild(edText);
  // Create rows
  for(let i = 0; i < Object.keys(stats).length; i++){
    let baby = table.insertRow();
    // create entries in row
    for(let j = 0; j < 4; j++){   
      let cell = baby.insertCell();
      if(j != 3){
        let data;   
        if(j == 0){
            data = stats[i]['exercise_name']
          }else if(j == 1){
            data = stats[i]['num_sets']
          }else if(j==2){
            data = stats[i]['num_reps']
          }
          let text = document.createTextNode(data);
          cell.appendChild(text);
      }else{
        let deleteButton = document.createElement("button");
        deleteButton.textContent = "DELETE";
        deleteButton.className = "profile-button";
        let deleteForm = document.createElement("form");
        deleteForm.setAttribute("method", "delete");
        deleteButton.type = "submit";
        cell.appendChild(deleteForm);
        deleteForm.appendChild(deleteButton);
      }
    }
  }
}

