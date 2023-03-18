import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(english_to_french(""),"")
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertNotEqual(english_to_french("Thanks"),"Au Revoir")

    def test_french_to_english(self):
        self.assertEqual(french_to_english(""),"")
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(english_to_french("Au Revoir"),"Thanks")

unittest.main()