from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translation = translator.english_to_french(textToTranslate)
    # Write your code here
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translation = translator.french_to_english(textToTranslate)
    # Write your code here
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
    # Write the code to render template

if __name__ == "__main__":
    app.run(debug=True, port=8080)
