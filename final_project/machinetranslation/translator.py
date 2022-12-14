""" json module. """
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Prepare the Authenticator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# Translate English to French
def english_to_french(english_text):
    """ docstring. """
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()

    print(json.dumps(french_text, indent=2, ensure_ascii=False))

    return french_text

# Translate French to English
def french_to_english(french_text):
    """ docstring. """
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

    print(json.dumps(english_text, indent=2, ensure_ascii=False))

    return english_text
