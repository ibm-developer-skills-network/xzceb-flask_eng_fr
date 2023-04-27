import unittest
import translator

class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(translator.english_to_french('hello'), 'Bonjour')
        self.assertEqual(translator.english_to_french('goodbye'), 'Au revoir')
        self.assertNotEqual(translator.english_to_french('hello'), 'Hola')
        self.assertNotEqual(translator.english_to_french('hello'), 'Hallo')
        self.assertNotEqual(translator.english_to_french('hello'), 'Ciao')
    
    def test_french_to_english(self):
        self.assertEqual(translator.french_to_english('bonjour'), 'Hello')
        self.assertEqual(translator.french_to_english('au revoir'), 'Goodbye')
        self.assertNotEqual(translator.french_to_english('au revoir'), 'Hola')
        self.assertNotEqual(translator.french_to_english('au revoir'), 'Hallo')
        self.assertNotEqual(translator.french_to_english('au revoir'), 'Ciao')

if __name__ == '__main__':
    unittest.main()