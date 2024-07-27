const prompt = require("prompt-sync")({sigint:true});
var num1 = prompt("Enter first number :: ");
if(num1%2==0){
    console.log(num1 + " -- Even Number ")
}
else{
    console.log(num1 + " -- odd Number ")
}