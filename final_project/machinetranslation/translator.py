import  os
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
authenticator = IAMAuthenticator('QFD-o48xdcvCFLJj3A1bQZVWuSz2fjE_EbIcMObHrV3F')
language_translator = LanguageTranslatorV3(
    version='2021-11-21',
    authenticator=authenticator
)


language_translator.set_service_url('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/e80c89f3-132e-474c-85e2-3961df9b9ce8')
language_translator.set_disable_ssl_verification(True)
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
def english_to_french(english_text):
    french_trans=language_translator.translate(text=english_text,model_id='en-fr').get_result()
    return french_trans.get("translations")[0].get("translation")
def french_to_english(french_text):
    english_text=language_translator.translate(text=french_text,model_id='fr-en').get_result()
    return english_text.get("translations")[0].get("translation")