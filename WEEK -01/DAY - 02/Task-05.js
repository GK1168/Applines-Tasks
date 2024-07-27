const prompt = require("prompt-sync")({sigint:true});
var num = prompt("Enter range  number :: ");
let sum=0;
for(let i=0;i<num;i++){
    sum+=i;
}
console.log("Sum : "+ sum);