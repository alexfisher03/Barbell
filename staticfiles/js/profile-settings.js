const resetPasswordButton = document.getElementById('reset-password');
resetPasswordButton.addEventListener('click', function(event){
    event.preventDefault();
    window.location.href = this.getAttribute("data-url");
});

document.addEventListener('DOMContentLoaded',function(){
    document.getElementById('cancel-button').addEventListener('click', function(event) {
        event.preventDefault();
        const url = this.getAttribute('data-url');
        window.location.href = url;
    });
 });