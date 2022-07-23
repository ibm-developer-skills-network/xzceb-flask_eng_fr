"""
Test Class for translator.py methods by Gabriele Cano
"""
import unittest
import os
from dotenv import load_dotenv
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    """
    Test cases for english_to_french method
    """
    def test_simple_test(self):
        """
        Test a simple string
        """
        result = english_to_french('Hello')
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["result"], "Bonjour")
    def test_empty_string(self):
        """
        Test an empty string
        """
        result = english_to_french('')
        self.assertEqual(result["status"], 400)
    def test_null_string(self):
        """
        Test a null string
        """
        result = english_to_french(None)
        self.assertEqual(result["status"], 400)
    def test_non_existent_word(self):
        """
        Test a null string
        """
        result = english_to_french("ashjdakjsd")
        self.assertEqual(result["status"], 400)


class TestFrenchToEnglish(unittest.TestCase):
    """
    Test cases for french_to_english method
    """
    def test_simple_test(self):
        """
        Test a simple string
        """
        result = french_to_english('Bonjour')
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["result"], "Hello")
    def test_empty_string(self):
        """
        Test an empty string
        """
        result = french_to_english('')
        self.assertEqual(result["status"], 400)
    def test_null_string(self):
        """
        Test a null string
        """
        result = french_to_english(None)
        self.assertEqual(result["status"], 400)
    def test_non_existent_word(self):
        """
        Test a null string
        """
        result = french_to_english("ashjdakjsd")
        self.assertEqual(result["status"], 400)


class TestAssertEnvironmentVariables(unittest.TestCase):
    """
    Test cases for environments variables
    """
    def test_simple_test(self):
        """
        Test a simple string
        """
        load_dotenv()
        apikey = os.environ['apikey']
        url = os.environ['url']
        self.assertTrue(len(apikey) > 0)
        self.assertTrue(len(url) > 0)

unittest.main()
