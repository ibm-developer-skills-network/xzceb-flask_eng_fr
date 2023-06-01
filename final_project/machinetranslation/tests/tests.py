import unittest
from translator import englishToFrench, frenchToEnglish


class TestEnglishToFrenchTranslation(unittest.TestCase):
    def test_e2f(self):
        english_text = "Hello"
        e2f_translate = englishToFrench(english_text)
        self.assertEqual("", "")
        self.assertEqual(e2f_translate, "Bonjour")

class TestFrenchToEnglishTranslation(unittest.TestCase):
    def test_f2e(self):
        french_text = "Bonjour"
        f2e_translate = frenchToEnglish(french_text)
        self.assertEqual("", "")
        self.assertEqual(f2e_translate, "Hello")

unittest.main()
