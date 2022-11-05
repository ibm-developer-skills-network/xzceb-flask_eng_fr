import unittest

class TestStringMethods(unittest.TestCase):
    #Firstly I test with 2 null input
    def test_null_frenchToEnglish(self):
        self.assertEqual(englishToFrench(''),'')

    def test_null_englishToFrench(self):
            self.assertEqual(englishToFrench(''),'')


    #Secondly I test the translation for Hello to Bonjour and vis-versa
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

    def test_frenchToEnglish(self):
        self.assertEqual(englishToFrench('Bonjour'),'Hello')


if __name__ == '__main__':
    unittest.main()