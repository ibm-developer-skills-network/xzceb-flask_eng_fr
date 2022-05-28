import machinetranslation
from machinetranslation import translator
from flask import Flask, render_template, request
import json


app = Flask("Web Translator")

@app.route("/english_to_french")
def english_to_french():
    # Write your code here
    french_text = request.args.get('english_text')
    print(french_text)
    return ("Translated text to French:{}".format(french_text))

@app.route("/french_to_english")
def french_to_english():
    # Write your code here
    english_text = request.args.get('french_text')
    print(english_text)
    return ("Translated text to English:{}".format(english_text))


@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
