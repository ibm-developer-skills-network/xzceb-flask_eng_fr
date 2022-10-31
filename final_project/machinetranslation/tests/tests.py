"""module to test the translator module"""
import unittest
from translator import english_to_french
from translator import french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """test for english to french fonction"""
    def test1(self):
        """test for none input"""
        self.assertNotEqual(english_to_french("none"), '')
        #test for Hello input
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    """test for french to english fonction"""
    def test1(self):
        """test for none input"""
        self.assertNotEqual(french_to_english("none"), '')
        #test for Bonjour input
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
