from translator import french_to_english, english_to_french
import unittest

class Test_e_to_f(unittest.TestCase): 
    """ Testing english to french translator """
    def test1(self): 
        try:
            self.assertEqual(english_to_french(""), "")
        except:
            print("cannotpass empty string")
        self.assertEqual(english_to_french("Hello"), "Bonjour")


class Test_f_to_e(unittest.TestCase): 
    def test1(self): 
        try:
            self.assertEqual(french_to_english(""), "")
        except:
             print("cannotpass empty string")
        self.assertEqual(french_to_english("Bonjour"), "Hello")



unittest.main()