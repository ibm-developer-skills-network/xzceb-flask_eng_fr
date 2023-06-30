import unittest
from translator import englishToFrench, frenchToEnglish

class TestEF(unittest.TestCase):
    def testOne(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench('Hello'), 'Hello')

class TestFE(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')

unittest.main()
