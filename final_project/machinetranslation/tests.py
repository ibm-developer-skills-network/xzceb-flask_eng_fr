import unittest

from translator import french_to_english, english_to_french

class Test(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello") 

    def test_french_to_english_2(self):
        self.assertEqual(french_to_english("Rouge"), "Red") 

    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")


unittest.main()