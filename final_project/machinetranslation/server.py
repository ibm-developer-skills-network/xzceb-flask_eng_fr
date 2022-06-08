from flask import Flask, render_template, request
import json
import translator

app = Flask("Web Translator", template_folder='templates')

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

@app.route("/englishToFrench")
def englishTorench():
    textToTranslate = request.args.get('textToTranslate')
    res = translator.english_to_french(textToTranslate)
    return res

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    res  = translator.french_to_english(textToTranslate)
    return res



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
