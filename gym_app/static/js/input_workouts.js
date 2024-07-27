document.addEventListener('DOMContentLoaded',function(){
    document.getElementById('cancel-button').addEventListener('click', function(event) {
        event.preventDefault();
        const url = this.getAttribute('data-url');
        window.location.href = url;
    });
 });