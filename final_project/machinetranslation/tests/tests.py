import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(' '), ' ') # test for null input for english_to_french
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test for the translation of the english word
        self.assertNotEqual(english_to_french('Hello'), 'Hello') # test for the translation of the english word
        

class TestF2E(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english(' '), ' ') # test for null input for french_to_english
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test for the translation of the french word
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour') # test for the translation of the french word


unittest.main()
