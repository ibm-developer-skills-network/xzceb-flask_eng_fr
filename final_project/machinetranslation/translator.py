""" New File """
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

"""Task 1: Create Translator Instance"""
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

#"""Check Available Languages"""
# languages = language_translator.list_languages().get_result()
# print(json.dumps(languages, indent=2))

"""Task 2: Create F to E function"""
def french_to_english(french_text):
    """Let it rip."""
    if french_text is not None:
        english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        f_e=json.dumps(english_text, indent=2, ensure_ascii=False)
        f_e = json.loads(f_e)["translations"]
        english_text= f_e[0]['translation']
        return english_text
   
    return None
        
"""Task 3: Create E to F function"""
def english_to_french(english_text):
    """Let it rip."""
    if english_text is not None:
        french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        e_f=json.dumps(french_text, indent=2, ensure_ascii=False)
        e_f = json.loads(e_f)["translations"]
        french_text = e_f[0]['translation']
        return french_text
    
    return None 

"""Task 5: Check Example"""
print('Bonjour is translated by Watson to', french_to_english('Bonjour'))

"""Task 4: Check Example"""
print('Hello is translated by Watson to', english_to_french('Hello'))
