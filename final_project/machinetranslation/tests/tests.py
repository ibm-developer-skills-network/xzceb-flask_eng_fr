''' This program tests translator.py'''
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """Translate a string from English to French"""
    def test1(self):
        """Test a Null String and translating Hello to Bonjour"""
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    """Translate a string from French to English"""
    def test1(self):
        """Test a Null String and translating Bonjour to Hello"""
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
