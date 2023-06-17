import unittest
from translator import english_to_french, french_to_english

class TranslatorTests(unittest.TestCase):
    def test_english_to_french(self):
        translation1 = english_to_french("Hello")
        self.assertEqual("Bonjour", translation1)
        translation2 = english_to_french("my name is")
        self.assertEqual("mon nom est", translation2)
       
    def test_french_to_english(self):
        translation1=french_to_english("Bonjour")
        self.assertEqual("Hello", translation1)

        translation2 = french_to_english("mon nom est")
        self.assertEqual("my name is", translation2)

if __name__ == '__main__':
    unittest.main()

