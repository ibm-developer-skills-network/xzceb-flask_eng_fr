import unittest

from translator import englishToFrench as E2F 
from translator import frenchToEnglish as F2E

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(E2F('Hello'),'Bonjour')
        self.assertIsNotNone(E2F(englishText))

class TestF2E(unittest.TestCase):
    def test2(self):
        self.assertEqual(F2E('Bonjour'),'Hello')
        self.assertIsNotNone(F2E(frenchText))

