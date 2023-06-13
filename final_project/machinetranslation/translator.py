from deep_translator import MyMemoryTranslator
"""two language translation"""

def english_to_french(english_text):
    """write the code here"""
    french_text = MyMemoryTranslator(source = 'en', target='fr').translate(english_text)
    print(french_text)
    return french_text

def french_to_english(french_text):
    """write the code here"""
    english_text = MyMemoryTranslator(source = 'fr', target='en').translate(french_text)
    print(english_text)
    return english_text
