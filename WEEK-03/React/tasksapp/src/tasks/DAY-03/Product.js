import React, { useEffect, useState } from 'react'
import './product.css'

export default function ProductCard(props) {


    const [isAvailable, setIsAvailable] = useState('')
    const [textColour, setTextColour] = useState('')
    // const QuantityCheck = (value) => {
    //     console.log(value)
    //     if(value >= 10){
    //         setIsAvailable('Available')
    //     }
    //     else if( value<=10 && value >= 1){
    //         setIsAvailable('Almost Out of Stack')
    //     }
    //     else{
    //         setIsAvailable('Out of Stack')
    //     }
    // }
   useEffect((value)=>{
    value = props.items.qty;
    if(value >= 10){
        setIsAvailable('Available')
        setTextColour('green');
    }
    else if( value<=10 && value >= 1){
        setIsAvailable('Almost Out of Stack')
        setTextColour('orange');
    }
    else{
        setIsAvailable('Out of Stack')
        setTextColour('red');
    }
   },[props.items.qty])

    return (
      <div className='row roww'>
        
        <div className='col-3'>
            <img src={props.items.Image} alt={ 'WatchImage' } />
        </div>
        <div className='col-8'>
            <h1> {props.items.Name}</h1>
            <p>&#x20B9;{props.items.price}</p>
            <p style={{color : textColour, fontSize : '24px'}} >{isAvailable}</p>
        </div>
      </div>
    )
}
