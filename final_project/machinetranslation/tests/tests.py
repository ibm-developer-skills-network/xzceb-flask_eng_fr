import unittest

from translator import english_to_french, french_to_english

class Teste2f(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test when 'Hello' is given as input the output is 'Bonjour'.
        self.assertEqual(english_to_french('World'), 'Monde')  # test when 'World' is given as input the output is 'Monde'.
        self.assertNotEqual(english_to_french('Morning'), 'Matin')  # test when 'Morning' is given as input the output is 'Matin'.
        

class Testf2e(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test when 'Bonjour' is given as input the output is 'Hello'.
        self.assertEqual(french_to_english('Monde'), 'World') # test when 'Monde' is given as input the output is 'World'.
        self.assertNotEqual(french_to_english('Matin'), 'Morning') # test when 'Matin' is given as input the output is 'Morning'.
unittest.main()