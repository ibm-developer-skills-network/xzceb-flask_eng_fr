
from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    """Function translate English to French"""
    frenchText = MyMemoryTranslator(source='english', target='french').translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    """Function translate French to English"""
    englishText = MyMemoryTranslator(source='french', target='english').translate(frenchText)
    return englishText