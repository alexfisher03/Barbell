import React from 'react';
import { createRoot } from 'react-dom/client';
import RoutineCalendar from './RoutineCalendar.jsx';

document.addEventListener('DOMContentLoaded', function () {
    const root = createRoot(document.getElementById('routine-root'));
    root.render(<RoutineCalendar />);
});

