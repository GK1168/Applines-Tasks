import React from "react";
import {NavLink} from 'react-router-dom';
import './navbar.css'

export const Navbar = () => {
   
    return(
        <nav>
            <NavLink to='/' > Home </NavLink> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <NavLink to='/f-c-components' > Components </NavLink>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <NavLink to='/image-cards' > ImageCards </NavLink>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <NavLink to='/employee-details' > EmployeeDetails </NavLink>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <NavLink to='/product-cart'> Product Cart </NavLink>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <NavLink to='/counter' > Counter </NavLink>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <NavLink to='/login-form' > Login Form </NavLink>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <NavLink to='/chart' > Chart </NavLink>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <NavLink to='/chart1' > chart1 </NavLink>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        </nav>
    );
}