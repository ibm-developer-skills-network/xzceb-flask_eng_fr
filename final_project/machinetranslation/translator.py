import json
import creds
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = creds.API_KEY
URL = "https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/c36cf875-e213-453e-bfab-31d31d3b9fe4"

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url(URL)


def english_to_french(text1):
    """
    This is going to translate from English To French
    """

    french_text = language_translator.translate(text=text1, model_id='en-fr').get_result()

    return french_text.get('translations')[0].get('translation')


def french_to_english(text2):
    """
    This is going to translate from French To English
    """

    english_text = language_translator.translate(text=text2, model_id='fr-en').get_result()

    return english_text.get('translations')[0].get('translation')
    