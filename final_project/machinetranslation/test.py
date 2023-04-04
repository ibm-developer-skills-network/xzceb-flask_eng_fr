import unittest
import json
from translator import Translator

class TestTranslator(unittest.TestCase):
    def test_english_to_french_Bonjour(self):
        english_text = "Hello"
        translator = Translator()
        french_text = translator.english_to_french(english_text)
        self.assertEqual(french_text, "Bonjour")

    def test_english_to_french_au_revoir(self):
        english_text = "Goodbye"
        translator = Translator()
        french_text = translator.english_to_french(english_text)
        self.assertNotEqual  (french_text, "Bonjour")

    def test_french_to_english_hello(self):
        french_text = "Bonjour"
        translator = Translator()
        english_text = translator.french_to_english(french_text)
        self.assertEqual(english_text, "Hello")

    def test_french_to_english_goodbye(self):
        french_text = "Au revoir"
        translator = Translator()
        english_text = translator.french_to_english(french_text)
        self.assertNotEqual  (english_text, "Bonjour")

if __name__ == '__main__':
    unittest.main()