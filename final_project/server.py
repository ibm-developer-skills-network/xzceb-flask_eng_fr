from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench(english_text):
    ''' Translate English to French '''
    textToTranslate = request.args.get('textToTranslate')
    french_text = translator.englishToFrench(textToTranslate)   
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish(french_text):
    ''' Translate French to Enflish '''
    textToTranslate = request.args.get('textToTranslate')
    english_text = translator.frenchToEnglish(textToTranslate)  
    return english_text

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    #app.run(debug = True, port = 5000)
    app.run(host = "0.0.0.0", port = 8080)