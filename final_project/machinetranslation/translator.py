"""
Translator module
"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

# Translate English to French
def englishToFrench(englishText):
    """
    Function converting English to French
    """
    frenchText = language_translator.translate(
        text=englishText, model_id='en-fr').get_result()
    print(json.dumps(frenchText.get("translations")[0].get(
        "translation"), indent=2, ensure_ascii=False))
    return frenchText.get("translations")[0].get("translation")


# Translate French to English
def frenchToEnglish(frenchText):
    """
    Function converting French to English
    """
    englishText = language_translator.translate(
        text=frenchText,model_id='fr-en').get_result()
    print(json.dumps(englishText.get("translations")[0].get(
        "translation"), indent=2, ensure_ascii=False))
    return englishText.get("translations")[0].get("translation")
