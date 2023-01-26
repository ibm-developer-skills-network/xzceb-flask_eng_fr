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
    authenticator = authenticator
)

language_translator.set_service_url(url)

 # translate from english to french
def english_to_french(english_text):
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = translation.get("translations")[0].get("translation")
    return french_text

# translate from french to english
def french_to_english(french_text):
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = translation.get("translations")[0].get("translation")
    return english_text
