import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french_with_null_input(self):
        self.assertIsNone(english_to_french(None))

    def test_french_to_english_with_null_input(self):
        self.assertIsNone(french_to_english(None))

    def test_english_to_french_translation(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_french_to_english_translation(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_french_to_english_not_equal(self):
        self.assertNotEqual(french_to_english('Bonjour'), 'Au revoir')

    def test_english_to_french_not_equal(self):
        self.assertNotEqual(english_to_french('Hello'), 'Goodbye')

if __name__ == '__main__':
    unittest.main()