import unittest

from machinetranslation.translator import englishtofrench, frenchtoenglish

class TestEnglishToFrench(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishtofrench('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    def test_frenchToEnglish(self):
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hi')

unittest.main()