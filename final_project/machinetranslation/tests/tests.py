""" import unittest
from translator import english_to_french, french_to_english
class TestSquare(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertEqual(english_to_french("Neck"),"Cou")
    def test2(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertEqual(french_to_english("Lait"),"Milk")
unittest.main() """