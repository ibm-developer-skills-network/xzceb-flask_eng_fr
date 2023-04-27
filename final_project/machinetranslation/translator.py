# mymodule.py
# Author: John Doe
# Created: January 1, 2022

"""
Translator module.

Uses IBM Watson and IBM Cloud to translate text

"""
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

def english_to_french(english_text: str):
    """
    Translates english text to french.

    Args:
        english_text (str): English text to be translated to french.

    Returns:
        str: Translated french text.
    """
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return french_text

def french_to_english(french_text: str):
    """
    Translates french text to english.

    Args:
        french_text (str): French text to be translated to english.

    Returns:
        str: Translated english text.
    """
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return english_text
    