import os
import json
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

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
    translation = language_translator.translate(
        text = englishtext,
        model_id='en-fr').get_result()
    text1 = json.dumps(translation, indent=2, ensure_ascii=False)
    json_object = json.loads(text1)
    text2 = json_object["translations"]
    for i in text2:
        for text in i:
            frenchtext = i[text]
    return frenchtext

def french_to_english(frenchtext):
    translation = language_translator.translate(
        text = frenchtext,
        model_id='fr-en').get_result()
    text1 = json.dumps(translation, indent=2, ensure_ascii=False)
    json_object = json.loads(text1)
    text2 = json_object["translations"]
    for i in text2:
        for text in i:
            englishtext = i[text]
    return englishtext
