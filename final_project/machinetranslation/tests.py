import unittest
from translator import english_to_french, french_to_english


class TestTranslateFunctions(unittest.TestCase):
    def test_nul(self):
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(french_to_english(None), None)


    def test_space(self):
        self.assertEqual(english_to_french(' '), ' ')
        self.assertEqual(french_to_english(' '), ' ')


    def test_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(french_to_english('Bonjour'),'Hello' )

if __name__ == '__main__':
    unittest.main()