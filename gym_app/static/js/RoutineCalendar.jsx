import React, { useEffect, useState } from 'react';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';
import { Swiper, SwiperSlide } from 'swiper/react';
import 'swiper/css';
import 'swiper/css/pagination';
import { Pagination } from 'swiper/modules';
import Alert from '@mui/material/Alert';
import Collapse from '@mui/material/Collapse';
import IconButton from '@mui/material/IconButton';
import CloseIcon from '@mui/icons-material/Close';
import './calendarCSS/RoutineCalendar.css';

// New Component for Alert
const RoutineCalendarAlert = ({ hasWorkouts }) => {
    const [showAlert, setShowAlert] = useState(true);

    useEffect(() => {
        // Set timeout to hide alert after 5 seconds
        const timer = setTimeout(() => {
            setShowAlert(false);
        }, 5000);

        // Cleanup the timeout if component unmounts
        return () => clearTimeout(timer);
    }, []);

    return (
        <Collapse in={showAlert}>
            <div className="flex justify-center mb-6 ">
                <div className="sm:w-1/2">
                    <Alert
                        sx={{ width: '100%' }}
                        variant="outlined"
                        severity="info"
                        action={
                            <IconButton
                                aria-label="close"
                                color="inherit"
                                size="small"
                                onClick={() => {
                                    setShowAlert(false);
                                }}
                            >
                                <CloseIcon fontSize="inherit" />
                            </IconButton>
                        }
                    >
                        {hasWorkouts
                            ? "Drag Exercises To The Calendar And Make Your Routine"
                            : "To Add More Exercises Click Input Exercises"}
                    </Alert>
                </div>
            </div>
        </Collapse>
    );
};

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
            isMobile: window.matchMedia('(max-width: 640px)').matches,
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
                { id: 'landing-area', name: 'Workouts', tasks: workoutsData.map((_, index) => `task-${index + 1}`) }
            ]
        };
    }

    componentDidMount() {
        window.addEventListener('resize', this.updateIsMobile);
    }

    componentWillUnmount() {
        window.removeEventListener('resize', this.updateIsMobile);
    }

    updateIsMobile = () => {
        this.setState({ isMobile: window.matchMedia('(max-width: 640px)').matches });
    };

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

    render() {
        const { userData, isMobile } = this.state;
        const hasWorkouts = this.state.landingArea[0].tasks.length > 0;

        const pagination = {
            clickable: true,
            renderBullet: function (index, className) {
                const dayLabels = ['M', 'T', 'W', 'Th', 'F', 'S', 'Su'];
                return `<span class="${className} mx-12 text-xs p-1.5">${dayLabels[index]}</span>`;
            },
        };

        return (
            <div className='routine-calendar-wrapper p-4 sm:p-10'>
                <h2 className="text-center text-2xl font-bold mb-5">{userData.username}'s Workout Routine</h2>
                <hr className="my-4 sm:my-8 h-px border-t-0 bg-transparent bg-gradient-to-r from-transparent via-neutral-500 to-transparent opacity-25 dark:via-neutral-400" />
                <div className='flex justify-center mb-2'>
                    <h3 className="font-bold text-lg mb-2">Your Exercises</h3>
                </div>       

                {/* Replaced old alert with RoutineCalendarAlert component */}
                <RoutineCalendarAlert hasWorkouts={hasWorkouts} />

                <DragDropContext onDragEnd={this.onDragEnd} dragHandleProps={{ distance: 10 }}>

                    {/* Landing Area - Visible on all screen sizes */}
                    <Droppable droppableId="landing-area">
                        {(provided) => (
                            <div className="flex justify-center pb-3 sm:pb-0">
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
                                                        className="task-item p-2 mt-2 text-center text-xs sm:text-sm"
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

                    {/* Swiper for Mobile - Hidden on larger screens */}
                    {isMobile && (
                        <div className="block sm:hidden">
                            <div className="flex justify-center mb-6 ">
                                <div className="sm:w-1/2">
                                    <Alert sx={{ width: '100%' }} variant="outlined" severity="info">Swipe Through Days</Alert>
                                </div>
                            </div>
                            <Swiper
                                pagination={{
                                    clickable: true,
                                    el: '.custom-swiper-pagination',
                                    renderBullet: function (index, className) {
                                        const dayLabels = ['M', 'T', 'W', 'Th', 'F', 'S', 'Su'];
                                        return `<span class="${className} mx-12 text-xs p-1.5">${dayLabels[index]}</span>`;
                                    }
                                }}
                                modules={[Pagination]}
                                className="mySwiper"
                            >
                                {this.state.days.map(day => (
                                    <SwiperSlide key={day.id}>
                                        <Droppable droppableId={day.id}>
                                            {(provided) => (
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
                                                                {(provided, snapshot) => (
                                                                    <div
                                                                        ref={provided.innerRef}
                                                                        {...provided.draggableProps}
                                                                        {...provided.dragHandleProps}
                                                                        className={`task-item p-2 mt-2 text-center text-xs sm:text-sm ${
                                                                            snapshot.isDragging ? 'dragging' : ''
                                                                        }`}
                                                                    >
                                                                        {task.content}
                                                                    </div>
                                                                )}
                                                            </Draggable>
                                                        );
                                                    })}
                                                    {provided.placeholder}
                                                </div>
                                            )}
                                        </Droppable>
                                    </SwiperSlide>
                                ))}
                            </Swiper>
                            <div className="custom-swiper-pagination" />
                        </div>
                    )}

                    {/* Regular Grid for larger screens */}
                    {!isMobile && (
                        <div className="hidden sm:flex sm:justify-center">
                            <div className="routine-calendar">
                                {this.state.days.map(day => (
                                    <Droppable droppableId={day.id} key={day.id}>
                                        {(provided) => (
                                            <div className=''>
                                                <div
                                                    ref={provided.innerRef}
                                                    {...provided.droppableProps}
                                                    className="day-column pr-10 sm:p-4 border rounded shadow"
                                                >
                                                    <h3 className="font-bold text-sm mr-2 sm:text-lg sm:mb-2">{day.name}</h3>
                                                    {day.tasks.map((taskId, index) => {
                                                        const task = this.state.tasks.find(task => task.id === taskId);
                                                        return (
                                                            <Draggable draggableId={task.id} index={index} key={task.id}>
                                                                {(provided) => (
                                                                    <div
                                                                        ref={provided.innerRef}
                                                                        {...provided.draggableProps}
                                                                        {...provided.dragHandleProps}
                                                                        className="task-item ml-2 mr-2 sm:p-2 sm:mt-2 mt-2 text-center text-xs sm:text-sm"
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
                    )}

                </DragDropContext>
                <hr className="my-8 h-px border-t-0 bg-transparent bg-gradient-to-r from-transparent via-neutral-500 to-transparent opacity-25 dark:via-neutral-400" />
                <div className="mt-4 flex flex-col items-center">
                    <div className='w-1/2 sm:w-1/3 pb-3 sm:pb-2'>
                        <button className="twButtonblue text-sm sm:text-lg p-1.5 sm:p-2" onClick={this.showInputWorkouts}>Input Exercises</button>
                    </div>
                </div>
            </div>
        );
    }
}

export default RoutineCalendar;