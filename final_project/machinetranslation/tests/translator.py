from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('xAoRj2_p045si1S_DTCJyVDV8zti1P2ckWojDIvueTz1')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
'https://api.au-syd.language-translator.watson.cloud.ibm.com\
/instances/015f0fd4-fc31-4f43-b697-c7c44b6670f9'
)

def english_to_french(english_text):
    translation = language_translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    translation = language_translator.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()
    english_text = translation['translations'][0]['translation']
    return english_text
    