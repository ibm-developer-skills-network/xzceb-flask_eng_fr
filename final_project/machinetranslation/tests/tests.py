import unittest
from translator import english_to_french, french_to_english

class TestSquare(unittest.TestCase): 
    def test_english_to_french1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')  # test when eng string is given.

    def test_english_to_french2(self): 
        self.assertEqual(english_to_french(), null)  # test when eng string is given.

    def test_french_to_english1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')  # test when eng string is given.

    def test_french_to_english2(self): 
        self.assertEqual(french_to_english(), null)  # test when eng string is given.




unittest.main()

