import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    "Translated text to French" = translator.english_to_french()
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    "Translated text to English" = translator.french_to_english()
    return "Translated text to English"

@app.route("/index")
def renderIndexPage():
    # Write the code to render template
    return render_index('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
