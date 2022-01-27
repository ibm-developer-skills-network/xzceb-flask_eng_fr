import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("hello"), "Bonjour")
        self.assertEqual(english_to_french("yes"), "Oui")
        self.assertEqual(english_to_french("I love you"), "Je t'aime")
        self.assertNotEqual(english_to_french("Boots"), "Something")


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("bonjour"), "Hello")
        self.assertEqual(french_to_english("oui"), "Yes")
        self.assertEqual(french_to_english("je t'aime"), "I love you")
        self.assertNotEqual(french_to_english("non"), "Something")

unittest.main()
