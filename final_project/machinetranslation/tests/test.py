import unittest

from translator import english_to_french, french_to_english


class TestenglishToFrench(unittest.TestCase):
    """
    a class for testing text converstion
    """

    def test(self):
        """
        test the convertion of enlgish text to french text
        """
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french(""), "")


class TestfrenchToEnglish(unittest.TestCase):

    """
    a class for testing text converstion
    """

    def test(self):
        """
        test the convertion of french text to english text
        """
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english(""), "")


unittest.main()
