"""tester for translator"""
import unittest
from translator import english_to_french, french_to_english

class TranslatorTestEnglish(unittest.TestCase):
    """tests to see if the English translates"""
    def test_english_to_french_equal(self):
        """tests if the english translates to french"""
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test_english_to_french_not_equal(self):
        """tests to make sure the english is translated"""
        self.assertNotEqual(english_to_french("Hello"), "Hello")

class TranslatorTestFrench(unittest.TestCase):
    """tests to see if the french translates"""
    def test_french_to_english_equal(self):
        """tests if the french translates to english"""
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    def test_french_to_english_not_equal(self):
        """tests to make sure the french is translated"""
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")

if __name__ == '__main__':
    unittest.main()
