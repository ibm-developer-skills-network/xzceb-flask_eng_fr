import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):

    def test_englishToFrench(self):
        # Test for null input
        self.assertRaises(ValueError, englishToFrench, None)
        
        # Test for translation of 'Hello'
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        
        # Test for translation of 'Goodbye'
        self.assertEqual(englishToFrench('Goodbye'), 'Au revoir')

    def test_frenchToEnglish(self):
        # Test for null input
        self.assertRaises(ValueError, frenchToEnglish, None)
        
        # Test for translation of 'Bonjour'
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        
        # Test for translation of 'Au revoir'
        self.assertEqual(frenchToEnglish('Au revoir'), 'Goodbye')

if __name__ == '__main__':
    unittest.main()
