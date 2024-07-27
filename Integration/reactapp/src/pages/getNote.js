import React, { useState } from 'react'
import axios from "axios"


var baseURL = "http://localhost:8000/djangoapp/note/" 
export const GetNote = () => {
    const [notes,setNotes] = useState([]);
    const [value,setValue] = useState(0);

    const getAllHandler = () => {
        axios.get(baseURL)
        .then((response) => {
        console.log(response.data)
        setNotes(response.data)})
    }

    const getSingleNoteHandler = (id) =>{
        console.log(id)
        axios.get(`${baseURL}${id}`)
        .then((response) => {
        console.log(response.data)
        setNotes(response.data)})
    }
    return (
        <>
            <button onClick={getAllHandler}>GetAll</button>
            <input type='number' placeholder='enter id' onChange={(e) => setValue(e.target.value)}/>
            <button onClick={()=>getSingleNoteHandler(value)}>GetIDNOte</button>
        </>
    )
}
