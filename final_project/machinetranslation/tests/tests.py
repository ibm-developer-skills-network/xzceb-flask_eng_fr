import unittest

class Translator(unittest.TestCase):

    def english_to_french(e2f):
        e2f.assertEqual('Hello', 'Bonjour')

    def french_to_english(f2e):
        f2e.assertEqual('Bonjour', 'Hello')
        
if __name__ == '__main__':
    unittest.main()
