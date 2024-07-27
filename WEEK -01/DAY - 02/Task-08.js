const prompt = require("prompt-sync")({sigint:true});
var base = prompt("Enter base value of the triangle :: ");
var height = prompt("Enter height value of the traingle ::");

console.log("Base : "+ base);
console.log("Height : "+ height);
let area = (1/2)*base*height;
console.log("Area : "+ area);