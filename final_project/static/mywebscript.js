let translateToFrench = ()=>{
    textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let jsObjText = JSON.parse(xhttp.responseText);
            let translatedText = jsObjText.translations[0]["translation"];
            document.getElementById("translated_text").innerHTML = translatedText;
        }
    };
    xhttp.open("GET", "englishToFrench?textToTranslate"+"="+textToTranslate, true);
    xhttp.send();
}

let translateToEnglish = ()=>{
    textToTranslate = document.getElementById("textToTranslate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let jsObjText = JSON.parse(xhttp.responseText);
            let translatedText = jsObjText.translations[0]["translation"];
            document.getElementById("translated_text").innerHTML = translatedText;
        }
    };
    xhttp.open("GET", "frenchToEnglish?textToTranslate"+"="+textToTranslate, true);
    xhttp.send();
}

