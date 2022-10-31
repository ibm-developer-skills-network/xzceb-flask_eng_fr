"""module to translate between english and french """
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('BiNv1rNa6uGIwM22F8D0bqDFbHFpNh_ao6r3Khl8TrCN')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/8468072f-3013-46ab-bd69-668ab9b19c38')

def english_to_french(english_text):
    """ function to translate from english to french"""
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return french_text

def french_to_english(french_text):
    """ function to translate from french to english """
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return english_text
  