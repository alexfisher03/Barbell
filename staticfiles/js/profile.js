import { Calendar } from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';
import listPlugin from '@fullcalendar/list';
import interactionPlugin from '@fullcalendar/interaction';

document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');
    var calendar = new Calendar(calendarEl, {
        plugins: [dayGridPlugin, listPlugin, interactionPlugin],
        initialView: 'dayGridWeek',
        headerToolbar: {
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridWeek,listWeek'
        },
        buttonText: {
        week: 'Week View',
        list: 'List View'
        },
        // Optionally remove dates from the day headers
        dayHeaderContent: (args) => {
        return {text: args.date.getDay()};  // Returns only the weekday
        },
        allDaySlot: false  // Removes the all-day slot row
    });

    calendar.render();


    const ctx = document.getElementById('userRecords').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["2024-05-01", "2024-05-02", "2024-05-03", "2024-05-04", "2024-05-05", "2024-05-06", "2024-05-07"], // These should be date strings
            datasets: [
                {
                    label: 'Exercise 1',
                    data: [65, 59, 80, 81, 56, 55, 40], 
                    fill: true,
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.2
                },
                {
                    label: 'Demo Data2',
                    data: [65, 19, 80, 31, 26, 45, 20], 
                    fill: false,
                    borderColor: 'rgb(175, 92, 192)',
                    tension: 0.2
                },
                {
                    label: 'Demo Data3',
                    data: [25, 39, 30, 11, 66, 25, 80], 
                    fill: false,
                    borderColor: 'rgb(75, 92, 192)',
                    tension: 0.2
                },
                {
                    label: 'Demo Data4',
                    data: [45, 69, 10, 21, 96, 65, 10], 
                    fill: false,
                    borderColor: 'rgb(5, 192, 92)',
                    tension: 0.2
                },
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                  labels: {
                    padding: 10
                  },
                  padding: {
                    bottom: 10
                  }
                }
              },
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'day'
                    },
                    title: {
                        display: true,
                        text: 'Date'
                    }
                },
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Value'
                    }
                }
            }
        }
    });

    const toggleButton = document.getElementById('toggleView');
    const calendarContainer = document.querySelector('.calendar-container');
    const chartContainer = document.querySelector('.chart-container');

    toggleButton.addEventListener('click', function () {
        if (calendarContainer.style.display === 'none') {
            calendarContainer.style.display = 'block';
            chartContainer.style.display = 'none';
            toggleButton.textContent = 'View Personal Records';
        } else {
            calendarContainer.style.display = 'none';
            chartContainer.style.display = 'block';
            toggleButton.textContent = 'View Weekly Routine';
        }
    });
});

