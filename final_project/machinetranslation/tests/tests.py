import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    
    def test_englishToFrench(self):
        # Test translation of "Hello"
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        
        # Test translation of empty string
        self.assertEqual(englishToFrench(""), "")
    
    def test_frenchToEnglish(self):
        # Test translation of "Bonjour"
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        
        # Test translation of empty string
        self.assertEqual(frenchToEnglish(""), "")
        
    def test_englishToFrench_and_frenchToEnglish(self):
        # Test translation consistency between englishToFrench and frenchToEnglish
        english_text = "Hello"
        french_text = englishToFrench(english_text)
        self.assertEqual(frenchToEnglish(french_text), english_text)
        
        french_text = "Bonjour"
        english_text = frenchToEnglish(french_text)
        self.assertEqual(englishToFrench(english_text), french_text)
        
if name == '__main__':
    unittest.main()