# from crypt import methods
from flask import Flask, render_template, url_for, request

# NLP packages
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')
from flaskext.markdown import Markdown

# init app
app = Flask(__name__)
Markdown(app)

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=["GET","POST"])
def extract():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        docx = nlp(rawtext)
        html = displacy.render(docx,style='ent')
        html = html.replace("\n\n","\n")
        result = HTML_WRAPPER.format(html)

    return render_template('results.html', rawtext = rawtext, result = result)


if __name__ == "__main__":
   app.run(host='localhost',port=8080,debug=True)