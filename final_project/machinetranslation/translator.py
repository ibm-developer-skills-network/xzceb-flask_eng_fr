import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
translator_instance = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

translator_instance.set_service_url(url)


def english_to_french(english_text):
    """english to french"""
    if english_text and english_text.strip():
        response = translator_instance.translate(
            text=english_text,
            model_id='en-fr'
        ).get_result()
        french_text = response['translations'][0]['translation']
    else:
        return ''
    return french_text


def french_to_english(french_text):
    """french to english"""
    if  french_text and french_text.strip():
        response = translator_instance.translate(
            text=french_text,
            model_id='fr-en'
        ).get_result()
        english_text = response['translations'][0]['translation']
    else:
        return ''
    return english_text
