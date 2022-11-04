from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    translated = language_translator.translate(text=textToTranslate, model_id='en-fr').get_result()
    # Write your code here
    return translated

@app.route("/frenchToEnglish")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    translated = language_translator.translate(text=textToTranslate, model_id='fr-en').get_result()
    # Write your code here
    return translated

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
