import unittest
import translator


class Test(unittest.TestCase):

    def test_null_eng_to_fr(self):
        """Null input english to french"""
        self.assertRaises('Type Error', translator.englishToFrench(''))

    def test_null_fr_to_eng(self):
        """Null input french to english"""
        self.assertRaises('Type Error', translator.frenchToEnglish(''))

    def test_eng_to_fr(self):
        """Eng-Fr Hello"""
        self.assertEqual(translator.englishToFrench('Hello'), 'Bonjour')

    def test_fr_to_eng(self):
        """Fr-Eng Bonjour"""
        self.assertEqual(translator.frenchToEnglish('Bonjour'), 'Hello')


if __name__ == '__main__':
    unittest.main()
