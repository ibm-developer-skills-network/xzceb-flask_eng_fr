
from flask import Flask, render_template, request
import json
package_folder = os.path.abspath(os.path.join(os.path.dirname(__machinetranslation__), 'machinetransaltion'))
sys.path.insert(0, package_folder)
from machinetranslation import translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    french_text = english_to_french(textToTranslate)
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    english_text = french_to_english(textToTranslate)
    return english_text

@app.route("/")
def renderIndexPage():
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
