 from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    translator = MyMemoryTranslator(source='en', target='fr')
    frenchText = translator.translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    translator = MyMemoryTranslator(source='fr', target='en')
    englishText = translator.translate(frenchText)
    return englishText