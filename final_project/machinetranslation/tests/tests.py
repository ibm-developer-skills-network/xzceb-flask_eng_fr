import unittest
from translator import english_to_french, french_to_english


class TranslationTests(unittest.TestCase):
    def test1(self):
        # Test translation of 'Hello' to French
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Goodbye'), 'Au revoir')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')


    def test1(self):
        # Test translation of 'Bonjour' to English
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Au revoir'), 'Goodbye')
        self.assertNotEqual(french_to_english('Bonjour'), 'Goodnight')

if __name__ == '__main__':
    unittest.main()
    
