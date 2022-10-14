"""
english to french to english translation using IBM watson
"""
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

def englishToFrench(english_text):
    """
    translate from english to French
    """
    if len(english_text)==0:
        return None #null
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return french_text['translations'][0]['translation']

def frenchToEnglish(french_text):
    """
    translate from French to  english
    """
    if len(french_text)==0:
        return None
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return english_text['translations'][0]['translation']
