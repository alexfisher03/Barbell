document.getElementById("back-button").addEventListener("click", function(event){
    event.preventDefault();
    history.back();
});




const createGroup = document.getElementById("create-group");

createGroup.addEventListener("click",event =>{
    event.preventDefault();
    window.location.href = "group_screen.html";
});

