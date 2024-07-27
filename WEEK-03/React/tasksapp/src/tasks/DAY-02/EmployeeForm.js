import React,{useState} from "react";

function EmployeeForm(){
    return(
        <div>
            <label for="username">Username</label>
            <input type="text" name="username" placeholder="gopal" required/>
            <label for="username">Age</label>
            <input type="number" name="age" placeholder="10" required/>
            <button type="submit">Submit</button>
        </div>
    );
}

export default EmployeeForm;