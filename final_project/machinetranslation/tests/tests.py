'''Test file for translation.py'''
import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    '''class to test englishToFrench()'''
    def test1(self):
        '''function to test englishToFrench()'''
        self.assertIsNone(\
            englishToFrench(None),\
            "Is none"
            ) # test when input is null
        self.assertEqual(\
            englishToFrench("Hello"),\
            "Bonjour",\
            "Is translated correctly"\
            ) # test when input is Hello

class TestFrenchToEnglish(unittest.TestCase):
    '''class to test frenchToEnglish'''
    def test1(self):
        '''function to test frenchToEnglish'''
        self.assertIsNone(\
            frenchToEnglish(None),\
            "Is none"
            ) # test when input is null
        self.assertEqual(\
            frenchToEnglish("Bonjour"),\
            "Hello",\
            "Is translated correctly"\
            ) # test when input is Bonjour

unittest.main()
