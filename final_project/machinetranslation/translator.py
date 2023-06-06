"""
Defines functions to translate from e2f and f2e
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates english text to french
    """
    translated = MyMemoryTranslator(source='english', target='french')
    french_text = translated.translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translates french text to english
    """
    translated = MyMemoryTranslator(source='french', target='english')
    english_text = translated.translate(french_text)
    return english_text
