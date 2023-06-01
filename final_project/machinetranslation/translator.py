#write the code here
"""Module providingFunction printing python version."""
#write the code here
import os
#write the code here
from ibm_watson import LanguageTranslatorV3
#write the code here
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#write the code here
from dotenv import load_dotenv

#write the code here
load_dotenv()

#write the code here
apikey = os.environ['apikey']
url = os.environ['url']
VERSION_LT='2018-05-01'

#write the code here
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=VERSION_LT,authenticator=authenticator)
language_translator.set_service_url(url)


def english_to_french(english_text):
    #write the code here
    """Module providingFunction printing python version."""
    french_text = language_translator.translate(text = english_text, model_id='en-fr').get_result()
    return french_text

def french_to_english(french_text):
    #write the code here
    """Module providingFunction printing python version."""
    english_text = language_translator.translate(text = french_text, model_id='fr-en').get_result()
    return english_text
