'''en-fr and fr-en Translator module'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version_lt='2021-08-18'

authenticator = IAMAuthenticator(apiKey)
language_translator = LanguageTranslatorV3(\
    version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url)

def englishToFrench(englishText):
    #write the code here
    frenchText = language_translator.translate(\
        text=englishText, model_id='en-fr')
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    englishText = language_translator.translate(\
    text=frenchText, model_id='fr-en')
    return englishText
