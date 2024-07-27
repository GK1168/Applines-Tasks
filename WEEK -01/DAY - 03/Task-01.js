const prompt = require("prompt-sync")({sigint:true});
var library = [
    {
    author: 'Bill Gates',
    title: 'The Road Ahead',
    readingStatus: true
    },
    {
    author: 'Steve Jobs',
    title: 'Walter Isaacson',
    readingStatus: true
    },
    {
    author: 'Suzanne Collins',
    title:  'Mockingjay: The Final Book of The Hunger Games', 
    readingStatus: false
    }]
library[0].authorChcek = "gopal";
delete library[0].authorChcek;
 //var input = prompt("Enter the title of the book ::");
 for(let i=0;i<library.length;i++){
    console.log("Author : "+library[i].author);
    console.log("gtitle : "+library[i].title);
    console.log("readingStatus : "+library[i].readingStatus);
    console.log("----------------------------------------------");
 }

 for(let i=0;i<library.length;i++){
    if(library[i].readingStatus === true){
        console.log("Already read ***** \'"+ library[i].author + "\' by "+ library[i].title)
    }
    else{
        console.log("You still need to read ***** \'"+ library[i].title+  "\' by "+library[i].author )
    }
 }
 console.log(library)