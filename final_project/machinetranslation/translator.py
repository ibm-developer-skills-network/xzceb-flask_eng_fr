from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    'Is this working?'
    translated = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    print(translated)
    return translated


def french_to_english(french_text):
    'Is this working?'
    translated = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    print(translated)
    return translated
