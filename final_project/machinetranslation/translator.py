'''
This file is used for translation fron eng to fr and fr to eng
'''

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

#language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    #function for translating from english to french
    french_text_dict = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = french_text_dict['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    #function for translating from french to english
    english_text_dict = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = english_text_dict['translations'][0]['translation']
    return english_text