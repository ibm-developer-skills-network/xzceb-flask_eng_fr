import unittest
from translator import frenchToEnglish, englishToFrench

"""Testing the method French to English"""
class TestFtoE(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish(),'') 
        self.assertEqual(frenchToEnglish(Bonjour), 'Hello') 
        self.assertNotEqual(frenchToEnglish(Bonjour), 'Helllo')  

"""Testing the method English to French"""            
class TestEtoF(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(),'') 
        self.assertEqual(englishToFrench(Hello), 'Bonjour') 
        self.assertNotEqual(englishToFrench(Hello), 'Bonjouri')
            
unittest.main()