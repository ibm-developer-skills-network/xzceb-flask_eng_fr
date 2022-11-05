"""
import os and api
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('vBku_sByItbcW_AQrUokyHif4S9CsHPpJfRM280fuvIy')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/4e439162-f58a-43bb-a112-eaed72603a0d')

def english_to_french(english_text):
# write code here
    """
    translate eng to fr
    """
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text=translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
# write code here
    """
    translate fr to eng
    """
    translation_new = language_translator.translate(text=french_text, model_id='fr-en').get_result()
    english_text=translation_new['translations'][0]['translation']
    return english_text
