import React, { useState } from 'react'
import Table from 'react-bootstrap/esm/Table'
import data from './search.json'
import './detailslist.css'
import nextId from 'react-id-generator'

export const DetailsList = () => {
    const [Input,setInput] = useState("")
    // console.log(data.filter(user => user.first_name.toLowerCase().includes(Value)))
    const data1 = data.filter((user) => user.first_name.toLowerCase().includes(Input) || user.last_name.toLowerCase().includes(Input) || user.email.toLowerCase().includes(Input))
    return (
        <>
            <div className='search'>
                <input type="text" name='search-input' placeholder='search here' onChange={(e) => setInput(e.target.value)}/>
            </div>
            <Table className="tablecenterCSS table table-striped table-fixed">
                <thead>
                    <tr>
                        
                        <th scope="col">FirstName</th>
                        <th scope="col">LastName</th>
                        <th scope="col">Email</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        data1.map(record => {
                            return (
                                <tr key={nextId()}>
                                    
                                    <td>{record?.first_name}</td>
                                    <td>{record?.last_name}</td>
                                    <td>{record?.email}</td>
                                </tr>
                            )
                        })
                    }
                </tbody>

            </Table>


        </>
    )
}
