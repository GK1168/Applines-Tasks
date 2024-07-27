
function getImage(){
    var images = [];
    images[0] = "/web_images/apj.jpg"
    images[1] = "/web_images/bg.jpeg"
    images[2] = "/web_images/galaxy.avif"
    images[3] = "/web_images/sunrise.jpg"
    images[5] = "/web_images/valley.jpg"
    var body = document.getElementById('images');
    var number = Math.floor(Math.random()*images.length);
    console.log(images[number])
    body.innerHTML = "<img src=\'"+images[number]+"\'>"
}