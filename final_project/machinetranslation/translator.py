import requests

def english_to_french(english_text):
    """
    Translates English text to French.
    
    :param english_text: The English text to be translated.
    :return: The translated French text, or None if there's an error.
    """
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": english_text,
        "langpair": "en|fr"
    }

    response = requests.get(url, params=params, timeout=5)
    data = response.json()

    if response.status_code == 200 and 'responseData' in data:
        french_text = data['responseData']['translatedText']
        return french_text

    return None

def french_to_english(french_text):
    """
    Translates French text to English.
    
    :param french_text: The French text to be translated.
    :return: The translated English text, or None if there's an error.
    """
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": french_text,
        "langpair": "fr|en"
    }

    response = requests.get(url, params=params, timeout=5)
    data = response.json()

    if response.status_code == 200 and 'responseData' in data:
        english_text = data['responseData']['translatedText']
        return english_text

    return None


    

