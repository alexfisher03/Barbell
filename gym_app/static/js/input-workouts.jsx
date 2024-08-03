import React from 'react';
import { createRoot } from 'react-dom/client';
import WorkoutSettings from './WorkoutSettings.jsx';
import { Tooltip, Collapse, Ripple, initTWE,} from "tw-elements";
  
initTWE({ Tooltip, Collapse, Ripple });

document.addEventListener('DOMContentLoaded', function () {
    const root = createRoot(document.getElementById('input-workout-root'));
    root.render(<WorkoutSettings />);
});