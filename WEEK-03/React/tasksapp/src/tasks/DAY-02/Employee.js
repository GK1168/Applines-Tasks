import React from "react";
import './Employee.css'



class Employee extends React.Component {
    render() {
        return (

            <div className="row">
                <div className="col-12">
                    <div className="card">
                        <div className="card-header">
                            Class based components with props
                        </div>
                        <div className="card-body">
                            <blockquote className="blocks">
                                <p>Welcome to Employee Component</p>

                            </blockquote>
                            <p>My Name is {this.props.name} and Iam {this.props.age} old</p>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}
export default Employee;