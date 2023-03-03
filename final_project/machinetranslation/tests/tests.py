import unittest

from translator import english_to_french, french_to_english

"""
Here are the tests for the translation
"""
class TestTheTranslator(unittest.TestCase):
    
    def test_englishToFrench(self):
        #This tests from english to french
        self.assertEqual(english_to_french("This shirt is pretty"), "Cette chemise est jolie")
        self.assertEqual(english_to_french("My name is Tal"), "Mon nom est Tal")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertIsNone(english_to_french(None))

    def test_frenchToEnglish(self):
        #This tests from french to english
        self.assertEqual(french_to_english("Cette chemise est jolie"), "This shirt is pretty")
        self.assertEqual(french_to_english("Mon nom est Tal"), "My name is Tal")
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertIsNone(french_to_english(None))
        
if __name__ == '__main__':
    unittest.main()