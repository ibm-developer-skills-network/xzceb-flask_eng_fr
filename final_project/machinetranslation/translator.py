"""Translates from English to French and French to English"""

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('AMM-1A4E5M9UQLZlLD1pip5Oub7RG2puLRNT9bpq_gQn')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/87fcc716-009a-4389-9135-57bc0d3733c8')

def english_to_french(english_text):
    """Translates from English to French"""
    french_text = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    return french_text['translations'][0]['translation']
def french_to_english(french_text):
    """Translates from French to English"""
    english_text = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    return english_text['translations'][0]['translation'] 
