import unittest

from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):

    """English to French tests"""

    def testen2fr(self):

        self.assertNotEqual(english_to_french("None"), '')

        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestF2E(unittest.TestCase):

    """French to English tests"""

    def testfr2en(self):

        self.assertNotEqual(french_to_english("None"), '')

        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__=='__main__':
    unittest.main()