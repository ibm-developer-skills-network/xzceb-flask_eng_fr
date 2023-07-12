""" Provide the module to translate text """
from deep_translator import MyMemoryTranslator


def englishtofrench(englishtext):
    """ Translate English text to French """
    frenchtext = MyMemoryTranslator(source='en-US', target='fr-FR').translate(englishtext)
    return frenchtext


def frenchtoenglish(frenchtext):
    """ Translate French text to English """
    englishtext = MyMemoryTranslator(source='fr-FR', target='en-US').translate(frenchtext)
    return englishtext
