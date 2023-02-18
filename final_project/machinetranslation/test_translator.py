"""Module providingFunction test."""
import unittest
from machinetranslation.translator import english_to_french, french_to_english
class TestTranslator(unittest.TestCase):
    """Class representing TestTranslator"""
    def test_translate_fr_to_en(self):
        """Function test french to english."""
        self.assertEqual(french_to_english('Bonjour'),'Hello')
    def test_translate_fr_to_en_not_equal(self):
        """Function test french to english is not equal."""
        self.assertNotEqual (french_to_english('Bonjour'),'Bonjour')
    def test_translate_en_to_fr(self):
        """Function test english to french."""
        self.assertEqual (english_to_french('Hello'),'Bonjour')
    def test_translate_en_to_fr_not_equal(self):
        """Function test english to french is not equal."""
        self.assertNotEqual (english_to_french('Hello'),'Hello')
if __name__ == '__main__':
    unittest.main()