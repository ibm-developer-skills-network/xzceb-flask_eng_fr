import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

def englishToFrench(englishText):
    #write the code here
    language_translator.set_service_url(url)
    result = language_translator.translate(
        text = englishText,
        model_id = 'en-fr').get_result()
    result = json.dumps(result["translations"][0]["translation"])
    frenchText = result[1:-1]
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    language_translator.set_service_url(url)
    result = language_translator.translate(
        text = frenchText,
        model_id = 'fr-en').get_result()
    result = json.dumps(result["translations"][0]["translation"])
    englishText = result[1:-1]
    return englishText
