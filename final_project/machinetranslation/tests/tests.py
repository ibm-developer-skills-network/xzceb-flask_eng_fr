from translator import french_to_english, english_to_french
import unittest

class Test_e_to_f(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(""), "")
        self.assertEqual(english_to_french("Hello"), "Bonjour")


class Test_f_to_e(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english(""), "")
        self.assertEqual(french_to_english("Bonjour"), "Hello")



unittest.main()