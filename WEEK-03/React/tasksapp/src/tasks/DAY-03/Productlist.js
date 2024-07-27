import React from "react";
import ProductCard from "./Product";
import watch from '../../assets/watch.png'

function Productslist(){
    const products = [
        {
          SNO: "1",
          Image: watch,
          Name: "MI watch",
          price: 1500,
          qty: 15,
        },
        {
          SNO: "2",
          Image: watch,
          Name: "Boat watch",
          price: 2700,
          qty: 1,
        },
        {
          SNO: "3",
          Image: watch,
          Name: "FastTrack watch",
          price: 1300,
          qty: 3,
        },
        {
          SNO: "4",
          Image: watch,
          Name: "Samsung watch",
          price: 1800,
          qty: 11,
        },
        {
          SNO: "5",
          Image: watch,
          Name: "Apple watch",
          price: 3000,
          qty: 0,
        },
      ]
    return(
        <div>
            {products.map((items)=> (
            <ProductCard key={items.SNO} items={items} />
            ))}
            
        </div>
    );
}
export default Productslist;