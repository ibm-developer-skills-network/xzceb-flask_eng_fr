''' Import the MyMemoryTranslator from deep_translator'''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    ''' This function converts english text to french'''
    french_text = MyMemoryTranslator(source="en",
    target="fr").translate(text=english_text)
    return french_text

def french_to_english(french_text):
    ''' This function converts text from french to english'''
    english_text = MyMemoryTranslator(source="fr",
    target="en").translate(text=french_text)
    return english_text
