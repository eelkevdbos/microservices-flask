from flask import Flask
import requests

app = Flask(__name__)

@app.route("/<nameParam>")

def default(nameParam):

    #hello microservice
    hello = requests.get('http://hello:5000/').text;

    #name microservice
    name = requests.get("http://name:5000/%s" % nameParam).text;

    return hello + ' ' + name

if __name__ == "__main__":
    app.run(host="0.0.0.0")
