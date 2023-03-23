"""
IBM Watson Language Translator Module
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

AUTHENTICATOR = IAMAuthenticator(API_KEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR
)

LANGUAGE_TRANSLATOR.set_service_url(URL)


def english_to_french(english_text='Hello'):
    """
    Translates English text to French
    """
    translation = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return translation["translations"][0]["translation"]


def french_to_english(french_text='Bonjour'):
    """
    Translates French text to English
    """
    translation = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return translation["translations"][0]["translation"]


if __name__ == '__main__':
    print(english_to_french('Hello'))
