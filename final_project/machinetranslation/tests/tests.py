import unittest
from translator import english_to_french, french_to_english

class EnglishTest(unittest.TestCase):    
    def test1(self):        
        self.assertIsNone(english_to_french(None), None)
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Hello"), "Hello")


class FrenchTest(unittest.TestCase):    
    def test2(self):        
        self.assertIsNone(french_to_english(None), None)
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")

unittest.main()