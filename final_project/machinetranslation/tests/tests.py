import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
	def test_en_fr(self):
		self.assertEqual(englishToFrench("Hello"), 'Bonjour')
		self.assertNotEqual(englishToFrench("Hello"), 'Hi')
		self.assertNotEqual(englishToFrench("None"), '')
		self.assertNotEqual(englishToFrench(0), 0)

class TestFrenchToEnglish(unittest.TestCase):
	def test_fr_en(self):
		self.assertEqual(frenchToEnglish('Bonjour'), "Hello")
        
if __name__ == '__main__':
    unittest.main()