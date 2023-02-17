import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']


def english_to_french(english_text):
    french_text= "Bonjour"
    english_text
    return french_text

def french_to_english(french_text):
    english_text= "Hello"
    french_text
    return english_text
