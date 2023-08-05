import unittest
from translator import *

class TranslationTest(unittest.TestCase):

    def test_englishToFrench(self):
        english_text = "Hello"
        expected_result = "Bonjour"
        french_text=english_to_french(english_text)
        self.assertEqual(french_text, expected_result)

    def french_to_english(self):
        french_text = "Bonjour"
        expected_result = "Hello"
        english_text=frenchToEnglish(french_text)
        self.assertEqual(english_text, expected_result)

if __name__ == '__main__':
    unittest.main()
