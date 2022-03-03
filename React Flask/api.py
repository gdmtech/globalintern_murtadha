from flask import Flask,jsonify
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    uri = "http://api.conceptnet.io/c/en/example"
    try:
        uResponse = requests.get(uri)
    except requests.ConnectionError:
       return "Connection Error"  
    Jresponse = uResponse.text
    data = json.loads(Jresponse)


    return Jresponse

if __name__ == "__main__":
    app.run(host='localhost',port=8081,debug=True)
