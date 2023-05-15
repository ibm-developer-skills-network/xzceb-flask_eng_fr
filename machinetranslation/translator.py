"""
This module provides functions for translating text between French and English
using IBM Watson Language Translator.

Module Description:
- The module initializes an instance of the IBM Watson Language Translator
  using the provided API key and URL.
- It defines two functions for translating text: french_to_english() and
  english_to_french().
"""

import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=authenticator
)

language_translator.set_service_url(url)


def french_to_english(french_text):
    """
    Translates a given French text to English using IBM Watson Language Translator.

    Args:
        french_text (str): The French text to be translated.

    Returns:
        str: The translated English text.
    """
    translation = language_translator.translate(text=french_text, model_id="fr-en").get_result()
    english_text = translation['translations'][0]['translation']
    return english_text


def english_to_french(english_text):
    """
    Translates a given English text to French using IBM Watson Language Translator.

    Args:
        english_text (str): The English text to be translated.

    Returns:
        str: The translated French text.
    """
    translation = language_translator.translate(text=english_text, model_id="en-fr").get_result()
    french_text = translation['translations'][0]['translation']
    return french_text


