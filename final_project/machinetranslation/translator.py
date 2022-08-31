'''This module is for translating texts'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)

translator = LanguageTranslatorV3(version='2018-05-01', 
authenticator=authenticator)

def english_to_french(english_text):
    '''This function translates text from english to french'''
    en_2_fr = translator.translate(text = english_text, model_id = 'en-fr').get_result()
    french_text = en_2_fr['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    '''This function translates text from french to english'''
    fr_2_en = translator.translate(text = french_text, 
    model_id = 'fr-en').get_result()
    english_text = fr_2_en['translations'][0]['translation']
    return english_text