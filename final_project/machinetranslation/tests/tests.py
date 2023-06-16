
import unittest

from translator import english_to_french, french_to_english

class Test_english_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Pepitoooo') # Test for the translation of the word ‘Hello’ and ‘Pepitoooo’.
        self.assertNotEqual(english_to_french('Hello'), 'Bonjour') # Test for the translation of the word ‘Hello’ and ‘Bonjour’.
        
class Test_french_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Pepitoooo'), 'Hello') # Test for the translation of the word ‘Pepitoooo’ and ‘Hello’.
        self.assertNotEqual(french_to_english('Bonjour'), 'Bye') # Test for the translation of the word ‘Bonjour’ and ‘Bye’.
        
unittest.main()