import unittest
from translator import englishtofrench, frenchtoenglish

class TranslationTests(unittest.TestCase):
    def test_french_to_english(self):
        french_text = "Bonjour"
        expected_translation = "Hello"
        translated_text = frenchtoenglish(french_text)
        self.assertEqual(translated_text, expected_translation)
    def test_french_to_english_not_equal(self):
        french_text = "Bonjour"
        unexpected_translation = "Hi"
        translated_text = frenchtoenglish(french_text)
        self.assertNotEqual(translated_text, unexpected_translation)
    
    def test_english_to_french(self):
        english_text = "Hello"
        expected_translation = "Pepitoooo"
        translated_text = englishtofrench(english_text)
        self.assertEqual(translated_text, expected_translation)
    
    def test_english_to_french_not_equal(self):
        english_text = "Hello"
        unexpected_translation = "Salut"
        translated_text = englishtofrench(english_text)
        self.assertNotEqual(translated_text, unexpected_translation)

if __name__ == '__main__':
    unittest.main()