function createOne(){
    console.log(document.getElementById("newOne"));
    var rows = window.prompt("Enter no.of rows ::");
    var cols = window.prompt("Enter no.of cols ::");
    for(let i=0;i<parseInt(rows);i++){
        var x = document.getElementById("newOne").insertRow(i);
        for(let j=0;j<parseInt(cols);j++){
            var y = x.insertCell(j).innerHTML="ROW - "+ i +" , COL - "+j;
        }
    }

}
