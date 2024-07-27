const prompt = require("prompt-sync")({sigint:true});
var numbers = prompt("Enter numbers :: ").split(" ");
console.log(numbers)
for(let i=0;i<numbers.length;i++){
    numbers[i] = parseInt(numbers[i])
}
let result = 0;

console.log(typeof(numbers));
console.log(numbers.sort())

for(let i=0;i<numbers.length;i++){
    if(numbers[i] > result){
        result = numbers[i]
    }
}
console.log("Max : "+ result)