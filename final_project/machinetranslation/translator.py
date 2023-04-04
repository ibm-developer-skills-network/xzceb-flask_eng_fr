"""
IBM Watson Language Translator Module
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['API_KEY']
API_SERVICE_URL = os.environ['API_SERVICE_URL']

class Translator:
  def __init__(self):
    self._initIAMAuthenticator()

  def _initIAMAuthenticator(self):
    authenticator = IAMAuthenticator(API_KEY)
    self.language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    self.language_translator.set_service_url(API_SERVICE_URL)

  def translate(self, text, model_id):
    translation = self.language_translator.translate(
        text=text,
        model_id=model_id).get_result()

    return translation["translations"][0]["translation"]

  def english_to_french(self, text='Hello'):
    """
    Translates English text to French
    """
    return self.translate(text, 'en-fr')

  def french_to_english(self, text='Bonjour'):
    """
    Translates French text to English
    """
    return self.translate(text, 'fr-en')
