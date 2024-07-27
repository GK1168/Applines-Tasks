import React from "react";
import Task1 from './task-03.js'

class Task extends React.Component{
    render(){
        return(
            <div>
                <h2>This is Class Component</h2>
                <Task1 />
            </div>
        );
    }
}

export default Task;