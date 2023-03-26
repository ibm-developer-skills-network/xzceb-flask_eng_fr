from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator")

@app.route("/machinetranslation/translator/englishToFrench",methods=['POST'])
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translatedText=translator.english_To_French(textToTranslate)
    # Write your code here
    return translatedText

@app.route("/machinetranslation/translator/frenchToEnglish",methods=['POST'])
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translatedText=translator.french_To_English(textToTranslate)
    return translatedText

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
