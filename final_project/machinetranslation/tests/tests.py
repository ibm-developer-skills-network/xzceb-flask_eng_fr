import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_eng_to_fr(self):
        self.assertNotEqual(english_to_french("None"), '') # test for null input
        self.assertNotEqual(english_to_french(0), 0) # test empy returns empty
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test for 'Hello' = 'Bonjour'

    def test_fr_to_eng(self):
        self.assertNotEqual(french_to_english("None"), '') # test for null input
        self.assertNotEqual(french_to_english(0), 0) # test empty returns empty
        self.assertEqual(french_to_english("Bonjour"), "Hello") # test for 'Bonjour' = 'Hello'

if __name__== "__main__":
    unittest.main()
