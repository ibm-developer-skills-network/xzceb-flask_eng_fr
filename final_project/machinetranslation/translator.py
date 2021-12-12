import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey  = os.environ['apikey']
url     = os.environ['url']


authenticator       = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)

language_translator.set_service_url(url)

def english_to_french(english_text):
    translation = language_translator.translate(
    text=english_text,model_id='en-fr').get_result()
    trans=translation['translations']
    final=trans[0].get('translation')
    return final

def french_to_english(french_text):
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    trans=translation['translations']
    final=trans[0].get('translation')
    return final
