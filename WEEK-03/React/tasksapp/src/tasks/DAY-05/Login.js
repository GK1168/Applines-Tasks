import React, { useState } from 'react';
import './Login.css';

export default function FormLogin() {
    const [formData, setFormData] = useState({
        name:'',
        password:'',
        email:'',
        designation: '',
        textArea: '',
        gender : '',
        terms : ''
    });
    const FormDataHandler = (e) => {
        setFormData({
            ...formData,[e.target.name]:e.target.value
        });
    };

    const userDetails =(e) =>{
        e.preventDefault();
        console.log(formData)
    }
    
    return (
        <>
            <div className='form' >
                <div className='form-header'>
                    Register
                </div>
                <div className='form-content'>
                    <form>
                        <div className='typed'>
                            <input type='text' placeholder='username' name='name' value={formData.name} onChange={FormDataHandler}/> <br />
                            <input type='email' placeholder='email id' name='email' value={formData.email} onChange={FormDataHandler}/><br />
                            <input type='password' placeholder='password' name='password' value={formData.password} onChange={FormDataHandler}/><br />
                            <input type='text' placeholder='Select Designation' name='designation' value={formData.designation} onChange={FormDataHandler}/><br />
                            <textarea typeof='text' placeholder='comments' name='textArea' value={formData.textArea} onChange={FormDataHandler}/> <br />
                        </div>

                        <div className='check'>
                             Gender<br /><br />
                            <input type='radio' name='gender' value='female' onChange={FormDataHandler}/>Female
                            <input type='radio' name='gender' value='male'  onChange={FormDataHandler}/>Male
                            <br /> <br />
                            <input type='checkbox' name='terms' value={formData.terms} onChange={FormDataHandler}/>Accept Terms & Conditions
                        </div><br /> <br />
                        <button type='submit' onClick={userDetails}>Submit</button>
                    </form>
                </div>

            </div>
        </>
    );
}