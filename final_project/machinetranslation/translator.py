"""
This module going to translation from English to Franch and Frach to English.
"""
#import json
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


#
def english_to_french(eng_text):
    """
    This function translate from Enghish to French
    """
    #write the code here
    translation = language_translator.translate(
    text = eng_text,
    model_id='en-fr').get_result()
    french_text=translation['translations'][0]['translation']
    return french_text

def french_to_english(fr_text):
    """
    This function translate from  French to English
    """
    #write the code here
    translation = language_translator.translate(
    text = fr_text,
    model_id='fr-en').get_result()
    english_text=translation['translations'][0]['translation']
    return english_text
