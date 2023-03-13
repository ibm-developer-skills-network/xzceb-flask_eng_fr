import unittest
from machinetranslation.translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    """Test cases for english_to_french"""

    def test_E2F_null(self):
        """Test for null input for english_to_french"""
        self.assertEqual(english_to_french(' '), ' ')

    def test_E2F_translation(self):
        """Test for the translation of the english word"""
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_E2F_not_translation(self):
        """Test for the not translation of the english word"""
        self.assertNotEqual(english_to_french('Hello'), 'Hello')        


class TestF2E(unittest.TestCase):
    """Test cases for french_to_english"""

    def test_F2E_null(self):
        """Test for null input for french_to_english"""
        self.assertEqual(french_to_english(' '), ' ')
    
    def test_F2E_translation(self):
        """Test for the translation of the french word"""
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    
    def test_F2E_not_translation(self):
        """Test for the not translation of the french word"""
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')

unittest.main()
