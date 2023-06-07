import unittest

from translator import english_to_french, french_to_english

class TestEnglishtoFrench (unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour') #Test to see if Hello is translated to Bonjour
        self.assertNotEqual(english_to_french('Hello'),'Hello' ) #Test when null input is given

class TestFrenchtoEnglish (unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello') #Test if Bonjour is translated too Hello
        self.assertNotEqual(french_to_english('Bonjour'),'Bonjour' ) #Test if not translating

unittest.main()