const prompt = require("prompt-sync")({sigint:true});
var num1 = prompt("Enter first number :: ");

if(num1 > 0){
    console.log(num1+" -- Positive")
}
else if (num1 < 0){
    console.log(num1 + " -- Negative")
}
else{
    console.log(num1 + " -- Zero")
}