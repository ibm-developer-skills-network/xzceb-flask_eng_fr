apikey = "XzuiiJ1gTmNT7kko5NGjTdSeOoyKPwGLYW7lJ0Z7HaxC"
url ="https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/533b174c-215d-4acd-b658-de7da345e333"


from gettext import translation
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(version="2018-05-01", authenticator= authenticator)
lt.set_service_url(url)


def englishToFrench(englishText):
    translation = lt.translate(text=englishText, model_id="en-fr").get_result()
    frenchText = translation["translations"][0]["translation"]
    print(frenchText)
    return frenchText

def frenchToEnglish(frenchText):
    translation = lt.translate(text=frenchText, model_id="fr-en").get_result()
    englishText = translation["translations"][0]["translation"]
    print(englishText)
    return englishText

englishToFrench("Hello dear, how are you? It is such a lovely day, is not it?")
