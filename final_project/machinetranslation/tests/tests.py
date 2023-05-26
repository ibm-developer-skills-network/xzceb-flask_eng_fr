from translate import Translator

def englishToFrench(text):
    translator = Translator(from_lang='en', to_lang='fr')
    translation = translator.translate(text)
    return translation

def frenchToEnglish(text):
    translator = Translator(from_lang='fr', to_lang='en')
    translation = translator.translate(text)
    return translation


## Test 1 English to French
englishText = "Hello"
frenchTranslation = englishToFrench(englishText)
print(frenchTranslation)

## Test 2 for English to French - Null
englishText = ""
frenchTranslation = englishToFrench(englishText)
print(frenchTranslation)

## Test 1 for French to English
frenchText = "Bonjour"
englishTranslation = frenchToEnglish(frenchText)
print(englishTranslation)

## Test 2 for French to English - Null
frenchText = ""
englishTranslation = frenchToEnglish(frenchText)
print(englishTranslation)