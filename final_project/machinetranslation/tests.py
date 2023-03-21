import unittest
from translator import english_to_french, french_to_english
class Test_eng_to_fr(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        #self.assertEqual(english_to_french('Hello'), 'Bonsoir')

class Test_fr_to_eng(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        #self.assertEqual(french_to_english('Bonjour'), 'Bonjour')

unittest.main()
