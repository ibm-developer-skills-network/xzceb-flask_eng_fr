import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):
        self.assertIsNone(\
            englishToFrench(), "Is none") # test when input is null
        self.assertEqual(\
            englishToFrench("Hello"), "Bonjour") # test when input is Hello

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertIsNone(\
            frenchToEnglish(), "Is none") # test when input is null
        self.assertEqual(\
            frenchToEnglish("Bonjour"), "Hello") # test when input is Bonjour

unittest.main()