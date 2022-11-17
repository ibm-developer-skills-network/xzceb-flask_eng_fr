"""
This module defines the application routes
"""
from flask import Flask, request, render_template
from ibm_translator import translator
app = Flask("Web Translator")

@app.route("/")
def renderIndexPage(): #home page of the localhost
    return render_template("index.html")

# /to_english?text="English word"
@app.route("/frenchToEnglish", methods=["GET"])
def to_english():  # put application's code here
    args = request.args.to_dict()
    if "textToTranslate" in args:
        return translator.french_to_english(args["textToTranslate"])
    return "Please pass `textToTranslate` as a query param"

# /to_french?text="French word"
@app.route("/englishToFrench", methods=["GET"])
def to_french():  # put application's code here
    args = request.args.to_dict()
    if "textToTranslate" in args:
        return translator.english_to_french(args["textToTranslate"])
    return "Please pass `textToTranslate` as a query param"


if __name__ == "__main__":
    app.run()

