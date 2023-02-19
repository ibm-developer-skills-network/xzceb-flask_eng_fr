"""Translator French to English."""
import json
import os
from ibm_watson import LanguageTranslatorV3 ,ApiException
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
    '''English to french via Watson API'''
    try:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr'
        )
        french_text = translation.get_result()['translations'][0]['translation']
    except ApiException as exception:
        print(f"Api error: {str(exception.code)}:{exception.message}" + "\n")
        print(json.dumps(translation, indent=2, ensure_ascii=False))
    return french_text


def french_to_english(french_text):
    '''French to english via Watson API'''
    try:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en'
        )
        english_text = translation.get_result()['translations'][0]['translation']
    except ApiException as exception:    
        print(f"Api error: {str(exception.code)}:{exception.message}" + "\n")
        print(json.dumps(translation, indent=2, ensure_ascii=False))
    return english_text