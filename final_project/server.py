from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_tofrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    tofrench = translator.english_tofrench(textToTranslate)
    return tofrench

@app.route("/frenchToEnglish")
def french_toenglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    toenglish = translator.french_toenglish(textToTranslate)
    return toenglish

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
