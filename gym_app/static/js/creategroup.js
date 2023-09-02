document.addEventListener("DOMContentLoaded", function(){
    const createGroupForm = document.querySelector('.create-group-form');

    createGroupForm.addEventListener('submit', function(e) {
        let valid = true;
        //getting the two text inputs
        const groupName = document.getElementById('name');
        const bio = document.getElementById('biogroup');
        
        if (!groupName.value.trim()) {
            alert('Please Enter a Group Name');
            valid = false;
        }
        
        if (!bio.value.trim()) {
            alert('Email cannot be empty.');
            valid = false;
        }
      
        //getting the radio (button) input
        const privacyRadios = document.querySelectorAll('input[type="radio"][name="gprivacy"]');
        let privacySelected = false;
        for (const radio of privacyRadios) {
            if (radio.checked) {
                privacySelected = true;
                break;
            }
        }
        //saying that if neither radio is selected False valid variable
        if (!privacySelected) {
            alert('Please Select a Privacy Preference')
            valid = false;
        }

        //if the form isnt valid then cancel form submission
        if (!valid) {
            e.preventDefault();
        }
    });
});


document.getElementById("back-button").addEventListener("click", function(event){
    event.preventDefault();
    history.back();
});


