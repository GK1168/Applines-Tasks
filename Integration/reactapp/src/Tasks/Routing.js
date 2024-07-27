import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";

import { ProductCart } from './ProductCart';
import { NavbarSearch } from "./NavbarSearch";
import { DetailsList } from "./DetailsList";
import { ProdCart } from "./prodCart";
import OnCode from "./oncode";


export const Routing = () => {
    return (
        <BrowserRouter>
            <NavbarSearch />
            <Routes>
                <Route path="/prod-cart" element={<ProductCart />} />
                <Route path="/search" element={<DetailsList />} />
                <Route path="oncode" element={<OnCode />} />
                <Route path="" element={<ProdCart />} />
                
            </Routes>



        </BrowserRouter>
    );
}