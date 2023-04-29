# Import 
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

# Read environment variables
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

# Create instance of IBM Watson Language Translator 
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com')

# English to French function
def englishToFrench(englishText):
    ''' 
    This function takes a string in english and returns a string in french using 
    the IBM Watson Language Translator API
    '''
   
    translation = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    
    frenchText = translation['translations'][0]['translation']
    return frenchText


# French to English Function
def frenchToEnglish(FrenchText):
    ''' 
    This function takes a string in french and returns a string in english using 
    the IBM Watson Language Translator API
    '''

    translation = language_translator.translate(
    text=FrenchText,
    model_id='fr-en').get_result()

    englishText  = translation['translations'][0]['translation']

    return englishText
