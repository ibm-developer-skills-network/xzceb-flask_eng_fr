import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('nA_3AG9jCGWTOl-o5nXCoyGkZYNGMZeLhRP_ULwl4RW8')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
 )
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/9ac5757f-278e-448e-99d6-cb25d97fdb66')

def english_to_french(english_text):
    '''English to French'''
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    '''French to English'''
    translation = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
