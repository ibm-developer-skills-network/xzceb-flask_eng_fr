import unittest
from translator import french_to_english, english_to_french

class Testfrenchtoenglish(unittest.TestCase):
    def test1(self):
        self.assertIsNotNone(french_to_english, msg=None)
        self.assertEqual(french_to_english("Bonjour"),"Hello")


class Testenglish_to_french(unittest.TestCase):
    def test1(self):
        self.assertIsNotNone(english_to_french, msg=None)
        self.assertEqual(english_to_french("Hello"),"Bonjour")

unittest.main()