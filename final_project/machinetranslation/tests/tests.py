import unittest
import warnings

from translator import english_to_french, french_to_english


warnings.filterwarnings("ignore")


class test_english_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertIsNotNone(english_to_french("HNello"),msg=None)
        self.assertEqual(english_to_french("Hello"), "Bonjour") 
        self.assertNotEqual(english_to_french("Hello"), "Hello") 
       

class test_french_to_english(unittest.TestCase):
    def test1(self):
        self.assertIsNotNone(french_to_english("Bonjour"),msg=None)
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")

unittest.main()