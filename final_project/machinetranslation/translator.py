"""
This module is for converting english text to french text and vice versa
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION = '2018-05-01'

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(URL)


def english_to_french(english_text):
    """
    converts enlgish text to french text
    """
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr', source='en', target='fr').get_result()
    return french_text


def french_to_english(french_text):
    """
    converts french text to english text
    """
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en', source='fr', target='en').get_result()
    return english_text
