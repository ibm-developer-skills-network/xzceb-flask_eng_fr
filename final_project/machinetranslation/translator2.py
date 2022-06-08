''' Translator '''
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#Create instance
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

''' Translate from English to French '''
french_text = language_translator.translate(
                     text = "Hello",
                     model_id = 'en-fr').get_result()
print(french_text['translations'][0]['translation'])

