from machinetranslation import translator
from flask import Flask, render_template, request
import json
"""Module provide Instance Watson Translator and Functions
   Translate English to French and French to Englist for a string. """
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
apikey='UHsdvPYktNXCAUlfhoqAgmNWT3mnidjM1eWAYAWYl_GT'
url='https://api.us-east.language-translator.watson.cloud.ibm.com/instances/e81d7774-1558-4df1-a0a4-90329e78cae4'
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
version='2023-04-28',
authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_to_french_text):
    """Function translate English to French validate null argument as an Error """
    if english_to_french_text == '':
        french_text = 'Error null string'
    else:
        french_text = language_translator.translate(
        text=english_to_french_text,
        model_id='en-fr').get_result()
        french_text = french_text['translations'][0]['translation']
    return french_text

def french_to_english(french_to_english_text):
    """Function translate French to English validate null argument as an Error """
    if french_to_english_text == '':
        english_text    = 'Error null string'
    else:
        english_text = language_translator.translate(
        text=french_to_english_text,
        model_id='fr-en').get_result()
        english_text = english_text['translations'][0]['translation']
    return english_text
app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    textTranslated = english_to_french(textToTranslate)
    return textTranslated

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    textTranslated = french_to_english(textToTranslate)
    return textTranslated

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
