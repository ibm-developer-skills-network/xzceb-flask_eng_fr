from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation 
app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    french_text = machinetranslation.english_to_french(text_to_translate)
    return "Translated text to French"

@app.route("/frenchToEnglish")
def french_to_english():
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    english_text = machinetranslation.french_to_english(text_to_translate)
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
