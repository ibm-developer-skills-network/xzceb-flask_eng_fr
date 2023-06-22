import unittest
from translator import english_to_french, french_to_english

class englishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Lust"), "Aimer")

class frenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Aimer"), "Lust")

unittest.main()