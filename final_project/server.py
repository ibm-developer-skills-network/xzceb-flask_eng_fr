# Flask app for translator of English to French and vice vera
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    # Calls the English to French tranlator function
    textToTranslate = request.args.get('textToTranslate')    
    translated_text = translator.english_to_french(textToTranslate)
    return translated_text    

@app.route("/frenchToEnglish")
def frenchToEnglish():
    # Calls the French to English tranlator function
    textToTranslate = request.args.get('textToTranslate')    
    translated_text = translator.french_to_english(textToTranslate)    	
    return translated_text        

@app.route("/")
def renderIndexPage():
    # Returns the Home page
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
