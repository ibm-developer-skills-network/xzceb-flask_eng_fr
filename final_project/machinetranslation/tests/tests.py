"""
This module tests the functions from translator.py
"""
from translator import french_to_english, english_to_french
import unittest


class TestFrenchToEnglish(unittest.TestCase):
    """
    This class tests the french_to_english function fron translator.py
    """

    def test1(self):
        """
        This function runs the test for the correct and incorrect
        outputs of the french_to_english function
        """
        self.assertEqual(french_to_english("Bonjour"), "Hi")
        self.assertNotEqual(french_to_english("Ce qui est en place"), "Hello")


class TestEnglishToFrench(unittest.TestCase):
    """
    This class tests the english_to_french function fron translator.py
    """

    def test2(self):
        """
        This function runs the test for the correct and incorrect
        outputs of the english_to_french function
        """
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Hi"), "What's up?")


unittest.main()
