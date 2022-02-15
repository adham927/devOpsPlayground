from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! " + os.environ['HOSTNAME'] + "</p>"

@app.route("/")
def hello(name):
    return f"Hello, {name}!"

app.run(host='0.0.0.0', port=3000)

