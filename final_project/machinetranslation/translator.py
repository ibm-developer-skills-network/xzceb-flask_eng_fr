"""translator.py providing english to french translation"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['NIR5sLlxrRNU3BvKY6bCsFlaYLbHvv3RX-jbP0U5Ldto']
url = os.environ['https://api.us-south.language-translator.watson.cloud.ibm.com']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

def englishtofrench(englishtext):
    """This function translates english to french"""
    frenchtext=language_translator.translate(
        text=englishtext,
        model_id = 'en-fr').get_result()
    frenchtext = frenchtext['translations'][0]['translation']
    return frenchtext
   

def frenchtoenglish(frenchtext):
    """This function translates french to english"""
    englishtext = language_translator.translate(
        text=frenchtext,
        model_id ='fr-en').get_result()
    englishtext = englishtext['translations'][0]['translation']
    return englishtext
   
