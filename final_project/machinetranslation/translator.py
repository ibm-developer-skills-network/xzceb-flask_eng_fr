""" New File """
```py
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
```
"""Task 1: Create Translator Instance"""
authenticator = IAMAuthenticator('{apikey}')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('{url}')

"""Task 2: Create E to F function"""
def englishToFrench(englishText):
    frenchText = language_translator.translate(
    text=englishText,
    model_id='en-es').get_result()
    print(json.dumps(frenchText, indent=2, ensure_ascii=False))

    return frenchText


"""Task 2: Create F to E function"""
def englishToFrench(frenchText):
    englishText = language_translator.translate(
    text=frenchText,
    model_id='en-es').get_result()
    print(json.dumps(englishText, indent=2, ensure_ascii=False))

    return englishText
    
