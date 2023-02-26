
import json
from flask import Flask, render_template, request

import machinetranslator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    french_text = machinetranslator.translator.english_to_french(
        english_text=textToTranslate
    )
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    english_text = machinetranslator.translator.french_to_english(
        french_text=textToTranslate
    )
    return english_text

@app.route("/")
def renderIndexPage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
