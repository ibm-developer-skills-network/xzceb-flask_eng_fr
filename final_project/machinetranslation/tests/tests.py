import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslation(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("How are you?"),"Comment es-tu?")

    def test_englishToFrenchIsNull(self):
        self.assertIsNone(englishToFrench(""), "Text is null")
    
    def test_englishToFrench_Hello(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
      

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish("Comment es-tu?"),"How are you?")
    
    def test_test_frenchToEnglishIsNull(self):
        self.assertIsNone(frenchToEnglish(""), "Text is null")

    def test_test_frenchToEnglish_Bonjour(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")


if __name__ == '__main__':
    unittest.main()