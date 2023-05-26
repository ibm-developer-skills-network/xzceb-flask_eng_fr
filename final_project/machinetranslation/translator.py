## not sure why they had ,,,py. but it seems to be the error.
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
## this should refer to .env for apikey and url
apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

languages = language_translator.list_languages().get_result()
print(json.dumps(languages, indent=2))
from flask import Flask, render_template, request
from translate import Translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
##def english_to_french():
def english_to_french(english_text):
    """
    Translate English text to French.

    Retrieves the text to translate from the request arguments.
    Uses the `translate` module to perform the translation.
    Returns the translated text in French.
    """
   ## text_to_translate = request.args.get('textToTranslate')
    ##translator = Translator(from_lang='en', to_lang='fr')
    ##french_translation = translator.translate(text_to_translate)
    ##return french_translation
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

@app.route("/frenchToEnglish")
##def french_to_english():
def french_to_english(french_text):
    """
    Translate French text to English.

    Retrieves the text to translate from the request arguments.
    Uses the `translate` module to perform the translation.
    Returns the translated text in English.
    """
  ##  text_to_translate = request.args.get('textToTranslate')
  ##  translator = Translator(from_lang='fr', to_lang='en')
  ##  english_translation = translator.translate(text_to_translate)
  ##  return english_translation
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text

@app.route("/")
def render_index_page():
    """
    Render the index.html template.

    Returns the rendered HTML template for the translator interface.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
