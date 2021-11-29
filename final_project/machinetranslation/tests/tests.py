import unittest
from translator import english_to_french, french_to_english

class TestSquare(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(null), null) # test when null is given .
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when eng string is given.



class TestDouble(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(null), null) # test when null is given .
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when french string is given.


unittest.main()
