import unittest
import warnings

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
       self.assertIsNotNone(englishToFrench("HNello"),msg=None)
       self.assertEqual(englishToFrench("hello"), "bonjour") 
       self.assertNotEqual(englishToFrench("hello"), "hello") 
    
class TestFrenchToEnglish(unittest.TestCase):
   def test2(self):
        self.assertIsNotNone(frenchToEnglish("Bonjour"),msg=None)
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Bonjour")


unittest.main()
