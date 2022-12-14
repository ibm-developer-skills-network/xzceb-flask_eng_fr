import unittest

from translator import englishToFrench, frenchToEnglish

class Test_EnglishToFrench(unittest.TestCase): 
    def test_English_to_French(self): 
        self.assertEqual(englishToFrench(""), "") # test for null input.
        self.assertEqual(englishToFrench("Hello"), "Bonjour")  # test for translation of Hello to Bonjour.
        

class Test_FrenchToEnglish(unittest.TestCase): 
    def test_French_to_English(self): 
        self.assertEqual(frenchToEnglish(""), "") # test for null input.
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello") # test for translation of Bonjour to Hello.
        
unittest.main()