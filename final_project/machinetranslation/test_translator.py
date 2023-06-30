import unittest
from translator import englishToFrench, frenchToEnglish

class TestEF(unittest.TestCase):
       def test1(self):
        # Test Hello returns Bonjour
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        # Test Hello does not return Hello
        self.assertNotEqual(englishToFrench('Hello'), 'Hello')
        # Test None returns empty string
        self.assertNotEqual(englishToFrench("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(englishToFrench(0), 0)

class TestFE(unittest.TestCase):
    def test1(self):
        # Test Hello returns Bonjour
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        # Test Hello does not return Hello
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')
        # Test None returns empty string
        self.assertNotEqual(frenchToEnglish("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(frenchToEnglish(0), 0)

unittest.main()
