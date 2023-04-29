import unittest

from translator import englishToFrench as E2F 
from translator import frenchToEnglish as F2E

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(E2F('Hello'),'Bonjour')
        self.assertEqual(E2F('One, TWO, Three'),'Un, DEUX, Trois')
        #self.assertIsNotNone(E2F(englishText))

class TestF2E(unittest.TestCase):
    def test2(self):
        self.assertEqual(F2E('Bonjour'),'Hello')
        self.assertEqual(F2E('Un, DEUX, Trois'),'One, TWO, Three')
        #self.assertIsNotNone(F2E(frenchText))


unittest.main()
