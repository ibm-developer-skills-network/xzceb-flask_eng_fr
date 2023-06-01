import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = 'LoEvljIma5xFK405J-FFVlxIsFNiqbMETjSl8bdLLcyh'
url = 'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/9057d64a-3e76-4e18-83e8-78b6ae4bd172'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)


def englishToFrench(englishText):
    translation_response = language_translator.translate(
        text=englishText,
        source='en',
        target='fr'
    )
    translation = translation_response.get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    translation_response = language_translator.translate(
        text=frenchText,
        source='fr',
        target='en'
    )
    translation = translation_response.get_result()
    englishText = translation['translations'][0]['translation']
    return englishText

