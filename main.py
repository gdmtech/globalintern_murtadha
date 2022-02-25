from flask import Flask, jsonify
# from flask_restful import Api, Resource

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to this example"

employees  = [{"name":"adam",
                "id":"0001",
                "position":"HR IV"},
                {"name":"steve",
                "id":"0002",
                "position":"Dev II"},
                {"name":"rachel",
                "id":"0003",
                "position":"MT III"}
            ]

@app.route("/employees", methods=['GET'])
def get():
    return jsonify({'employees':employees})

if __name__ == "__main__":
   app.run(host='localhost',port=8080,debug=True)
