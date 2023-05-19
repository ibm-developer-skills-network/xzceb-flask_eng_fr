"""
Translator functionality
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Create instance of IBM Watson Language translator
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)


# Function definitions
def english_to_french(englishtext):
    """
    This function translates the English input to French
    """

    translation = language_translator.translate(
    text=englishtext,
    model_id='en-fr').get_result()

    frenchtext = translation['translations'][0]['translation']
    return frenchtext

def french_to_english(frenchtext):
    """
    This function translates the French input to English
    """

    translation = language_translator.translate(
    text=frenchtext,
    model_id='fr-en').get_result()

    englishtext = translation['translations'][0]['translation']
    return englishtext


# Main translation tests
#print("English hello = ", englishToFrench("hello"))
#print("French adieu = ", frenchToEnglish("adieu"))