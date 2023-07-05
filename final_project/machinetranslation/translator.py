import json
import os
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    'Is this working?'
    translated = MyMemoryTranslator(source='en-IN', target='fr-FR').translate(english_text)
    print(translated)
    return translated


def french_to_english(french_text):
    'Is this working?'
    translated = MyMemoryTranslator(source='fr-FR', target='en-IN').translate(french_text)
    print(translated)
    return translated
