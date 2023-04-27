import unittest 

from translator import englishToFrench, frenchToEnglish

class FrenchNull(unittest.TestCase):
    """Test to raise a Type Error at Null Input for frenchToEnglish"""
    def test1(self):
        self.assertRaises(TypeError, frenchToEnglish)

class EnglishNull(unittest.TestCase):
    """Test to raise a Type Error at Null Input for englishToFrench"""
    def test1(self):
        self.assertRaises(TypeError, englishToFrench)

class HelloTest(unittest.TestCase):
    """Test translation of Hello to Bonjour"""
    def test1(self):
        self.assertRegexpMatches(englishToFrench('Hello'), 'Bonjour')

class BonjourTest(unittest.TestCase):
    """Test translation of Bonjour to Hello"""
    def test1(self):
        self.assertRegexpMatches(frenchToEnglish('Bonjour'), 'Hello')

unittest.main()
