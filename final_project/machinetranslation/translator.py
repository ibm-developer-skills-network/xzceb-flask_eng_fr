"""
translator.py

Este módulo proporciona funciones para traducir texto entre inglés y francés utilizando el paquete deep_translator.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Traductor de inglés a francés
    """
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

#print(english_to_french("hello"))

def french_to_english(french_text):
    """
    Traductor de francés a inglés
    """
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text

#print(french_to_english("bonjour"))
