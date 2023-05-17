import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

version = '2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version= version,
    authenticator=authenticator
)

language_translator.set_service_url(url)


def englishToFrench(englishText):
    translation = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    # frenchText = (json.dumps(translation, indent=2, ensure_ascii=False))
    return translation['translations'][0]['translation']


def frenchToEnglish(frenchText):
    translation = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    # englishText = (json.dumps(translation, indent=2, ensure_ascii=False))
    return translation['translations'][0]['translation']

# languages = language_translator.list_identifiable_languages().get_result()
# print(json.dumps(languages, indent=2))