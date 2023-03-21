""" Modules to start with translation service """
import json
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


# Add code to create an instance of the IBM Watson Language translator
authenticator = IAMAuthenticator('RfRS_emOQyPnPpl30_enozlkbG6SBMYHsBShBCtFlbtB')
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/0944c1c5-afe3-4afc-a434-3b212a54ceaf')


# Define functions
def english_to_french(english):
    """ Function to translate eng to fr """
    translation = language_translator.translate(text=english, model_id='en-fr').get_result()
    frenchtext = translation['translations'][0]['translation']
    return frenchtext


def french_to_english(french):
    """ Function to translate fr to eng """
    translation = language_translator.translate(text=french, model_id='fr-en').get_result()
    englishtext = translation['translations'][0]['translation']
    return englishtext
