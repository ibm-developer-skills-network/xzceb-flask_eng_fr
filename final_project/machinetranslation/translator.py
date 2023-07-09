from deep_translator import MyMemoryTranslator

def englishtofrench(englishtext):
    '''convert text from english to french'''
    frenchtext = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(englishtext)
    print(frenchtext)
    return frenchtext

def frenchtoenglish(frenchtext):
    '''convert text from french to english'''
    englishtext = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(frenchtext)
    print(englishtext)
    return englishtext
