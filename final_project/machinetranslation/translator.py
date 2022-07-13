import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['aDIJVpIiG7qcv0g6CLxrxM8MARwC25FSXzTj0A5TY-LB']
url = os.environ['https://api.us-east.language-translator.watson.cloud.ibm.com/instances/5ac36773-9b21-4cd0-b9ad-794af2154b61']

authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('{url}')

def englishToFrench(englishText):
    frenchText = language_translator.translate(
        text=englishText, 
        model_id='en-fr').get_result()
    return frenchText['Translations'][0]['translation']

def frenchToEnglish(frenchText):
    frenchText = language_translator.translate(
        text=frenchText, 
        model_id='en-fr').get_result()
    return frenchText['Translations'][0]['translation']
