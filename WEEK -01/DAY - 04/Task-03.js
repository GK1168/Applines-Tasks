function getDetails(){
    var anchor = document.querySelector('a')
    console.log("Href : "+anchor.href);
    console.log("HrefLang :"+anchor.hreflang);
    console.log("Relation : "+anchor.rel);
    console.log("Target : "+ anchor.target);
    console.log("type attributes : "+anchor.type);
}