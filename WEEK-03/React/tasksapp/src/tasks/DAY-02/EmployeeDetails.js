import React from "react";
import Employee from "./Employee";
import EmployeeCourseStats from "./EmployeeCourseStats";
// import EmployeeForm from "./EmployeeForm";

class EmployeeDetails extends React.Component {
    render() {
        
        return (
            <div>
                <Employee name="sonu" age="23" />
                <Employee name="Loukya" age="1" />
                <Employee name="Divya" age="20" />
                <EmployeeCourseStats name="Gayathri" course="MBBS" />
                <EmployeeCourseStats name="Sonu" course="BTECH" />
            </div>
        );
    };
}
export default EmployeeDetails;