from translator import french_to_english, english_to_french
import unittest

class TestTranslator(unittest.TestCase):
    def test_french_to_english_null_input(self):
        self.assertIsNone(french_to_english(None))

    def test_english_to_french_null_input(self):
        self.assertIsNone(english_to_french(None))

    def test_french_to_english_hello(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_english_to_french_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_french_to_english_bonjour(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_english_to_french_bonjour(self):
        self.assertEqual(english_to_french('Bonjour'), 'Hello')

