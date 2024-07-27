//import { Navigation } from "./exportBasic.js";
function getDetails(){
    if(document.getElementById("male").checked){
        console.log("male is selected")
    }
    else if(document.getElementById("female").checked){
        console.log("female is selected")
    }
    else if(document.getElementById("others").checked){
        console.log("others is selected")
    }
    else{
        console.log("You are not selected gender")
    }
}

var dropDownElement = document.getElementById("dropdown");
dropDownElement.addEventListener('click',function(e){
    var list = dropDownElement.value;
    var value = dropDownElement.options[dropDownElement.selectedIndex].text; 
    console.log(value+"is clicked")
})



