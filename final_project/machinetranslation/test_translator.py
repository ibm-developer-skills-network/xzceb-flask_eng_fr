import unittest
from mymodule import square, double
class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Hello"), "Bonjour") 
        
class frenchToEnglish(unittest.TestCase): 
    def test1(self): 
         self.assertEqual(frenchToEnglish("Bonjour"), "Hello") 
        
unittest.main()