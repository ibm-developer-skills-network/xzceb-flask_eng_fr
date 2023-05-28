import unittest

from translator import english_to_french,french_to_english

class TestEtof(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french('Hello'),'Hello')
    def test2(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')


class TestFtoe(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english('Bonjour'),'Bonjour')
    def test2(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')


unittest.main()