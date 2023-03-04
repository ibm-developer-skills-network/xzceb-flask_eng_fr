"""
This module contains functions for translating text between
English and French using the IBM Watson Language Translator API.
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

# IBM Watson service credentials
apikey = os.environ['apikey']
url = os.environ['url']

# Authenticator object
authenticator = IAMAuthenticator(apikey)

# Language Translator instance
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

# Set the service URL
language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Translates english_text to french
    """
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()

    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    """
    Translates french_text to english
    """
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()

    return english_text['translations'][0]['translation']
    