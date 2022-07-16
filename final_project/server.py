from machinetranslation import translator
from flask import Flask, render_template, request
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask("Web Translator")
apikey = os.environ['apikey']
url = os.environ['url']

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    language_translator.set_service_url(url)
    frenchText = language_translator.translate(
            text = textToTranslate,
            model_id = 'en-fr').get_result()
    return frenchText

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    language_translator.set_service_url(url)
    englishText = language_translator.translate(
        text = textToTranslate,
        model_id='fr-en').get_result()
    return englishText

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    app.get("/", (req, res)
    return res.render(index);


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
