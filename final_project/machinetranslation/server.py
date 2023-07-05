from machinetranslation import translator
import machinetranslation
import json
from flask import Flask, render_template, request
import json

app = Flask('webtranslate')

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    return "text to french: {}".format(machinetranslation.translator.english_to_french(textToTranslate))


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return "text to english: {}".format(machinetranslation.translator.french_to_english(textToTranslate))

@app.route('/')
def html():
    return render_template ('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

