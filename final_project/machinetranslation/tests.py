import translator

def test_french_to_english():
# Test translation of null input
    assert translator.french_to_english('') == ''
    assert translator.french_to_english('Bonjour') == 'Hello'

    # Test for translation of 'Bonjour' to 'Hello'
    french_text = 'Bonjour'
    expected_result = 'Hello'
    assert translator.french_to_english(french_text) == expected_result

def test_english_to_french():
    # Test for null input
    assert translator.english_to_french(None) == None

    # Test for translation of 'Hello' to 'Bonjour'
    english_text = 'Hello'
    expected_result = 'Bonjour'
    assert translator.english_to_french(english_text) == expected_result

def test_translations():
    # Test for translation of 'Hello' and 'Bonjour'
    english_text = 'Hello'
    expected_french_result = 'Bonjour'
    assert translator.english_to_french(english_text) == expected_french_result

    french_text = 'Bonjour'
    expected_english_result = 'Hello'
    assert translator.french_to_english(french_text) == expected_english_result

# Run the tests
test_french_to_english()
test_english_to_french()
test_translations()