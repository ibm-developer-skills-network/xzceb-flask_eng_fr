#Code to convert text from English to French and vice versa
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def english_To_French(englishText):
    '''Function to translate english text to french'''
    authenticatorkey = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticatorkey)
    language_translator.set_service_url(url)
    french_Text = language_translator.translate(text=englishText, model_id="en-fr").get_result()
    return french_Text['translations'][0]['translation']

def french_To_English(frenchText):
    '''Function to translate french text to english'''
    authenticatorkey = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticatorkey)
    language_translator.set_service_url(url)
    english_Text = language_translator.translate(text=frenchText, model_id="fr-en").get_result()
    return english_Text['translations'][0]['translation']
