"""
Unit tester for Translator module
"""
from asyncio.windows_events import NULL
import unittest

from translator import english_to_french, french_to_english

class Testenglish_to_french(unittest.TestCase):
    def test1(self):
        """
        Check for common input issues with english_to_french
        """
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french(NULL),'')
        self.assertEqual(english_to_french(''),'')
        self.assertEqual(english_to_french(0),'')
        self.assertEqual(english_to_french("Hello, how are you today?"),
        "Bonjour, comment vous êtes aujourd'hui?")

class Testfrench_to_english(unittest.TestCase):
    def test1(self):
        """
        Check for common input issues with french_to_english
        """
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english(0),'')
        self.assertEqual(french_to_english(NULL),'')
        self.assertEqual(french_to_english(''),'')
        self.assertEqual(french_to_english("Je ne sais quoi"),"I don't know what")

unittest.main()
