import unittest
from translator import english_tofrench, french_toenglish
class TestSquare(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_tofrench("Hello"),"Bonjour")
        self.assertEqual(english_tofrench("Neck"),"Cou")
    def test2(self):
        self.assertEqual(french_toenglish("Bonjour"),"Hello")
        self.assertEqual(french_toenglish("Lait"),"Milk")
unittest.main()

