import unittest

from translator import english_to_french, french_to_english

class TestenglishToFrench(unittest.TestCase):
    def testenglishToFrench(self):
        self.assertNotEqual(english_to_french('null'), 'null')
        self.assertEqual(english_to_french("Hello"), "Bonjour")

class TestfrenchToEnglish(unittest.TestCase):
    def testfrenchToEnglish(self):
        self.assertNotEqual(french_to_english('null'), 'null')
        self.assertEqual(french_to_english("Bonjour"),"Hello")
unittest.main()




