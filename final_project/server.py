from machinetranslation import translator as t
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    f = t.english_to_french(textToTranslate)
    return "Translated text to French: " + f

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    e = t.french_to_english(textToTranslate)
    return "Translated text to English: " + e

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
    # Write the code to render template

if __name__ == "__main__":
    app.run()
