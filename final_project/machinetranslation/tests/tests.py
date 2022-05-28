import unittest

from translator import english_to_french, french_to_english

class Test_englishToFrench(unittest.TestCase):
    def test1(self):
        self.assertTrue('Hello', 'Bonjour')
        self.assertTrue('bye', 'au revoir')
        self.assertIsNotNone(self)

class Test_frenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertTrue('Bonjour','Hello')
        self.assertTrue('Au revoir','Bye')
        self.assertIsNotNone(self)

unittest.main()