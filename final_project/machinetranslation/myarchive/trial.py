#import unittest
from translator import englishToFrench, frenchToEnglish
english_translation=englishToFrench('Hello')
print(english_translation)
#class Test_englishToFrench(unittest.TestCase): 
#    def test1(self): 
#        self.assertEqual(englishToFrench('Hello'), 'Bonjour') # Test for the translation of the word ‘Hello’ and ‘Bonjour’.
        #self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.
        #self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.
        
#class Test_frenchToEnglish(unittest.TestCase): 
#    def test1(self): 
#        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # Test for the translation of the word ‘Bonjour’ and ‘Hello’.
        #self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.
        #self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.
        
#unittest.main()