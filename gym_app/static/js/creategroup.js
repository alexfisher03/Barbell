document.getElementById("back-button").addEventListener("click", function(event){
    event.preventDefault();
    history.back();
});

const createGroup = document.getElementById("create-group");
console.log(createGroup);

document.addEventListener("DOMContentLoaded", function() {
    const createGroup = document.getElementById("create-group");
    console.log(createGroup);

    createGroup.addEventListener("click", event => {
        event.preventDefault();
        window.location.href = "/group";
    });
});

