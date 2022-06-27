import unittest
from machinetranslation import translator
class Test_E2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertEqual(english_to_french(" ")," ")
    

class Test_F2E(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english(" ")," ")
        self.assertEqual(french_to_english("Bonjour"),"Hello")

unittest.main()