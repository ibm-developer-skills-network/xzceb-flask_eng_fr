"""
Python Final Project by Gabriele Cano
"""
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

def init_translator():
    """
    initializing the translator service
    """
    load_dotenv()
    apikey = os.environ['apikey']
    url = os.environ['url']
    local_authenticator = IAMAuthenticator(apikey)
    translator_service = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=local_authenticator
    )
    translator_service.set_service_url(url)
    return translator_service

def english_to_french(english_text):
    """
    Translate from English to French
    """
    if english_text is not None and isinstance(english_text, str) and len(english_text) > 0:
        return get_translation('en-fr',english_text)
    return {"status" : 400, "result" : "You have entered an empty text. Please retry."}

def french_to_english(french_text):
    """
    Translate from French to English
    """
    if french_text is not None and isinstance(french_text, str) and len(french_text) > 0:
        return get_translation('fr-en',french_text)
    return {"status" : 400, "result" : "You have entered an empty text. Please retry."}

def translate(translator, text):
    """
    Translate the textToTranslate with the translator
    """
    try:
        return (True, language_translator.translate(
            text=text,
            model_id=translator).get_result())
    except ApiException as ex:
        return (False, "Method failed with status code " + str(ex.code) +
                ": " + ex.message, ex.code)

def get_translation(translator, text):
    """
    Manage the text result
    """
    result = translate(translator, text)
    success = result[0]

    if success:
        result_contains_translations = len(result[1]) > 0 and 'translations' in (result[1])
        if result_contains_translations:
            translations = result[1]['translations']
            translations_contains_translation = (len(translations) > 0 and
            'translation' in (translations[0]))
            if translations_contains_translation:
                translation = translations[0]['translation']
                translation_is_not_empty = len(translation) > 0
                if translation_is_not_empty:
                    successful_translation = translation.casefold() != text.casefold()
                    if successful_translation:
                        return {"status" : 200, "result" : translation}
                    return {"status" : 400, "result" : "Can't find a translation"}
    return {"status" : 500, "result" : "Error"}

#Main Code

print("Welcome to the English/French translator!")
language_translator = init_translator()

if language_translator is not None:
    SELECT_CONDITION = True
    translators = {
        1:('English -> French', english_to_french),
        2:('French -> English', french_to_english),
        3:('Exit', None)}

    while SELECT_CONDITION:
        print("Select a translator:")
        for key,item in translators.items():
            print('' + str(key) + '. ' + item[0])
        selection = input()
        INT_SELECTION = None

        if selection.isdigit():
            INT_SELECTION = int(selection)

            if INT_SELECTION in (translators) and INT_SELECTION != 3:
                text_to_translate=input("You have selected the "
                + translators[INT_SELECTION][0] + " translator.\n" +
                "Please enter the text you want to translate:")

                result_received = translators[INT_SELECTION][1](text_to_translate)
                status_code = result_received['status']

                manage_status = {
                    200 : ('OK', result_received['result'], True),
                    400 : ('Bad request',
                    'Sorry, I can\'t find a translation for the text: ' + text_to_translate, True),
                    500 : ('Error', 'Sorry, but something went wrong. Please retry later.', False)
                }

                print(manage_status[result_received['status']][1])
                SELECT_CONDITION = manage_status[result_received['status']][2]

            elif INT_SELECTION == 3:
                print("Bye!")
                SELECT_CONDITION = False
            else:
                print("You have entered a wrong selection (" + selection + "). Please retry.")
        else:
            print("You have entered a wrong selection (" + selection + "). Please retry.")
else:
    print("I'm sorry, but the translator is currently unavailable. Please retry.")
