import unittest

from translator import frenchToEnglish, englishToFrench

class testFrenchToEnglish(unittest.TestCase):
    def test_translation(self):
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")
        self.assertNotEqual(frenchToEnglish("War"),"Guerre")

    def test_null(self):
        self.assertEqual(frenchToEnglish(""),"")


class testEnglishToFrench(unittest.TestCase):
    def test_translation(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
        self.assertNotEqual(englishToFrench("Guerre"),"War")

    def test_null(self):
        self.assertEqual(englishToFrench(""),"")

if __name__ == '__main__':
    unittest.main()