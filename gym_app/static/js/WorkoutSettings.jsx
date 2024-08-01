import React, { useState, useEffect } from 'react'; 
import { TextField, Button, Container, Grid, ButtonGroup, Typography } from '@mui/material';

const WorkoutSettings = () => {
    // Get user data from script tag
    const userDataScript = document.getElementById('user-data');
    const workoutsDataScript = document.getElementById('workouts-data');

    // Parse the user data
    const userData = JSON.parse(userDataScript.textContent);
    const workoutsData = JSON.parse(workoutsDataScript.textContent);

    // Debugging: Check the parsed workouts data
    console.log('Parsed workouts data:', workoutsData);

    // Ensure workoutsData is an array
    const initialWorkouts = Array.isArray(workoutsData) ? workoutsData : [];

    // Set up initial state with current workouts
    const [workouts, setWorkouts] = useState(initialWorkouts);

    // Add a new workout
    const addWorkout = () => {
        setWorkouts([...workouts, {name: '', id: `new-${Date.now()}`}]);
    };

    // Remove a workout
    const removeWorkout = (id) => {
        setWorkouts(workouts.filter(workout => workout.id !== id));
    };

    // Handle changes to workout names
    const handleChange = (id, value) => {
        setWorkouts(workouts.map(workout => workout.id === id ? {...workout, name: value } : workout));
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
            }
        });
    };

    return (
        <Container maxWidth="xs">
            <Grid container spacing={2}>
                {workouts.map((workout, index) => (
                    <Grid item xs={12} key={workout.id}>
                        <TextField
                            fullWidth
                            label={`Workout ${index + 1}`}
                            variant='outline'
                            color='secondary'
                            value={workout.name}
                            onChange={(e) => handleChange(workout.id, e.target.value)}
                        />
                        
                    </Grid>
                ))}
            </Grid>
            <ButtonGroup variant="contained" aria-label="Basic button group">
                <Button variant="contained" color="primary" onClick={addWorkout}>Add Workout</Button>
                <Button color="secondary" onClick={() => removeWorkout(workout.id)}>Remove</Button>
            </ButtonGroup>
            
            <Button variant="contained" color="primary" onClick={handleSubmit}>Save Changes</Button> 
        </Container>
    );
};

export default WorkoutSettings;