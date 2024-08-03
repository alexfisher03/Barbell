import React, { useState, useEffect } from 'react'; 
import { TextField, Button, Container, Grid } from '@mui/material';

const WorkoutSettings = () => {
    // Get user data from script tag
    const userDataScript = document.getElementById('user-data');
    const workoutsDataScript = document.getElementById('workouts-data');

    // Parse the user data
    const userData = JSON.parse(userDataScript.textContent);
    const workoutsData = JSON.parse(workoutsDataScript.textContent);

    // Ensure workoutsData is an array
    const initialWorkouts = Array.isArray(workoutsData) ? workoutsData : [];

    // Set up initial state with current workouts
    const [workouts, setWorkouts] = useState(initialWorkouts);

    // Add a new workout
    const addWorkout = () => {
        setWorkouts([...workouts, { name: '', id: `new-${Date.now()}` }]);
    };

    // Remove a workout
    const removeWorkout = (id) => {
        setWorkouts(workouts.filter(workout => workout.id !== id));
    };

    // Handle changes to workout names
    const handleChange = (id, value) => {
        setWorkouts(workouts.map(workout => workout.id === id ? { ...workout, name: value } : workout));
    };

    // Submit changes
    const handleSubmit = () => {
        fetch('/input_workouts/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: JSON.stringify({ workouts })
        }).then(response => {
            if (response.ok) {
                window.location.href = `/profile/${userData.profile_id}`;
            } else {
                response.json().then(data => {
                    alert(data.error || 'An error occurred while submitting the form. Please try again later.');
                });
            }
        }).catch(error => {
            console.error('Error:', error);
            alert('An error occurred while submitting the form. Please try again later.');
        });
    };

    return (
        <Container maxWidth="sm">
            <Grid container spacing={2}>
                {workouts.map((workout, index) => (
                    <Grid item xs={12} key={workout.id} container alignItems="center">
                        <Grid item xs={9}>
                            <TextField
                                fullWidth
                                label={`Workout ${index + 1}`}
                                value={workout.name}
                                color="secondary"
                                onChange={(e) => handleChange(workout.id, e.target.value)}
                                sx={{
                                    '& .MuiInputBase-root': {
                                        color: 'white',
                                    },
                                    '& .MuiInputLabel-root': {
                                        color: 'white',
                                    },
                                }}
                            />
                        </Grid>
                        <Grid item xs={3}>
                            <div className="p-3">
                                <Button className='hover:scale-105 ease-in-out duration-500' color="error" variant="outlined" onClick={() => removeWorkout(workout.id)}>Remove</Button>
                            </div>
                        </Grid>
                    </Grid>
                ))}
            </Grid>
            <div className="flex justify-center">
                <Button className="w-1/3 hover:scale-110 ease-in-out duration-75" color="" variant="" style={{ marginTop: '20px' }} onClick={addWorkout}>Add Workout</Button>
            </div>
            <div className="flex justify-center pb-3">
                <button className="twButtonpurple w-1/3 p-2" variant="contained" style={{ marginTop: '20px' }} onClick={handleSubmit}>Save Changes</button>
            </div>
        </Container>
    );
};

export default WorkoutSettings;
