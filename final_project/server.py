from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translatedText = translator.english_to_french(textToTranslate)
    return translatedText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    englishText = translator.french_to_english(textToTranslate)
    return englishText

@app.route("/")
def renderIndexPage():
    return "Welcome to the translation service"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
