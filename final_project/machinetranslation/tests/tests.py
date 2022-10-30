import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase): 
    #test for english to french fonction
    def test1(self): 
        #test for none input
        self.assertEqual(englishToFrench(None), None)
        # test for Hello input
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') 
        
        

class TestfrenchToEnglish(unittest.TestCase): 
    #test for french to english fonction
    def test1(self): 
        #test for none input
        self.assertEqual(englishToFrench(None), None)
        #test for Bonjour input
        self.assertEqual(englishToFrench('Bonjour'), 'Hello') 
        
        
unittest.main()