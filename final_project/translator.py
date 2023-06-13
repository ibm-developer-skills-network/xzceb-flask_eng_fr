"""Module providing Function Translator."""
from deep_translator import MyMemoryTranslator

def englishToFrench(englishtext):
    """Function for translating from English to French."""
    frenchtext = MyMemoryTranslator(source='en', target='fr').translate(englishtext)
    return frenchtext

def frenchToEnglish(frenchtext):
    """Function for translating from French to English."""
    englishtext = MyMemoryTranslator(source='fr', target='en').translate(frenchtext)
    return englishtext
