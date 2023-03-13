import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version='2019-04-30'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(englishText):
    """
    This function translates english to french
    """
    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']

    return french_text

def french_to_english(frenchText):
    """
    This function translates french to english
    """
    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']

    return english_text
