"""Unit test functions French to English."""
import unittest
from translator import french_to_english, english_to_french

class testFrenchToEnglish(unittest.TestCase):
    def test_translation(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(french_to_english("War"),"Guerre")

    def test_null(self):
        self.assertEqual(french_to_english(""),"")

class testEnglishToFrench(unittest.TestCase):
    def test_translation(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertNotEqual(english_to_french("Guerre"),"War")

    def test_null(self):
        self.assertEqual(english_to_french(""),"")

if __name__ == '__main__':
    unittest.main()