from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator")

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

@app.route("/english_to_french")
def translate_english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translator.english_to_french(textToTranslate)
    return translated_text

@app.route("/french_to_english")
def translate_french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translator.french_to_english(textToTranslate)
    return translated_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

