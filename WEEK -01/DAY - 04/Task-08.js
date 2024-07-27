const prompt = require("prompt-sync")({sigint:true})
var radius = prompt("Enter sphere radius::");
var pi = 3.14;
var area = Math.floor((4/3)*pi*radius*radius*radius);
console.log("Volume of the Sphere : "+area);