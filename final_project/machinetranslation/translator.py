import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

''' Translator instance '''

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version="2023-05-15",
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    ''' Translation function: English to French '''
    try:
        french_text = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
    except Exception as err:
        return f"Error during translation: {err}"

    return french_text.get("translations")[0].get("translation")

def french_to_english(french_text):
    ''' Translation function: French to English '''
    try:
        english_text = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
    except Exception as err:
        return f"Error during translation: {err}"

    return english_text.get("translations")[0].get("translation")
