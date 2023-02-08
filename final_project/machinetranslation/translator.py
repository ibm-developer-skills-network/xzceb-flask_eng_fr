"""
Translator of french to english text.
@Author: Olle Pontén
"""
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(URL)
#language_translator.set_disable_ssl_verification(True)
def englishToFrench(english_text):
    """
    Translates english text to french via Watson API
    """
    try:
        response = language_translator.translate(text=english_text, model_id='en-fr')
        french_text = response.get_result()['translations'][0]['translation']
    except ApiException as exception:
        print("Api failed with error: " +str(exception.code) + ": " + exception.message +"\n")
        return ""
    return french_text

def frenchToEnglish(french_text):
    """
    Translates french text to english via Watson API
    """
    try:
        response = language_translator.translate(text=french_text, model_id='fr-en')
        english_text = response.get_result()['translations'][0]['translation']
    except ApiException as exception:
        print("Api failed with error: " +str(exception.code) + ": " + exception.message + "\n")
        return ""
    return english_text
