import unittest

from translator import english_to_french, french_to_english

class TestMyModule(unittest.TestCase):
    def test_fr_to_en_null(self):
        self.assertIsNotNone(english_to_french(''))
    def test_en_to_fr_null(self):
        self.assertIsNotNone(french_to_english(''))
    def test_en_to_fr_hello(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    def test_fre_to_en_bonjour(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
if __name__ == '__Main__':
    unittest.main()
