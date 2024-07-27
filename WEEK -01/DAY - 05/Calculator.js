var data = document.getElementById("output")
var output = data.innerHTML;
console.log(output);

function addToOutput(op){
    if(data.innerHTML == 0){
        data.innerHTML = op;
    }
    else if(data.innerHTML == 00){
        data.innerHTML += op;
    }
    else{
        data.innerHTML += op;
        console.log(data.innerHTML);
    }
}

function clearOutput(){
    data.innerHTML = 0;
}

function deleteLast(){
    data.innerHTML = data.innerHTML.replace(data.innerHTML[data.innerHTML.length-1],"");
    console.log(data.innerHTML);
}

function calculateOutput(){
    var result = eval(data.innerHTML);
    data.innerHTML = result;
    console.log(result);
}