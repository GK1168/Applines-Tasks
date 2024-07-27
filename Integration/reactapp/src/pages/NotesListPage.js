import React, { useEffect, useState } from 'react'
import axios from "axios";
import './NotesPageList.css';
import { GetNote } from './getNote.js';

var baseURl ="http://localhost:8000/djangoapp/note/"
var baseURL1 = "http://localhost:8000/djangoapp/note" 
export const NotesListPage = () => {
    
    let [notes,setNotes] = useState([]);
    const [isError,setIsError] = useState("");
    // useEffect(() => {
    //     async function getNotes(){
    //         try {
    //             const notes = await axios.get(baseURl)
    //             console.log(notes.data)
    //             setNotes(notes.data)
    //         } catch (error) {
    //             console.log(error)
    //             setIsError(error.message)
    //         }
    //     }
    //     getNotes()
    // }, [])
    
    // const getNotesHandler = () =>{
    //     axios.get(baseURl)
    //     .then((response) => {
    //     console.log(response.data)
    //     setNotes(response.data)
    // })
    // }
        
    
    const postNotesHandler = () =>{
        try {
            axios.post(baseURl,[{
                body:"Third one",
                created:"2202-09-12",
                updated:"2023-06-21"
            }])
            .then((response) => setNotes(response.data));
        } catch (error) {
            setIsError(error.message)
        }
    }

    const putNotesHandler = () => {
        try {
            axios.put(`${baseURL1}/12`,{
                body:"Twelvth Note",
                updated:"2023-11-09",
                created:"2021-09-23"
            })
            .then((response) => {
                setNotes(response.data)
            })
        } catch (error) {
            setIsError(error.message)
        }
    }

    const deleteNotesHandler = () => {
        try {
            axios.delete(`${baseURL1}/19`)
            .then(() => {
                alert("Note deleted")
            })
        } catch (error) {
            
        }
    }
    
  return (
    <div className='items'>
        {isError !== "" && <h2>{isError}</h2>}
       <div><GetNote /></div> 
       {/* <div><button  onClick={getNotesHandler}>GET NOTES</button></div>  */}
       <div><button  onClick={postNotesHandler}>POST NOTES</button></div> 
       <div><button  onClick={putNotesHandler}>UPDATE NOTES</button></div> 
       <div><button  onClick={deleteNotesHandler}>DELETE NOTES</button></div> 
    </div>
  )
}
