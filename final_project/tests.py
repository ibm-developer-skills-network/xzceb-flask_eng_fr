import unittest

from translator import english_to_french, french_to_english

class EnglishToFrench(unittest.TestCase): 

    def test1(self): 
        self.assertEqual(english_to_french('How are you?'), 'Comment es-tu?') 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') 
        

class FrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Comment es-tu?'), 'How are you?') 
        self.assertEqual(french_to_english('Bonjour?'), 'Hello?') 

       
unittest.main()