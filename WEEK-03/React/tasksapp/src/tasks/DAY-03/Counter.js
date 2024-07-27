import React,{useState} from "react";
import './Counter.css'

function NumCounter() {
    const [initialValue, setInitialValue] = useState(0);
    const CounterIncrement = () => {
        let value = initialValue
        setInitialValue(value+1);
    }
    const CounterDecrement = () => {
        let value = initialValue
        setInitialValue(value-1);
        
    }
    
    return (
        <div className="card text-white bg-primary mb-3" style={{maxwidth: '18rem'}}>
            <div className="card-Header">Counter</div>
            <div className="card-body">
                <h4 className="card-content">{initialValue}</h4>
                <button type="submit" className="card-button-increment" onClick={CounterIncrement}>Increment</button>
                <button type="submit" className="card-button-decrement" onClick={CounterDecrement}>Decrement</button>
            </div>
        </div>
    );
}

export default NumCounter;