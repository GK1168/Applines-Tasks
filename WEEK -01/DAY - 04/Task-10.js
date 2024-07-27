
function highlight(){
    var bold = document.querySelectorAll('b');
    //console.log(bold)
    for(let i=0;i<bold.length;i++){
        bold[i].style.color="red"
    }
}
function highlightChange(){
    var bold = document.querySelectorAll('b');
    //console.log(bold)
    for(let i=0;i<bold.length;i++){
        bold[i].style.color="black"
    }
}