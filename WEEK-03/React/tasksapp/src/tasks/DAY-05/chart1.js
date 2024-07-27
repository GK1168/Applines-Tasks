import React from "react";
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
  Title,
  CategoryScale,
  LinearScale,
  BarElement,
} from "chart.js";
import { Bar } from "react-chartjs-2";


ChartJS.register(ArcElement, Tooltip,Title, Legend,CategoryScale, LinearScale, BarElement);

export const options = {
    responsive:true,
    plugins : {
        legend:{
            position:'top',
        },
        title:{
            display:true,
            text:'Chart.js Bar Chart'
        },
    },
  };

const labels = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
];
export const data = {
  labels,
  datasets: [
    {
      label: "Dataset1",
      data: [4, 8, 5, 9, 2, 4, 1],
      backgroundColor: "#BD19AE",
    },
    {
      label: "dataset2",
      data: [5, 7, 4, 8, 1, 3, 5],
      backgroundColor: "#5DADE2",
    },
  ],
};


function BarChartComparison1() {
  return (
    <>
      <Bar data={data} options={options} />
    </>
  );
};
export default BarChartComparison1;
