import unittest
from translator import english_to_french, french_to_english


class TestEngToFr(unittest.TestCase):
    def test_eng_to_fr(self):
        self.assertEqual(english_to_french("Yes"), "Oui")
        self.assertEqual(english_to_french("one"), "Un")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        # self.assertEqual(english_to_french(None), None)
        



class TestFrtoEng(unittest.TestCase):
    def test_fr_to_eng(self):
        self.assertEqual(french_to_english("oui"), "Yes")
        self.assertEqual(french_to_english("un"), "A")
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        # self.assertEqual(french_to_english(None), None)
        

        
if __name__ == "__main__":
    unittest.main()
