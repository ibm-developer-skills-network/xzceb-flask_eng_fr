import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from deep_translator import MyMemoryTranslator

authenticator = IAMAuthenticator("nA_3AG9jCGWTOl-o5nXCoyGkZYNGMZeLhRP_ULwl4RW8")
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
 )
language_translator.set_service_url("https://api.us-south.language-translator.watson.cloud.ibm.com/instances/9ac5757f-278e-448e-99d6-cb25d97fdb66")

def englishToFrench(englishText):
    frenchText = MyMemoryTranslator(source='en', target='fr').translate(englishText)
    print(frenchText)
    return frenchText

def frenchToEnglish(frenchText):
    englishText = MyMemoryTranslator(source='fr', target='en').translate(frenchText)
    print(englishText)
    return englishText