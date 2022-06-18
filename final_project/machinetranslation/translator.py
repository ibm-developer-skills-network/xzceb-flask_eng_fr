# import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey=os.environ['apikey']
url=os.environ['url']

def translator_instance():
    authenticator=IAMAuthenticator(apikey)
    language_translator=LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    language_translator.set_service_url(url)
    return language_translator

def english_to_french(english_text):
    if english_text is None:
        return None
    language_translator=translator_instance()
    response=language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()

    french_text=response.get("translations")[0].get('translation')
    return french_text

def french_to_english(french_text):
    if french_text is None:
        return None
    language_translator=translator_instance()
    response=language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

    english_text=response.get("translations")[0].get('translation')
    return english_text
