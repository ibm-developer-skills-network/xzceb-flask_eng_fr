from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Translates English text to French using the MyMemoryTranslator class from the deep_translator package."""
    translator = MyMemoryTranslator(source='en-US', target='fr-FR')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """Translates French text to English using the MyMemoryTranslator class from the deep_translator package."""
    translator = MyMemoryTranslator(source='fr-FR', target='en-US')
    english_text = translator.translate(french_text)
    return english_text

