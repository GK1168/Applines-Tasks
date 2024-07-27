import React from 'react'
import './imageCard.css'



function Cards(props) {
    return (

        <div className="card" style={{ width: '16rem' }}>
            <img src={props.image} className="card-img-top" alt="..." />
            <div className="card-body">
                <h5 className="card-title">{props.title}</h5>
                <p className="card-text">
                    {props.description}
                </p>
                <a href="#" className="btn btn-primary">
                    Read More
                </a>
            </div>
        </div>


    );

}

export default Cards;