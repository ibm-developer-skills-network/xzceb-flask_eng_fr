import unittest
import json
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french_Bonjour(self):
        english_text = "Hello"
        french_text = english_to_french(english_text)
        self.assertEqual(french_text, "Bonjour")

    def test_french_to_english_hello(self):
        french_text = "Bonjour"
        english_text = french_to_english(french_text)
        self.assertEqual(english_text, "Hello")

    def test_english_to_french_au_revoir(self):
        english_text = "Goodbye"
        french_text = english_to_french(english_text)
        self.assertEqual(french_text, "Au revoir")

    def test_french_to_english_goodbye(self):
        french_text = "Au revoir"
        english_text = french_to_english(french_text)
        self.assertEqual(english_text, "Goodbye")

if __name__ == '__main__':
    unittest.main()
