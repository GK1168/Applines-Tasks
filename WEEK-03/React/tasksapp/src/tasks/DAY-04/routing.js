import { Navbar } from "../DAY-05/navbar";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Images from '../DAY-01/imagesList.js'
import Task from "../DAY-01/task-02.js";
import EmployeeDetails from "../DAY-02/EmployeeDetails";
import Productslist from "../DAY-03/Productlist";
import NumCounter from '../DAY-03/Counter.js'
import FormLogin from "../DAY-05/Login";
import BarChartComparison from "../DAY-05/chart";
import HomeDetails from "../DAY-01/Home";
import BarChartComparison1 from "../DAY-05/chart1";


export const Routing = () => {
    return (
        <BrowserRouter>
            <Navbar />
            <Routes>
                <Route path="/" element={<HomeDetails />} />
                <Route path="/f-c-components" element={<Task />} />
                <Route path="/image-cards" element={<Images />} />
                <Route path="/employee-details" element={<EmployeeDetails />} />
                <Route path="/product-cart" element={<Productslist />} />
                <Route path="/counter" element={<NumCounter />} />
                <Route path="/login-form" element={<FormLogin />} />
                <Route path="/chart" element={<BarChartComparison />} />

                <Route path="/chart1" element={<BarChartComparison1 />} />
            </Routes>



        </BrowserRouter>
    );
}