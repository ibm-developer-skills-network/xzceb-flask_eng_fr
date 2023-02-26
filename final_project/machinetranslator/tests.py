"""Unit tests for translator.py methods"""

import unittest

from translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):
    """TestCase for translator.py unit tests"""
    def test_english_to_french(self):
        """Tests whether English translator works correctly on basic words"""
        self.assertEqual(english_to_french('dog').lower(), 'chien')
        self.assertNotEqual(english_to_french('dog').lower(), 'dog')


    def test_french_to_english(self):
        """Tests whether French translator works correctly on basic words"""
        self.assertEqual(french_to_english('chien').lower(), 'dog')
        self.assertNotEqual(french_to_english('chien').lower(), 'chien')


if __name__ == '__main__':
    unittest.main()
