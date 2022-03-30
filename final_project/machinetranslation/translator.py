"""
Greg's Final Project for IBM Python Project for AI & Application Development
MARCH 2022
"""
#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_watson import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#print("Start of App")

#Instantiate the IBM Translator API for use in this module
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Simple function to translate English to French using IBM Watson Cloud Language Translator API
    english_text must be a str
    """
    if isinstance(english_text,str) is False:
        english_text=""

    #If text is empty, nothing to translate so exit!
    if english_text=="":
        return ""

    try:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()

        french_text=translation["translations"][0]["translation"]
    except ApiException as ex:
        print("Method failed with status code " +
        str(ex.code)+ ": " + ex.message)
        french_text=""
    return french_text

def french_to_english(french_text):
    """
    Simple function to translate French to English using IBM Watson Cloud Language Translator API
    frenchText must be a str
    """
    if isinstance(french_text,str) is False:
        french_text=""

    #If text is empty, nothing to translate so exit!
    if french_text=="":
        return ""

    try:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()

        english_text=translation["translations"][0]["translation"]
    except ApiException as ex:
        print("Method failed with status code " +
        str(ex.code)+ ": " + ex.message)
        english_text=""
    return english_text

#Basics to see if it's working correctlyD
#ENG_TEST = "Hello, how are you today?"
#FR_TEST = "Je ne sais quoi"
#print(ENG_TEST, english_to_french(ENG_TEST))
#print(FR_TEST, french_to_english(FR_TEST))
