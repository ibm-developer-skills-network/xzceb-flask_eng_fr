"""
translator.py
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from ibm_watson import ApiException

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

print(authenticator)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    """
    englishToFrench
    """
    try:
        translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        return json.dumps(translation, indent=2, ensure_ascii=False)
    except ApiException as ex:
        return ""

def frenchToEnglish(french_text):
    """
    frenchToEnglish
    """
    try:
        translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        return json.dumps(translation, indent=2, ensure_ascii=False)
    except ApiException as ex:
        return ""




