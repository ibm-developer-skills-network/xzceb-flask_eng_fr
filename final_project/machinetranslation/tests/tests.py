import unittest
import json
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_english_to_french_Bonjour(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_english_to_french_au_revoir(self):
        self.assertEqual (french_to_english("Bonjour"), "Hello")

    def test_english_to_french_empty(self):
        self.assertNotEqual(english_to_french(0), "")

    def test_french_to_english_empty(self):
        self.assertNotEqual  (french_to_english(0), "")

if __name__ == '__main__':
    unittest.main() 