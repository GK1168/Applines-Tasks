var imagePath = `https://openweathermap.org/img/wn/50d@2x.png`
console.log(imagePath)
document.getElementById("image").src=imagePath



async function getStats(){
    var apikey = "46f80a02ecae410460d59960ded6e1c6";
    var cityName = document.querySelector('input').value;
    console.log(cityName); 
    var reqURL = `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=${apikey}&units=metric`;
    const response = await fetch(reqURL);
    var data = await response.json()
    console.log(data);
    var feelsLike = data.main.feels_like;
    var temp = data.main.temp;
    /*var cloud = data.weather.main;*/
    var humidity = data.main.humidity;
    var  windSpeed = data.wind.speed;
    console.log(feelsLike,temp,humidity,windSpeed);
    document.getElementById("feelsLike").innerHTML += feelsLike;
    document.getElementById("humidity").innerHTML += humidity +'%';
    document.getElementById("windSpeed").innerHTML += windSpeed+' m/s';
    document.getElementById("temp").innerHTML += temp+' &deg;C';
    cityName.value = "";
}