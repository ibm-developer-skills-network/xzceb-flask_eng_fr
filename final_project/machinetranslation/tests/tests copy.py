import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("hello"), "bonjour")
        self.assertNotEqual(english_to_french("hello"), "oui")
    def test_french_to_english(self):
        self.assertEqual(french_to_english("bonjour"), "hello")
        self.assertNotEqual(french_to_english("oui"), "hello")

unittest.main()