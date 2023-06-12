import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("hello"), "bonjour") # Translate Hello to French
        self.assertNotEqual(english_to_french('Pain'), 'Pain') # 
        
class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("bonjour"), "hello") # And vice versa
        self.assertNotEqual(french_to_english('Pain'), 'Pain') # 

unittest.main()
