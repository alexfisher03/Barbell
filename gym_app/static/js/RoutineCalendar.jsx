import React from 'react';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';
import Alert from '@mui/material/Alert';
import './calendarCSS/RoutineCalendar.css';

class RoutineCalendar extends React.Component {
    constructor(props) {
        super(props);

        let userData = {};
        let workoutsData = [];
        
        const userDataScript = document.getElementById('user-data');
        const workoutsDataScript = document.getElementById('workouts-data');
        
        if (userDataScript) {
            try {
                userData = JSON.parse(userDataScript.textContent);
            } catch (error) {
                console.error("Failed to parse user data JSON: ", error);
            }
        }

        if (workoutsDataScript) {
            try {
                workoutsData = JSON.parse(workoutsDataScript.textContent);
            } catch (error) {
                console.error("Failed to parse workouts data JSON: ", error);
            }
        }

        this.state = {
            userData,
            days: [
                { id: 'day-1', name: 'M', tasks: [] },
                { id: 'day-2', name: 'T', tasks: [] },
                { id: 'day-3', name: 'W', tasks: [] },
                { id: 'day-4', name: 'TH', tasks: [] },
                { id: 'day-5', name: 'F', tasks: [] },
                { id: 'day-6', name: 'Sat', tasks: [] },
                { id: 'day-7', name: 'Sun', tasks: [] }
            ],
            tasks: workoutsData.map((workout, index) => ({
                id: `task-${index + 1}`,
                content: workout.name
            })),
            landingArea: [
                { id: 'landing-area', name: 'Exercises', tasks: workoutsData.map((_, index) => `task-${index + 1}`) }
            ]
        };
    }

    onDragEnd = result => {
        const { destination, source, draggableId } = result;

        if (!destination) {
            return;
        }

        if (
            destination.droppableId === source.droppableId &&
            destination.index === source.index
        ) {
            return;
        }

        const start = source.droppableId === 'landing-area' 
            ? this.state.landingArea[0] 
            : this.state.days.find(day => day.id === source.droppableId);

        const finish = destination.droppableId === 'landing-area' 
            ? this.state.landingArea[0] 
            : this.state.days.find(day => day.id === destination.droppableId);

        if (start === finish) {
            const newTaskIds = Array.from(start.tasks);
            newTaskIds.splice(source.index, 1);
            newTaskIds.splice(destination.index, 0, draggableId);

            const newDay = {
                ...start,
                tasks: newTaskIds
            };

            if (start.id === 'landing-area') {
                this.setState({
                    landingArea: [{ ...newDay }]
                });
            } else {
                this.setState({
                    days: this.state.days.map(day => (day.id === newDay.id ? newDay : day))
                });
            }
            return;
        }

        const startTaskIds = Array.from(start.tasks);
        startTaskIds.splice(source.index, 1);
        const newStart = {
            ...start,
            tasks: startTaskIds
        };

        const finishTaskIds = Array.from(finish.tasks);
        finishTaskIds.splice(destination.index, 0, draggableId);
        const newFinish = {
            ...finish,
            tasks: finishTaskIds
        };

        if (start.id === 'landing-area') {
            this.setState({
                landingArea: [{ ...newStart }],
                days: this.state.days.map(day => (day.id === newFinish.id ? newFinish : day))
            });
        } else if (finish.id === 'landing-area') {
            this.setState({
                landingArea: [{ ...newFinish }],
                days: this.state.days.map(day => (day.id === newStart.id ? newStart : day))
            });
        } else {
            this.setState({
                days: this.state.days.map(day => {
                    if (day.id === newStart.id) return newStart;
                    if (day.id === newFinish.id) return newFinish;
                    return day;
                })
            });
        }
    };

    showInputWorkouts() {
        window.location.href = '/input_workouts';
    }

    showRecords() {
        // TODO:
        // Logic to switch to the records view 
    }

    render() {
        const { userData } = this.state;
        const hasWorkouts = this.state.landingArea[0].tasks.length > 0;

        return (
            <div className='routine-calendar-wrapper p-10'>
                <h2 className="text-center text-2xl font-bold mb-5">{userData.username}'s Workout Routine</h2>
                <hr class="my-8 h-px border-t-0 bg-transparent bg-gradient-to-r from-transparent via-neutral-500 to-transparent opacity-25 dark:via-neutral-400" />
                <div className='flex justify-center mb-2'>
                    <h3 className="font-bold text-lg mb-2">Your Exercises</h3>
                </div>
                {!hasWorkouts && (
                    <div className="flex justify-center mb-6">
                        <Alert sx={{ width: '50%' }} variant="outlined" severity="info">You Have No Workouts, Click Input Workouts To Add Some</Alert>
                    </div>
                    )}
                <DragDropContext onDragEnd={this.onDragEnd}>
                    <Droppable droppableId="landing-area">
                        {(provided) => (
                            <div className="flex justify-center">
                                <div
                                    ref={provided.innerRef}
                                    {...provided.droppableProps}
                                    className="landing-area gap-x-8 gap-y-4 p-4 border rounded shadow">
                                    {this.state.landingArea[0].tasks.map((taskId, index) => {
                                        const task = this.state.tasks.find(task => task.id === taskId);
                                        return (
                                            <Draggable draggableId={task.id} index={index} key={task.id}>
                                                {(provided) => (
                                                    <div
                                                        ref={provided.innerRef}
                                                        {...provided.draggableProps}
                                                        {...provided.dragHandleProps}
                                                        className="task-item p-2 mt-2 text-center text-sm"
                                                    >
                                                        {task.content}
                                                    </div>
                                                )}
                                            </Draggable>
                                        );
                                    })}
                                    {provided.placeholder}
                                </div>
                            </div>
                        )}
                    </Droppable>

                    <div className='flex justify-center'>
                        <div className="routine-calendar">
                            {this.state.days.map(day => (
                                <Droppable droppableId={day.id} key={day.id}>
                                    {(provided) => (
                                        <div className=''>
                                            <div
                                                ref={provided.innerRef}
                                                {...provided.droppableProps}
                                                className="day-column p-4 border rounded shadow"
                                            >
                                                <h3 className="font-bold text-lg mb-2">{day.name}</h3>
                                                {day.tasks.map((taskId, index) => {
                                                    const task = this.state.tasks.find(task => task.id === taskId);
                                                    return (
                                                        <Draggable draggableId={task.id} index={index} key={task.id}>
                                                            {(provided) => (
                                                                <div
                                                                    ref={provided.innerRef}
                                                                    {...provided.draggableProps}
                                                                    {...provided.dragHandleProps}
                                                                    className="task-item p-2 mt-2 bg-blue-500 text-white rounded text-sm"
                                                                >
                                                                    {task.content}
                                                                </div>
                                                            )}
                                                        </Draggable>
                                                    );
                                                })}
                                                {provided.placeholder}
                                            </div>
                                        </div>
                                    )}
                                </Droppable>
                            ))}
                        </div>
                    </div>
                </DragDropContext>
                <div className="mt-4 flex flex-col items-center">
                    <div className='w-1/3 pb-3'>
                        <button className="twButtonblue p-2" onClick={this.showInputWorkouts}>Input Workouts</button>
                    </div>

                    <div className='w-1/3'>
                        <button className="twButtonpurple p-2" onClick={this.showRecords}>Display Records</button>
                    </div>
                </div>
            </div>
        );
    }
}

export default RoutineCalendar;
