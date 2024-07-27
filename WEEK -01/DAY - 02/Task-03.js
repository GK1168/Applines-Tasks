string = "Applines is awesome"
console.log(string)
console.log("Length : "+ string.length);
console.log("Finiding Applines index from First :: "+string.indexOf("Applines"));
console.log("Finiding Applines index from Last :: "+string.lastIndexOf("Applines"));
console.log("Slicing data from 5 to 15 : "+ string.slice(5,15))
console.log("Getting subpart from 6th index upto 10 chars : "+ string.substr(6,10));
console.log("Converrting to uppercase : "+ string.toUpperCase());
console.log("Converrting to lowercase : "+ string.toLowerCase());
console.log("Concatenating substr to string : "+ string.concat(string.slice(10,20)));
console.log("Finding character at a particular position :"+ string.charAt(13));
console.log("spliiting string : "+ string.split(" "));

