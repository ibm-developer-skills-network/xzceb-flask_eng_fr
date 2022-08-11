"""
Ma premiere Application de traduction de Texte avec IBM WATSON
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
AUTHENTICATOR = IAMAuthenticator(APIKEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR
)

LANGUAGE_TRANSLATOR.set_service_url(URL)

#LANGUAGES = LANGUAGE_TRANSLATOR.list_languages().get_result()
#print(json.dumps(LANGUAGES, indent=2))

def english_tofrench(english_text):
    """
    Traduit de l'anglais vers le francais
    """
    variable_un = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        model_id='en-fr').get_result()
    inter_variableun = variable_un['translations']
    inter_variabledeux = inter_variableun[0]
    french_text = inter_variabledeux['translation']
    return french_text

def french_toenglish(french_text):
    """
    Traduit du fracais vers l'anglais
    """
    variable_un = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        model_id='fr-en').get_result()
    inter_variableun = variable_un['translations']
    inter_variabledeux = inter_variableun[0]
    english_text = inter_variabledeux['translation']
    return english_text
