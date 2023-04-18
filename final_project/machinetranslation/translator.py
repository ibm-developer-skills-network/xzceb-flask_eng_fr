import json
import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3


load_dotenv()

API_KEY = os.getenv('API_KEY')
URL = os.getenv('URL')

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator,
)
language_translator.set_service_url(URL)


def english_to_french(english_text: str) -> str:
    """Translate English text to French using IBM Watson Language Translator API.

    Args:
        english_text: A string of English text to be translated.

    Returns:
        A string of French text translated from the input English text.
        If the input text is empty or None, an empty string will be returned.

    Raises:
        ValueError: If the input text is not a string.
    """
    if not english_text:
        return ""

    if not isinstance(english_text, str):
        raise ValueError("Input text must be a string.")

    try:
        translation = language_translator.translate(
            text=english_text,
            source='en',
            target='fr'
        ).get_result()

        french_text = translation['translations'][0]['translation']

        return french_text

    except Exception as e:
        print(f"Failed to translate text: {e}")
        return ""


def french_to_english(french_text: str) -> str:
    """Translate French text to English using IBM Watson Language Translator API.

    Args:
        french_text: A string of French text to be translated.

    Returns:
        A string of English text translated from the input French text.
        If the input text is empty or None, an empty string will be returned.

    Raises:
        ValueError: If the input text is not a string.
    """
    if not french_text:
        return ""

    if not isinstance(french_text, str):
        raise ValueError("Input text must be a string.")

    try:
        translation = language_translator.translate(
            text=french_text,
            source='fr',
            target='en'
        ).get_result()

        english_text = translation['translations'][0]['translation']

        return english_text

    except Exception as e:
        print(f"Failed to translate text: {e}")
        return ""