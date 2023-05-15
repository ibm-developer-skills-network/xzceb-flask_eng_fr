import unittest
from translator import english_to_french, french_to_english

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(None), 'Error during translation: text must be provided')
    def test2(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")


class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(None), 'Error during translation: text must be provided')
    def test2(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

unittest.main()