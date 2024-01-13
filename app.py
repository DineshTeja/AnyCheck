from flask import Flask
from flask import request
from flask import render_template
from flask import Flask, request, render_template
from helpers import FullLLMChain, EssayLLMChain
import PyPDF2
import io

from helpers import FullLLMChain,EssayLLMChain

app = Flask(__name__, static_folder='static')

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/solutions", methods=["POST"])
def solutions():
    form_data = request.form

    claim = form_data["claim_box"]

    solution=FullLLMChain(claim)

    return render_template("index.html", solution=solution, claim=claim, form='dataForm')

@app.route("/essayreview", methods=["POST"])
def essay_review():
    form_data = request.form
    essay = form_data.get("essay_box", "")

    if 'file' in request.files and request.files['file'].filename != '':
        file = request.files['file']
        if file and file.filename.endswith('.pdf'):
            pdfReader = PyPDF2.PdfFileReader(io.BytesIO(file.read()))
            for pageNum in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                essay += pageObj.extractText()

    results, accuracy = EssayLLMChain(essay)
    return render_template("index.html", resultsList=results, accuracy=accuracy, essay=essay, form='secondForm')

if __name__ == "__main__":
    print("If you'd like to have tailwind running with css, make sure to run:")
    print(
        "npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch"
    )
    print("concurrently in another terminal")
    app.run(debug=True)
