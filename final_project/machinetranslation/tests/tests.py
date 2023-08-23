import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        
        self.assertEqual(english_to_french('hello'), 'Bonjour' )
        with self.assertRaisesRegex(ValueError, 'text must be provided'):
            english_to_french(None)

        
    def test_frenchToEnglish(self):

        self.assertEqual(french_to_english('bonjour'), 'Hello')
        with self.assertRaisesRegex(ValueError, 'text must be provided'):
            french_to_english(None)


if __name__ == '__main__':
    unittest.main()
