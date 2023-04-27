from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench", methods = ['GET'])
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated = translator.englishToFrench(textToTranslate)
    return translated

@app.route("/frenchToEnglish", methods = ['GET'])
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated = translator.frenchToEnglish(textToTranslate)
    return translated

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
