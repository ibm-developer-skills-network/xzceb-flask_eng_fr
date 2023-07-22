"""
This module translate french and english strings
"""
from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """
    Translates an english string to french
    """
    french_text = MyMemoryTranslator(source="en-US", target="fr-FR").translate(
        english_text
    )
    return french_text


def french_to_english(french_text):
    """
    Translates a french string into english
    """
    english_text = MyMemoryTranslator(source="fr-FR", target="en-US").translate(
        french_text
    )
    return english_text
