import unittest
from translator import english_to_french, french_to_english

class TestFrToEng(unittest.TestCase):

    def test1(self):
        
        self.assertEqual(french_to_english(""), "")
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bonjour"),"Bonjour")

class TestEngToFr(unittest.TestCase):

    def test1(self):
        
        self.assertEqual(english_to_french(""),"")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Hello"), "Hello")

unittest.main()