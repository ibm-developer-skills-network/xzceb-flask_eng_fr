import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey=os.environ['apikey']
url=os.environ['url']

authenticator = IAMAuthenticator('tRS9swzvXPqVSLco9VwZ-3eo9zesZyscb5dHr13AKHLp')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/cc74c187-1f11-421d-8277-ab1aeb5fe0e7')

def english_to_french(english_text):
    #write the code here
    translation= language_translator.translate(text=english_text, model_id="en-fr").get_result()
    french_text=translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    #write the code here
    translation= language_translator.translate(text=french_text, model_id="fr-en").get_result()
    english_text=translation['translations'][0]['translation']
    return english_text