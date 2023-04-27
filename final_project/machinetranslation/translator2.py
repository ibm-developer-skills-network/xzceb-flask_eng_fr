import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os

apikey = "zHIjSZnBrSNZIpK0PNENyWWWRD3rmW7TOKWBATrlSi7j"
url = "https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/2f8238c6-3132-402d-9c61-42021f84d845"
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

translation = language_translator.translate(
    text='Hello, how are you today?',
    model_id='en-fr').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))


class TestEnglish(unittest.TestCase): 
    """Tests whether english text is correctly translated"""
    def test1(self):
        self.assertEqual(englishToFrench('This is a hat.'), 'C\'est un chapeau.') # Test correct translation
    def test2(self):
        self.assertEqual(englishToFrench('I am a lizard.'), 'Je suis un lézard.') # Test correct translation
  
class TestFrench(unittest.TestCase): 
    """Tests whether french text is correctly translated"""
    def test1(self):
        self.assertEqual(frenchToEnglish('C\'est un chapeau.'), 'It\s a hat.') # Test correct translation
    def test2(self):
        self.assertEqual(frenchToEnglish('Je suis un lézard.'), 'I\'m a lizard.') # Test correct translation