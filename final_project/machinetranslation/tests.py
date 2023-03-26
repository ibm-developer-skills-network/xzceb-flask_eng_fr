import unittest
from translator import english_To_French, french_To_English

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_To_French("hello"),"Bonjour")
        self.assertEqual(english_To_French("welcome"),"Bienvenue")
        self.assertEqual(english_To_French("love"),"Amour")

class TestFrenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_To_English("bonjour"),"Hello")
        self.assertEqual(french_To_English("bienvenue"),"Welcome")
        self.assertEqual(french_To_English("amour"),"Love")

unittest.main()