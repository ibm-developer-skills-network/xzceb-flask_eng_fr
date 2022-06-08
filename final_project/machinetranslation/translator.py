import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
auth = IAMAuthenticator(apikey)

translator = LanguageTranslatorV3(authenticators=auth)
translator.set_service_url(url)


def englishToFrench(englishText):
    text = translator.translate(
        englishText,
        model_id='en-fr'
    ).get_result()
    frenchText = json.dumps(text)
    return frenchText


def frenchToEnglish(frenchText):
    text = translator.translate(
        frenchText,
        model_id='fr-en'
    ).get_result()
    englishText = json.dumps(text)
    return englishText
