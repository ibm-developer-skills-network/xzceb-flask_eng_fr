"""
Text translation methods that use IBM Watson
The following languages are covered:
    - English to French
    - French to English
"""

import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(URL)


def english_to_french(english_text:str) -> str:
    """Translates English text to French"""
    resp = language_translator.translate(english_text, model_id='en-fr')

    if resp.status_code==200:
        french_text = resp.result["translations"][0]["translation"]
        return french_text

    raise Exception(
        f'Cannot translate from English to French. Status code: {resp.status_code}'
    )


def french_to_english(french_text:str) -> str:
    """Translates French text to English"""
    resp = language_translator.translate(french_text, model_id='fr-en')

    if resp.status_code==200:
        english_text = resp.result["translations"][0]["translation"]
        return english_text

    raise Exception(
        f'Cannot translate from French to English. Status code: {resp.status_code}'
    )
    