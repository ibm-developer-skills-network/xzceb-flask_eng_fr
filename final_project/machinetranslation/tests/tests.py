import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase): 
    def test_e2f(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')
        self.assertEqual(english_to_french(None), None)
                
class TestF2E(unittest.TestCase): 
    def test_f2e(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
        self.assertEqual(french_to_english(None), None)

unittest.main()