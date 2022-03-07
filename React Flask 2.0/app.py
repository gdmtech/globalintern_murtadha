from flask import Flask, render_template, url_for, request


from flaskext.markdown import Markdown

import requests

# init app
app = Flask(__name__)
Markdown(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=["GET","POST"])
def extract():
    if request.method == 'POST':
        rawtext = request.form['rawtext'].strip()
        uri = "http://api.conceptnet.io/c/en/" + rawtext

        try:
          uResponse = requests.get(uri)
        except requests.ConnectionError:
          return "Connection Error"  
        Jresponse = uResponse.text

    return Jresponse
   


if __name__ == "__main__":
   app.run(host='localhost',port=8080,debug=True)