import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Null'), 'Null') 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when Hello is given as input the output is Bonjour.
  


class TestFrenchToEnglish(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(french_to_english('Null'), 'Null')
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when Bonjour is given as input the output is Hello.
       

unittest.main()