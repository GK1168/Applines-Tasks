var rows;
var cols;
function createOne(){
    console.log(document.getElementById("newOne"));
    rows = window.prompt("Enter no.of rows ::");
    cols = window.prompt("Enter no.of cols ::");
    for(let i=0;i<parseInt(rows);i++){
        var x = document.getElementById("newOne").insertRow(i);
        for(let j=0;j<parseInt(cols);j++){
            var y = x.insertCell(j).innerHTML="ROW - "+ i +" , COL - "+j;
        }
    }

}

document.getElementById("change").onclick = function(){
    var row = window.prompt("Enter row index: ");
    var col = window.prompt("Enter column index: ");
    var content = window.prompt("Enter content : ");
    if(row>rows || col>cols){
        console.log("Out of index")
    }
    else{
        document.getElementById("newOne").rows[parseInt(row)].cells[parseInt(col)].innerHTML = content;
    }
}
document.getElementById("newOne").onmouseover = function(){
    window.location.reload();
}