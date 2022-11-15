"""
This module defines the application routes
"""
from flask import Flask, request, render_template

app = Flask("Web Translator")

@app.route("/")
def renderIndexPage(): #home page of the localhost
    return render_template("index.html")

# /to_english?text="English word"
@app.route("/frenchToEnglish", methods=["GET"])
def to_english():  # put application's code here
    args = request.args.to_dict()
    if "text" in args:
        return service.french_to_english(args["text"])
    return "Please pass `text` as a query param"

# /to_french?text="French word"
@app.route("/englishToFrench", methods=["GET"])
def to_french():  # put application's code here
    args = request.args.to_dict()
    if "text" in args:
        return service.english_to_french(args["text"])
    return "Please pass `text` as a query param"


if __name__ == "__main__":
    app.run()

