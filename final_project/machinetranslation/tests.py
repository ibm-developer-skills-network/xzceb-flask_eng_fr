import unittest
import json
from translator import english_to_french
from translator import french_to_english

class TestTranslatorMethod(unittest.TestCase):
    def test_englishToFrench(self):
        englishText = 'Hello'
        second = 'Bonjour'
        self.assertEqual(english_to_french(englishText), second, msg='Passed')

    def test_frenchToEnglish(self):
        frenchText = 'Bonjour'
        second = 'Hello'
        self.assertEqual(french_to_english(frenchText), second, msg='Passed')
