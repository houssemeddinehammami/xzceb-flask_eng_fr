from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/english_to_french")
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = textToTranslate.english_to_french
    return translated_text


@app.route("/french_to_english")
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = textToTranslate.french_to_english
    return translated_text

@app.route("/")
def renderIndexPage():
    return render_template('index.html')
       
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
