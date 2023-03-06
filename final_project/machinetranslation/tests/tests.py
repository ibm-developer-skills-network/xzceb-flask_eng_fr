import unittest
from translator import english_to_french, french_to_english

class TestTranslate(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test2(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
unittest.main()