import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('NWXxTxbTPDsasr291loUy5_FrI57zp1VMHRrupcl1hi-')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/d4e31325-757d-4f87-a59c-d468f67c81a1')

#translate English to French
def english_to_french(english_text):
    translation = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

#Translate French into English
def french_to_english(french_text):
    translation = language_translator.translate(text=french_text, model_id='fr-en' ).get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
