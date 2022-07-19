import unittest
from translator import english_french, french_english
class TestTranslator(unittest.TestCase):
    def test_english_french(self):
        
        self.assertEqual(english_french("Hello"), "Bonjour")
    
    def test_french_english(self):
        
        self.assertEqual(french_english("Bonjour"),"Hello")

if __name__=='__main__':
    unittest.main()
    