var initialValue = 0;
function addRows(){
    initialValue += 1;
    var tab = document.querySelector('table');
    var row = tab.insertRow(initialValue);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    cell1.innerHTML="Row-"+initialValue+" Col - 0"
    cell2.innerHTML="Row-"+initialValue+" Col - 1"
}