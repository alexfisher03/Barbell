document.addEventListener('DOMContentLoaded',function(){
    var inputRepStatsButton = document.getElementById('input-rep-stats');
    inputRepStatsButton.addEventListener('click', function(event){
        event.preventDefault();
        window.location.href = 'input_rep_stats_screen.html';
    });
});

document.addEventListener('DOMContentLoaded', function(){
    var resetPasswordButton = document.getElementById('reset-password');
    resetPasswordButton.addEventListener('click', function(event){
        event.preventDefault();
        window.location.href = 'forgotpassword_screen.html';
    });
});

document.getElementById("confirm-profile-settings").addEventListener("click", function(event){
    event.preventDefault();
    window.location.href = 'profile_self_screen.html';
});

document.getElementById("back-button").addEventListener("click", function(event){
    event.preventDefault();
    history.back();
});