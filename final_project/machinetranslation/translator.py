# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 11:53:42 2023

@author: claes_z2wsugl
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
lt = LanguageTranslatorV3(version="2018-05-01", authenticator=IAMAuthenticator(apikey))
lt.set_service_url(url)

def englishToFrench(englishText=""):
    """
    Translates english text to french.
    """
    model_id='en-fr'
    try:
        translation = lt.translate(text=englishText, model_id=model_id).get_result()
        return translation['translations'][0]['translation']
    except:
        return ""

def frenchToEnglish(frenchText=""):
    """
    Translates french text to english.
    """
    model_id='fr-en'
    try:
        translation = lt.translate(text=frenchText, model_id=model_id).get_result()
        return translation['translations'][0]['translation']
    except:
        return ""
