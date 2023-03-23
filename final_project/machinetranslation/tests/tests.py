"""System module."""
import unittest
from translator import frenchToEnglish, englishToFrench

class Testf2e(unittest.TestCase):
    """ Testf2e """
    def test_1(self):
        ''' test_1 '''
        self.assertEqual(frenchToEnglish('0'), '0')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish("None"), '')
        self.assertNotEqual(frenchToEnglish(0), 0)


class Teste2f(unittest.TestCase):
    """ Teste2f """
    def test_1(self):
        ''' test_1 '''
        self.assertEqual(englishToFrench('0'), '0')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(englishToFrench("None"), '')
        self.assertNotEqual(englishToFrench(0), 0)

unittest.main()