import unittest

from translator import frenchToEnglish, englishToFrench

class TestFrenchToEnglish(unittest.TestCase): 
    """
    TestFrenchToEnglish
    """
    def test1(self): 
        self.assertEqual(frenchToEnglish(""),"") # test when 2 is given as input the output is 4.
    def test2(self): 
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello") # test when 2 is given as input the output is 4.
      
        
class TestEnglishToFrench(unittest.TestCase): 
    """
    TestEnglishToFrench
    """
    def test1(self): 
        self.assertEqual(englishToFrench(""),"") # test when 2 is given as input the output is 4.
    def test2(self): 
        self.assertEqual(englishToFrench("Hello"),"Bonjour") # test when 2 is given as input the output is 4.
      
       
unittest.main()