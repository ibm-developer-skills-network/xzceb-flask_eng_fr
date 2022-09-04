import unittest
from translator import english_to_french
from translator import french_to_english

class TextMyModule(unittest.TestCase):
    def test_f2e_null(self):
        self.assertEqual(french_to_english(' '), ' ')
    
    def test_e2f_null(self):
        self.assertEqual(english_to_french(' '), ' ')

    def test_f2e_hello(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_e2f_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_f2e_zero(self):
        self.assertEqual(french_to_english('0'), '0')
    
    def test_e2f_zero(self):
        self.assertEqual(english_to_french('0'), '0')

unittest.main()