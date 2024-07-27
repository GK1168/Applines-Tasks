import React from "react";
import {NavLink} from 'react-router-dom';
import './navbar.css'

export const NavbarSearch = () => {
   
    return(
        <nav>
            <NavLink to='/prod-cart' > product Cart </NavLink> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <NavLink to='/search' > Search </NavLink>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <NavLink to='' > prodcart </NavLink>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <NavLink to='/oncode' > oncode </NavLink>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        </nav>
    );
}