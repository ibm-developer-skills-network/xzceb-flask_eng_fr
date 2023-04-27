"""Python File"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey = apikey)

instance = LanguageTranslatorV3(version = '2018-05-01', authenticator = authenticator)
instance.set_service_url(url)

def englishToFrench(englishText):
    """This Function translates english into french text"""
    translation = instance.translate(text = englishText, model_id='en-fr').get_result()
    translation = translation["translations"][0]["translation"]
    frenchText = json.dumps(translation, indent=2, ensure_ascii=False)
    return frenchText

def frenchToEnglish(frenchText):
    """This function translates french into english text"""
    translation = instance.translate(text = frenchText, model_id='fr-en').get_result()
    translation = translation["translations"][0]["translation"]
    englishText = json.dumps(translation, indent=2, ensure_ascii=False)
    return englishText
