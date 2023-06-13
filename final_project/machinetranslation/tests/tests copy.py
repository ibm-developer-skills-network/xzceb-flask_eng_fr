import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def testE2F(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertNotEqual(english_to_french('yes'), 'bonjour')
    
class TestFrenchToEnglish(unittest.TestCase):
    def testF2E(self):
        self.assertEqual(french_to_english('bonjour'), 'hello')
        self.assertNotEqual(french_to_english('oui'), 'hello')

unittest.main()