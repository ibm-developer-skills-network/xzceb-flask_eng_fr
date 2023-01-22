import unittest
from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test(self):
        self.assertIsNotNone(english_to_french('Hello'), True)
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


class TestFrenchToEnglish(unittest.TestCase):
    def test(self):
        self.assertIsNotNone(french_to_english('Bonjour'), True)
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


unittest.main()
