import unittest
from translator import englishtofrench
from translator import frenchtoenglish

class TestF2E(unittest.TestCase):
    """English to French tests"""
    def test1(self):#Test for null input f2e
        self.assertNotEqual(frenchtoenglish("None"),'')
        self.assertNotEqual(frenchtoenglish(0),0)
        self.assertEqual(frenchtoenglish('Bonjour'),'Hello')
        self.assertEqual(frenchtoenglish('Je vous remercie'),'Thank You')

class TestE2F(unittest.TestCase):
    """French to English tests"""
    def test1(self):#Test for null input e2f
        self.assertNotEqual(englishtofrench("None"),'')
        self.assertNotEqual(englishtofrench(0),0)
        self.assertEqual(englishtofrench('Hello'),'Bonjour')
        self.assertEqual(englishtofrench('Thank You'),'Je vous remercie')

unittest.main()