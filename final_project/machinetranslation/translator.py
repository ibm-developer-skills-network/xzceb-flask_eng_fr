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


def english_to_french(englishtext):
    """
    Translates English text to French.
    """
    if englishtext is None:
        return None
    translation_response = language_translator.translate(
        text=englishtext,
        source='en',
        target='fr'
    )
    return translation_response.get_result()['translations'][0]['translation']

def french_to_english(frenchtext):
    """
    Translates French text to English.
    """
    if frenchtext is None:
        return None
    translation_response = language_translator.translate(
        text=frenchtext,
        source='fr',
        target='en'
    )
    return translation_response.get_result()['translations'][0]['translation']