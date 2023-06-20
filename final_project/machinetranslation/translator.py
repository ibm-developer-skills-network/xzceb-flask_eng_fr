"""
    This module implements translation function
"""

from deep_translator import MyMemoryTranslator


def englishToFrench(english_text):
    """Function translates text from english to french

    Args:
        englishText ( String ): English text

    Returns:
        String: French text
    """
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text


def frenchToEnglish(french_text):
    """Function translates text from french to english

    Args:
        englishText ( String ): French text

    Returns:
        String: English text
    """
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
    