import React, { useState } from 'react';
import './ProductCart.css'
import data from './products.json'
import Table from 'react-bootstrap/Table';
import { TotalMultiply } from './TotalMultiply';



export const ProductCart1 = () => {
  const [Quantity, setQuantity] = useState(0)
  const [Products,setProducts] = useState(data);
  // console.log(Products)
  let grandTotal = 0;
  console.log(Quantity)
  
  return (
    <>
      <div>
        <Table className="tablecenterCSS table table-striped table-fixed">
          <thead>
            <tr>
              <th>Product ID</th>
              <th>Image</th>
              <th>Name</th>
              <th>Quantity</th>
              <th>Price</th>
              <th>Total</th>
            </tr>
          </thead>


          <tbody>

            {
              Products && Products.map(product => {
                const total = eval(product.price * product.qty)
                grandTotal += total;
                return (




                  <tr key={product.SNO}>
                    <td>{product.SNO}</td>
                    <td><img src={product.Image} alt={"image_pic"} style={{ width: '100px', }} /></td>
                    <td>{product.Name}</td>
                    <td><button className='symbol' onClick={() => setQuantity(eval(product.qty - 1))}> - </button>
                      &nbsp;{product.qty}&nbsp;
                      <button className='symbol' onClick={() => setQuantity(eval(product.qty + 1))}> + </button></td>
                    <td>{product.price}</td>
                    <td><TotalMultiply num1 = {product.qty} num2 = {product.price} /></td>
                  </tr>



                )
              })}
              </tbody>
            <tfoot>
              <tr>
                <th></th><th></th><th></th><th></th>
                <th colSpan={'5'} style={{float:'right'}}> Grand Total : {grandTotal}</th>
              </tr> 
            </tfoot>
          
        </Table>
      </div>
    </>
  )
}













