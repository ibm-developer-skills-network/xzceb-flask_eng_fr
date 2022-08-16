'''This module is used to test the translator.py script'''
import unittest
from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    '''class TestE2F to initiate the test from English to French'''
    def test1(self):
        '''test the translation from English to French'''
        self.assertEqual(english_to_french("Book"),"Livre")
    def test_a(self):
        '''test the translation from English to French, text given by Coursera'''
        self.assertNotEqual(english_to_french(0),0)
        self.assertEqual(english_to_french("Hello"),"Bonjour")

class TestF2E(unittest.TestCase):
    '''class TestF2E to initiate the test from French to English'''
    def test2(self):
        '''test the translation from French to English'''
        self.assertEqual(french_to_english("Aigle"),"Eagle")
    def test_b(self):
        '''test the translation from French to English, text given by Coursera'''
        self.assertNotEqual(french_to_english(0),0)
        self.assertEqual(french_to_english("Bonjour"),"Hello")

unittest.main()
