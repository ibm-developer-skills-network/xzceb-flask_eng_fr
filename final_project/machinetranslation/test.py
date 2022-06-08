import unittest
import translator


class Test(unittest.TestCase):

    def test_eng_to_fr(self):
        self.assertEqual(translator.englishToFrench('Hello'), 'Bonjour')

    def test_fr_to_eng(self):
        self.assertEqual(translator.frenchToEnglish('Bonjour'), 'Hello')


if __name__ == '__main__':
    unittest.main()
