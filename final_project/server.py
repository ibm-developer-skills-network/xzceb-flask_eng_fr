import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    output_result = translator.english_to_french(textToTranslate)
    return output_result

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    output_result = translator.french_to_english(textToTranslate)
    return output_result

@app.route("/")
def renderIndexPage():
    return render_template('home.html')
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
