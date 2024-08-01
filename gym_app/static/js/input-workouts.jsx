import React from 'react';
import { createRoot } from 'react-dom/client';
import WorkoutSettings from './WorkoutSettings.jsx';

document.addEventListener('DOMContentLoaded', function () {
    const root = createRoot(document.getElementById('input-workout-root'));
    root.render(<WorkoutSettings />);
});