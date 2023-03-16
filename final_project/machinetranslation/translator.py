import json
import os
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


authenticator = IAMAuthenticator(apikey)



language_translator = LanguageTranslatorV3(
    version='2019-02-28',
    authenticator=authenticator
)


language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    Translate English to French.

    Args:
        english_text (str): The English text to translate.

    Returns:
        str: The French translation of the input English text.
    """
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()

    french_text = translation['translations'][0]['translation']

    return french_text


def french_to_english(french_text):
    """
    Translate French to English.

    Args:
        french_text (str): The French text to translate.

    Returns:
        str: The English translation of the input French text.
    """
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()

    english_text = translation['translations'][0]['translation']

    return english_text




