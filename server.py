from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    ENGLISH_TEXT = input("Type in some English here: ")
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    FRENCH_TEXT = input("Type in some French here: ")
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
