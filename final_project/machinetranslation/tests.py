import unittest

from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('bye'), 'bye')

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('au revoir'), 'au revoir')

if __name__ == "__main__":
    unittest.main()