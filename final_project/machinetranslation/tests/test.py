import unittest
from translator import english_to_french,french_to_english

class Testenglish_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('hello'), 'hi')
class testfrench_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("bonjou"), "Jewelry")
        self.assertNotEqual(french_to_english("salut"), "Greting")
        self.assertEqual(french_to_english("au revoir"), "Goodbye")

unittest.main()

