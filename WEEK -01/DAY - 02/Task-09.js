const prompt = require("prompt-sync")({sigint:true});
var num1 = prompt("Enter first number :: ");

let count = 0;
for(let i=1;i<=num1/2;i++){
    if(num1%i==0){
        count++;
    }
}
if(count==1){
    console.log(num1 +" -- Prime Number");
}
else{
    console.log(num1 + "-- Not a Prime Number ");
}
