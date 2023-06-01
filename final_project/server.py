from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")
@app.route("/")
    # Write the code to render template
def render_index_page():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

@app.route("/englishToFrench")
    # Write your code here
def english_to_french():
    text_to_translate = translator.english_to_french('textToTranslate')
    french_translation = translator.english_to_french(text_to_translate)
    return french_translation

@app.route("/frenchToEnglish")
    # Write your code here
def french_to_english():
    text_to_translate  = request.args.get('textToTranslate')
    english_translation = translator.french_to_english(text_to_translate)
    return english_translation
     
    ##text_to_translate = request.args.get('textToTranslate')
    ##translator = Translator(from_lang='fr', to_lang='en')
    ##english_translation = translator.translate(text_to_translate)
    ##return english_translation
