const prompt = require("prompt-sync")({sigint:true});
let input = prompt("Enter a string :: ");
var substrings = [];
for(let i=0;i<input.length;i++){
    for(let j=i+1;j<=input.length;j++){
        substrings.push(input.slice(i,j));
    }
}
console.log("Given String :: "+ input);
console.log(substrings);