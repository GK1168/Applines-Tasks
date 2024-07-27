import React from "react";
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const data = [
    { name: 'January', value1: 4, value2: 5 },
    { name: 'February', value1: 8, value2: 7 },
    { name: 'March', value1: 5, value2: 4 },
    { name: 'April', value1: 9, value2: 8 },
    { name: 'May', value1: 2, value2: 1 },
    { name: 'June', value1: 4, value2: 3 },
    { name: 'July', value1: 1, value2: 5 }
];

const BarChartComparison = () => {
    return (
        <>
            <h2 style={{fontSize:'24px',textAlign:'center'}}>Recharts Bar Chart</h2>
            <BarChart width={1500} height={800} data={data}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis tickCount={10}/>
                <Tooltip />
                <Legend verticalAlign="top" height={36} />
                <Bar dataKey="value1" fill="#BD19AE" />
                <Bar dataKey="value2" fill="#5DADE2" />
            </BarChart>
        </>
    );
}
export default BarChartComparison;