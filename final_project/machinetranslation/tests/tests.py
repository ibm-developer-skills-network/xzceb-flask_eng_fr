import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        english_text = 'Hello'
        french_text = english_to_french(english_text)
        self.assertIsNotNone(french_text)
        self.assertNotEqual(french_text, english_text)

    def test_french_to_english(self):
        french_text = 'Bonjour'
        english_text = french_to_english(french_text)
        self.assertIsNotNone(english_text)
        self.assertNotEqual(english_text, french_text)

if __name__ == '__main__':
    unittest.main()
