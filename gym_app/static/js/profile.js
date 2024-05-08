document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('userRecords').getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05", "2023-01-06", "2023-01-07"], // These should be date strings
            datasets: [
                {
                    label: 'Demo Data1',
                    data: [65, 59, 80, 81, 56, 55, 40], 
                    fill: false,
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
});