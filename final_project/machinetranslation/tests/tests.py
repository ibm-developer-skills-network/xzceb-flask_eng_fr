import unittest
from ..translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_frenchToEnglish_null(self):
        result= french_to_english("")
        self.assertEqual(result,'Please enter text.')
    def test_englishToFrench_null(self):
        result= english_to_french("")
        self.assertEqual(result,'Please enter text.')
  
    def test_frenchToEnglish_hello(self):
        result = french_to_english("Bonjour")
        self.assertEqual(result, "Hello")

    def test_englishToFrench_hello(self):
        result = english_to_french("Hello")
        self.assertEqual(result, "Bonjour")
        
if __name__ == '__main__':
    unittest.main()



