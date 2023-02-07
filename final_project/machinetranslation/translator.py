"""
This translates English and French text in both directions
"""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey='80FGiql_VRGQNa21L1FQy67nbWgUqYv2KoyXNkO_ReGd'
url='https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/0c3c6e34-36e6-46f0-b24f-214a52d62f14'

#apikey = os.environ['apikey']
#url = os.environ['url']
VER = '2018-05-01'

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version=VER,
    authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """ 
    This function translates from English to French
    """
    if english_text is not None:
        translation_response = language_translator.translate(
            text=english_text, model_id='en-fr'
        )
        translation = translation_response.get_result()
        french_text = translation['translations'][0]['translation']
        return french_text
    else:
        print('Please enter text to translate')


def french_to_english(french_text):
    """
    This function translates from French to English
    """
    if french_text is not None:
        translation_response = language_translator.translate(
            text=french_text, model_id='fr-en'
        )
        translation = translation_response.get_result()
        english_text = translation['translations'][0]['translation']
        return english_text
    else:
        print('Please enter text to translate')
    