from flask import Flask, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
    return "I haz mad hacker skillzzzzz!"