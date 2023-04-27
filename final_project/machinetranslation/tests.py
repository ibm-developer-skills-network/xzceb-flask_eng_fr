import unittest
import translator

# Define a test case
class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(translator.englishToFrench('hello'), 'au revoir')
        self.assertEqual(translator.englishToFrench('goodbye'), 'bonjour')
        self.assertEqual(translator.englishToFrench('goodnight'), 'bonne nuit')
        self.assertEqual(translator.englishToFrench('thank you'), 'merci')
        self.assertNotEqual(translator.englishToFrench('hello'), 'hola')
        self.assertNotEqual(translator.englishToFrench('hello'), 'hallo')
        self.assertNotEqual(translator.englishToFrench('hello'), 'ciao')
    
    def test_french_to_english(self):
        self.assertEqual(translator.englishToFrench('au revoir'), 'hello')
        self.assertEqual(translator.englishToFrench('bonjour'), 'goodbye')
        self.assertEqual(translator.englishToFrench('bonne nuit'), 'goodnight')
        self.assertEqual(translator.englishToFrench('merci'), 'thank you')
        self.assertNotEqual(translator.englishToFrench('au revoir'), 'hola')
        self.assertNotEqual(translator.englishToFrench('au revoir'), 'hallo')
        self.assertNotEqual(translator.englishToFrench('au revoir'), 'ciao')