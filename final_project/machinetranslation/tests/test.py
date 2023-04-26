import unittest
from translator import french_to_English, english_to_French

"""Testing the method French to English"""
class TestFtoE(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(None),None) 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') 
        self.assertNotEqual(french_to_english('Bonjour'), 'Helllo')  

"""Testing the method English to French"""            
class TestEtoF(unittest.TestCase): 
    def test1(self): 
        #self.assertEqual(englishToFrench(),'') 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') 
        self.assertNotEqual(english_to_french('Hello'), 'Bonjouri')

unittest.main()

