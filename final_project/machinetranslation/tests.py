import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('None'), ' ')

class TestTranslator(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('None'), ' ')

unittest.main()