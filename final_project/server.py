__import__(machinetranslation)
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    textTranslated = english_to_french(textToTranslate)
    return

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    textTranslated = french_to_english(textToTranslate)
    return textTranslated

@app.route("/")
def renderIndexPage():
    render_template(index.html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
