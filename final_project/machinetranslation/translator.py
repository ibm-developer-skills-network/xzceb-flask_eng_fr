""" This module will translate English to French and vice versa """
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """ Function to translate English to French """
    if english_text is None:
        return None
    translation = language_translator.translate(
    english_text,
    model_id='en-fr').get_result()
    french_text = json.dumps(translation, indent=2, ensure_ascii=False)
    french_text_dict = json.loads(french_text)
    french_text = french_text_dict["translations"][0]["translation"]
    return french_text

def french_to_english(french_text):
    """ Function to translate French to English """
    if french_text is None:
        return None
    translation = language_translator.translate(
    french_text,
    model_id='fr-en').get_result()
    english_text = json.dumps(translation, indent=2, ensure_ascii=False)
    english_text_dict = json.loads(english_text)
    english_text = english_text_dict["translations"][0]["translation"]
    return english_text
