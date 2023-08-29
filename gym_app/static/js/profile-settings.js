document.addEventListener('DOMContentLoaded',function(){
    var inputRepStatsButton = document.getElementById('input-rep-stats');
    inputRepStatsButton.addEventListener('click', function(event){
        event.preventDefault();
        window.location.href = this.getAttribute("data-url");
    });
});

const resetPasswordButton = document.getElementById('reset-password');
resetPasswordButton.addEventListener('click', function(event){
    event.preventDefault();
    window.location.href = this.getAttribute("data-url");
});

document.getElementById("back-button").addEventListener("click", function(event){
    event.preventDefault();
    history.back();
});