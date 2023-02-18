"""Module providingFunction translator."""
import json
import os
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
    '''English to french function'''
    translation = language_translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()
    french_text = translation['translations'][0]['translation']
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    return french_text


def french_to_english(french_text):
    '''French to english function'''
    translation = language_translator.translate(
        text=french_text,
        source='en',
        target='fr'
    ).get_result()
    english_text = translation['translations'][0]['translation']
    print(json.dumps(translation, indent=2, ensure_ascii=False))
    return english_text