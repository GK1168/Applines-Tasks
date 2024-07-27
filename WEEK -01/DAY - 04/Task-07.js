var dropDownElement = document.getElementById("dropdown");
dropDownElement.addEventListener('click',function(e){
    var list = dropDownElement.value;
    var value = dropDownElement.options[dropDownElement.selectedIndex].text; 
    console.log(value+" is clicked")
    dropDownElement.remove(dropDownElement.selectedIndex)
})