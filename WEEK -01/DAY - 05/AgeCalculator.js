
document.getElementById("submit").onclick = function(){
    var enteredDate = document.getElementById("date").value;
    var enteredMonth = document.getElementById("month").value;
    var enteredYear = document.getElementById("year").value;
    var date = enteredYear+"-"+enteredMonth+"-"+enteredDate;
    var givenDate = new Date(date)
    var currentDate = new Date();
    console.log("givenDate : "+givenDate);
    console.log("Currentdate : "+currentDate);
    var age = 2023 - enteredYear;
    //var age = currentDate-givenDate;
    console.log("Age : "+ age);
    document.getElementById("output").innerHTML = "You are "+age+" years old";
}