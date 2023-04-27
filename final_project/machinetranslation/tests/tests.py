import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test2(self):
        self.assertEqual(english_to_french(''), None)


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    def test2(self):
        self.assertEqual(french_to_english(''), None)
    

unittest.main()