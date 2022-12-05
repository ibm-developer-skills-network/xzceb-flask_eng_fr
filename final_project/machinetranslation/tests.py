import unittest
from translator import english_to_french
from translator import french_to_english

class TestEnglish(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour') #test the translation for a Hello input
        self.assertEqual(english_to_french(' '),' ') #Test for nule input
class TestFrench(unittest.TestCase):
    def test_f2e(self):
        self.assertEqual(french_to_english(' '),' ') #Test for null input
        self.assertEqual(french_to_english('Bonjour'), 'Hello') #Test the translation for a Bonjour input
unittest.main()