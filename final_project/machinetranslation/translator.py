"""translates between english and french"""

from deep_translator import MyMemoryTranslator

#english_text = "Hello"
#french_text = "Bonjour"


def english_to_french(english_text):
    """translates from english to french"""
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text


def french_to_english(french_text):
    """translates from french to english"""
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
