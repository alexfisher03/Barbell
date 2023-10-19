$.get("/get_stats", function(data){
  var stats = data;
  let table = document.getElementById('custom');
  showTable(table, stats);
});

// Assume user data from the backend has been retrieved
const userData = {};

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
  head.appendChild(exercise);
  head.appendChild(sets);
  head.appendChild(reps);
  let eText = document.createTextNode("Exercise");
  let sText = document.createTextNode("Sets");
  let rText = document.createTextNode("Reps");
  exercise.appendChild(eText);
  sets.appendChild(sText);
  reps.appendChild(rText);
  
  for(let i = 0; i < Object.keys(stats).length; i++){
    let baby = table.insertRow();
    for(let j = 0; j < 3; j++){   
     let cell = baby.insertCell();
     let data;   
     if(j == 0){
        data = stats[i]['exercise_name']
      }else if(j == 1){
        data = stats[i]['num_sets']
      }else{
        data = stats[i]['num_reps']
      } 
      let text = document.createTextNode(data);
      cell.appendChild(text);
    }
    /* let deleteButton = document.createElement("button");
    baby.appendChild(deleteButton); */
  }
  }