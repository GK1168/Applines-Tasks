import React, { useEffect, useState } from 'react'
import axios from "axios";
import './ProductCart.css';
import Table from 'react-bootstrap/Table';
import Image from '../pages/image.webp'
import { Dialog } from 'primereact/dialog';
import { Button } from 'primereact/button';



let baseURL = "http://localhost:8000/productCart/prod-det/"
let operandURL ="http://localhost:8000/productCart/prod-deta/"
let changeURL = "http://localhost:8000/productCart/chg-con"
export const ProdCart = () => {
    const [Products, setProducts] = useState([]);
    const [isError, setIsError] = useState("");
    const [search, setSearch] = useState('');
    const [ID, setID] = useState(0);
    const [Name, setName] = useState('');
    const [Qty, setQty] = useState(0);
    const [Price, setPrice] = useState(0);
    const [Input, setInput] = useState("")
    let grandTotal = 0;
    const [inEditMode, setInEditMode] = useState({
        status: false,
    });

    
    const [visible, setVisible] = useState(false);


    async function getProdDetails() {
        try {
            await axios.get(baseURL)
            .then((response) => {
                console.log(response.data)
                setProducts(response.data)
            })
            
        } catch (error) {
            console.log(error)
            setIsError(error.message)
        }
    }

    useEffect(() => {
        getProdDetails()
    }, [])

    // const putHandlerDecrement = (prod) => {
    //     let value = prod['product_qty']
    //     if (value <= 0)
    //         value = 0
    //     else
    //         value = value - 1
    //     console.log(prod, value)
    //     const id = prod['id']
    //     console.log(prod['product_name'], "pppppp")
    //     try {
    //         axios.put(`${baseURL}${id}`, {
    //             product_name: prod['product_name'],
    //             product_qty: value,
    //             product_price: prod['product_price'],
    //         })
    //             .then((response) => {
    //                 prod = response.data
    //                 console.log(prod)
    //                 getProdDetails()
    //                 // setProducts(response.data)

    //             })
    //     } catch (error) {
    //         setIsError(error.message)
    //     }

    // }

    const putHandlerDecrement = (prod) => {
        try {
            let id = prod['id']
            console.log(prod,prod['id'])
            axios.put(`${baseURL}${id}/dec`,{
                product_name: prod['product_name'],
                product_qty: prod['product_qty'],
                product_price: prod['product_price'],
            })
            axios.get(`${operandURL}`)
            .then((response) => {
                console.log(response.data, "&&&&&&&&&&&&&&&&&&&&&&")
                
                setProducts(response.data)
                getProdDetails()

            })
           
        } catch (error) {
            console.log(error)
            setIsError(error.message)
        }
    }

    // const putHandlerIncrement = (prod) => {
    //     let value = prod['product_qty']
    //     value = value + 1
    //     console.log(prod, value, "**********")
    //     const id = prod['id']

    //     try {
    //         axios.put(`${baseURL}${id}`, {
    //             product_name: prod['product_name'],
    //             product_qty: value,
    //             product_price: prod['product_price'],
    //         })
    //             .then((response) => {
    //                 prod = response.data
    //                 console.log(prod)
    //                 getProdDetails()
    //                 // setProducts(response.data)

    //             })
    //     } catch (error) {
    //         setIsError(error.message)
    //     }
    // }

    const putHandlerIncrement = (prod) => {
        try {
            let id = prod['id']
            console.log(prod,prod['id'])
            axios.put(`${baseURL}${id}/inc`,{
                product_name: prod['product_name'],
                product_qty: prod['product_qty'],
                product_price: prod['product_price'],
            })
            axios.get(`${operandURL}`)

            .then((response) => {
                console.log(response.data, "&&&&&&&&&&&&&&&&&&&&&&")
                
                setProducts(response.data)
                getProdDetails()
            })
        } catch (error) {
            console.log(error)
            setIsError(error.message)
        }
    }

    const postAddProduct = () => {
        try {
            axios.post(baseURL, {
                product_id: parseInt(ID),
                product_name: Name,
                product_qty: parseInt(Qty),
                product_price: parseInt(Price),
            })
                .then((response) => {
                    console.log(response.data)
                    getProdDetails()
                })
        } catch (error) {
            console.log(error)
            setIsError(error.message)
        }
    }
    const footerContent = (
        <div>
            <Button label="Cancel" icon="pi pi-times" onClick={() => setVisible(false)} className="p-button-text" />
            <Button label="Add" icon="pi pi-check" onClick={postAddProduct} autoFocus />
        </div>
    );
    // const prodInfo = Products.filter((product) => product.product_name.toLowerCase().includes(Input)) 
    const searchHandler = (e) => {
        // e.preventDefault()
        // const search_value = e.target.value
        // window.location.reload(false);
        console.log(e,"***************")
        try {
             axios.get(`${baseURL}${Input}`)
            .then((response) => {
                console.log(response.data, "&&&&&&&&&&&&&&&&&&&&&&")
                setProducts(response.data)
            })
        } catch (error) {
            console.log(error)
            setIsError(error.message)
        }

    }

    

    const editHandler = (prod) =>{
        axios.put(`${changeURL}-put/${prod['id']}`,{
            product_name: Name,
            product_qty: prod['product_qty'],
            product_price: prod['product_price'],
        })
        axios.get(`${changeURL}`)

        .then((response) => {
            console.log(response.data, "&&&&&&&&&&&&&&&&&&&&&&")
                
            setProducts(response.data)
            getProdDetails()
        })
    }

    const deletehandler = (prod) => { 
        try {
            axios.delete(`${changeURL}-del/${prod['id']}`)
            .then(() => {
                alert("Product Deleted")
                getProdDetails()
            })
            
        } catch (error) {
            
        }
    }
    return (
        <>

            <div style={{ width: '1300px', marginLeft: '17%' }}>
                <div className='search-container'>
                    
                        <input className='inp-search' type='text' placeholder='search' value={Input} onChange={(e) => setInput(e.target.value)} />
                        <button><i className="pi pi-search" style={{ fontSize: '1.5rem' }} onClick={() => searchHandler(Input)} ></i></button>
                        {/* <button onClick={() => searchHandler(Input)}> search </button> */}

                </div>
                {/* <input id='inp-search' type='text' placeholder='search'  value = {Input} onChange={searchHandler} /> */}
                <Button label="Add-Product" icon="pi pi-external-link" style={{ float: 'right',marginRight: '100px' }} onClick={() => setVisible(true)} />
                {/* <Button label="Search" type='submit' icon="pi pi-external-link" style={{paddingLeft:'20px',marginLeft:'20px'}} onClick={(e) => searchHandler(Input)} /><br /> */}
                <Dialog header="Add Product" visible={visible} style={{ width: '700px', height: '600px', backgroundColor: '#7F8C8D', borderRadius: '10px solid red' }} onHide={() => setVisible(false)} footer={footerContent}>
                    <form id='add-prod' target='_parent'>
                        {/* <label className='form-label'> id : </label>
                        <input id='form-input' type="number" placeholder='Enter id' onChange={(e) => setID(e.target.value)}/><br /><br /> */}
                        <label className='form-label'>Product Name : </label>
                        <input id='form-input' type="text" placeholder='Enter Name' onChange={(e) => setName(e.target.value)} /> <br /><br />
                        <label className='form-label'>Quantity :  </label>
                        <input id='form-input' type="number" placeholder='Enter Quantity' onChange={(e) => setQty(e.target.value)} /><br /><br />
                        <label className='form-label'>Price :  </label>
                        <input id='form-input' type="number" placeholder='Enter price' onChange={(e) => setPrice(e.target.value)} /><br /><br />


                    </form>
                </Dialog>
            </div>
            <div>
                <br /><br /> {isError !== "" && <h2>{isError}</h2>}
                <Table className="tablecenterCSS table table-striped table-fixed">
                    <thead>
                        <tr>
                            <th>Product ID</th>
                            <th>Image</th>
                            <th>Name</th>
                            <th>Quantity</th>
                            <th>Price</th>
                            <th></th>
                            <th></th>
                            <th>Total</th>
                        </tr>
                    </thead>


                    <tbody>

                        {
                            Products !== [] && Products?.map(product => {
                                const total = eval(product.product_price * product.product_qty)
                                grandTotal += total;
                                return (

                                    <tr key={product.id}>
                                        <td>{product.id}</td>
                                        <td><img src={Image} alt={"image_pic"} style={{ width: '100px', }} /></td>
                                        {/* <td><input value = {product.product_name} onChange={(e) => setName(e.target.value)}/></td> */}
                                        <td>{product.product_name}</td>
                                        <td><button className='symbol' onClick={() => putHandlerDecrement(product)}> - </button>
                                            &nbsp;{product.product_qty}&nbsp;
                                            <button className='symbol' onClick={() => putHandlerIncrement(product)}> + </button></td>
                                        <td>{product.product_price}</td>
                                        <td>{<i className="fa-solid fa-pen-to-square" onClick={() => editHandler(product)}></i>}</td>
                                        <td>{<i className="fa-regular fa-trash-can" onClick={() => deletehandler(product)}></i>}</td>
                                        <td>{product.total_price}</td>
                                        
                                    </tr>



                                )
                            })}
                    </tbody>
                    <tfoot>
                        <tr>
                            <th></th><th></th><th></th><th></th><th></th><th></th><th></th>
                            <td colSpan={6} style={{ float: 'center',textAlign: 'center' }}> Grand Total : {grandTotal}</td>
                        </tr>
                    </tfoot>

                </Table>
            </div>

        </>
    )
}
