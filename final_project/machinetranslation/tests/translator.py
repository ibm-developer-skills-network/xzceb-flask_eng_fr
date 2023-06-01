#importing required modules
import os
from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3


load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]

# code to create an instance of the IBM Watson Language translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version="2018-05-01", authenticator=authenticator
)
language_translator.set_service_url(url)


def english_to_french(english_text):
    """translate english to french"""
    translation = language_translator.translate(
        text=english_text, model_id="en-fr"
    ).get_result()
    french_text = translation["translations"][0]["translation"]
    return french_text


def french_to_english(french_text):
    """translate french to english"""
    translation = language_translator.translate(
        text=french_text, model_id="fr-en"
    ).get_result()
    english_text = translation["translations"][0]["translation"]
    return english_text
