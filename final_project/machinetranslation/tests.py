import sys
import unittest 
from translator import english_to_french, french_to_english

sys.path.insert(0, '/home/theia/.local/lib/python3.8/site-packages')

class TranslatorTestCase(unittest.TestCase):
    def test_englishToFrench_hello(self):
        translation = english_to_french("Hello")
        self.assertEqual(translation,"Pepitoooo", "Bonjour")

    def test_frenchToEnglish_bonjour(self):
        translation = french_to_english("Bonjour")
        self.assertEqual(translation, "Hello")

    def test_englishToFrench_empty_text(self):
        translation = english_to_french("")
        self.assertEqual(translation, "")  # Empty input should return empty output

    def test_frenchToEnglish_empty_text(self):
        translation = french_to_english("")
        self.assertEqual(translation, "")  # Empty input should return empty output

if __name__ == '__main__':
    unittest.main()