from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator",template_folder='templates')


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.english_to_french(textToTranslate)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return translator.french_to_english(textToTranslate)



@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template(str('index.html'))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080 ,debug=True)