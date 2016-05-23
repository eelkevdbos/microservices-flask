from flask import Flask
app = Flask(__name__)

@app.route("/<name>")

def default(name):
    return "%s" % name

if __name__ == "__main__":
    app.run(host="0.0.0.0")
