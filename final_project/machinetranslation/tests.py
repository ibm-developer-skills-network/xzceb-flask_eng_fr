""" Module Test functionality Null and 
Translation English to French and French to English. """
__import__(name:machinetranslation)
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """ Class to test English to French. """
    def test1(self):
        """Function test error when Null and translate Hello to Bonjour. """
        self.assertEqual(english_to_french(''),
        'Error null string') # null input for englishToFrench.
        self.assertEqual(english_to_french('Hello'),
        'Bonjour')  # Test for the translation of the world Hello and Bonjour.

class TestFrenchToEnglish(unittest.TestCase):
    """ Class to test French to English. """
    def test1(self):
        """Function test error when Null and translate Bonjour to Hello. """
        self.assertEqual(french_to_english(''),
        'Error null string') # null input for frenchToEnglish.
        self.assertEqual(french_to_english('Bonjour'),
        'Hello') # Test for the translation of the world Bonjour and Hello.

unittest.main()
