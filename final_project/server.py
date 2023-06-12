from machinetranslation import translator
from flask import Flask, render_template, request
from machinetranslation import machinetranslation
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    en_to_fr_translated = englishToFrench('textToTranslate')
    return en_to_fr_translated

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    fr_to_en_translated = frenchToEnglish('textToTranslate')
    return fr_to_en_translated

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return 'Index'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
