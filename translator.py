""" This file is for my final project """
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
MODEL_ID = 'en-it'
ENGLISH_TEXT = "Hello"
FRENCH_TEXT = "Bonjour"

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(ENGLISH_TEXT):
    """ Used to convert english to french """
    translation = "Nada"
    translation = language_translator.translate(
        text = ENGLISH_TEXT,
        model_id = MODEL_ID).get_result()
    return FRENCH_TEXT

def french_to_english(FRENCH_TEXT):
    """ Used to convert french to english """
    translation = "Nada"
    translation = language_translator.translate(
        text = FRENCH_TEXT,
        model_id = MODEL_ID).get_result()
    return ENGLISH_TEXT
