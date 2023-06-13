"""
Defines functions to translate from e2f and f2e
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates english text to french
    """
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translates french text to english
    """
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
