import unittest
from translator import englishToFrench
from translator import frenchToEnglish

class TestTranslatorMethod(unittest.TestCase):
    def test_englishToFrench(self):
        englishText = 'Hello'
        second = 'Bonjour'
        self.assertEqual(englishToFrench(englishText), second, msg='Passed')

    def test_frenchToEnglish(self):
        frenchText = 'Bonjour'
        second = 'Hello'
        self.assertEqual(frenchToEnglish(frenchText), second, msg='Passed')
