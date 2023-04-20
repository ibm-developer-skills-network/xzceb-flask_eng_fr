
"""
This module provides functions for translating text from English to French and from French to English using IBM Watson Language Translator API.
"""
import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]
VERSION = "2018-05-01"

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=VERSION, authenticator=authenticator)
language_translator.set_service_url(url)


def english_to_french(english_test):
    if english_test!= "":
        translation = language_translator.translate(text=english_test, model_id="en-fr").get_result()
        french_text = translation["translations"][0]["translation"]
        return french_text
    else:
        return "Please enter text."


def french_to_english(french_text):
    """
    Translates French text to English using IBM Watson Language Translator API.

    Args:
        frenchText (str): The French text to be translated.

    Returns:
        str: The translated English text.
    """
    if french_text!= "":
        translation = language_translator.translate(text=french_text, model_id="fr-en").get_result()
        english_test = translation["translations"][0]["translation"]
        return english_test
    else:
        return "Please enter text."



