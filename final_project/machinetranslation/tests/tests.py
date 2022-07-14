import unittest

from translator import english_to_french, french_to_english

class TestEnglishtoFrench (unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour') #Test to see if Hello is translated to Bonjour
        self.assertEqual(english_to_french(), ) #Test when null input is given

class TestFrenchtoEnglish (unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello') #Test if Bonjour is translated too Hello
        self.assertEqual(french_to_english (), ) #Test null value

unittest.main()