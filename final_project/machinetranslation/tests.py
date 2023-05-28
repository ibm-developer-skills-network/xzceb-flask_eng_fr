import unittest

from translator import english_to_french,french_to_english

class TestEtof(unittest.TestCase):
    def test1(self):
       # self.assertIsNone(english_to_french('Hello'),"null value")
        self.assertEqual(english_to_french('Hello'),'Bonjour')


class TestFtoe(unittest.TestCase):
    def test1(self):
       # self.assertIsNone(french_to_english('Bonjour'),"null value")
        self.assertEqual(french_to_english('Bonjour'),'Hello')


unittest.main()