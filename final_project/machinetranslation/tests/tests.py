# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 13:06:54 2023

@author: claes_z2wsugl
"""
import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    """
    Test of english to french.
    """
    def test1(self):
        """
        Test translation
        """
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
    def test2(self):
        """
        Test English != French
        """
        self.assertNotEqual(englishToFrench("Hello"), "Hello")
    def test3(self):
        """
        Test no text.
        """
        self.assertEqual(englishToFrench(), "")

class TestFrenchToEnglish(unittest.TestCase):
    """
    Test of french to english.
    """
    def test1(self):
        """
        Test translation
        """
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
    def test2(self):
        """
        Test English != French
        """
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Bonjour")
    def test3(self):
        """
        Test no text.
        """
        self.assertEqual(frenchToEnglish(), "")

unittest.main()
