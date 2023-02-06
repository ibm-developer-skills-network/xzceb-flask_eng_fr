from flask import Flask, render_template, request
from machinetranslation.translator import english_to_french, french_to_english

app = Flask("Web Translator")


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    response = english_to_french(textToTranslate)
    translated_text = response['translations'][0]['translation']
    return translated_text


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    response = french_to_english(textToTranslate)
    translated_text = response['translations'][0]['translation']
    return translated_text


@app.route("/")
def renderIndexPage():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
