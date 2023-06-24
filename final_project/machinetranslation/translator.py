''' this code for building translator '''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    ''' This function takes an english text and translates it to french '''
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    ''' This function takes a french text and translates it to english '''
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
