import React from "react";
import './EmployeeCourseStats.css'

class EmployeeCourseStats extends React.Component {
    render() {
        return (
            <div className="row">
                <div className="col-12">
                    <div className="card text-white bg-success mb-3" style={{ width: '24rem' }} >

                        <div className="main-content">
                            <h2 className="title">Welcome to {this.props.name}</h2>
                            <p className="course">Course : {this.props.course} </p>
                            <blockquote className="course">&#123; name : {this.props.name}, course: {this.props.course} &#125;</blockquote>



                        </div>
                    </div>
                </div>
            </div>
        );
    };
}
export default EmployeeCourseStats;