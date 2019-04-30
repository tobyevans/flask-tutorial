from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
    return "I haz mad hacker skillz!"

@app.route("/api")
def api():
	data = pd.DataFrame({'words':['one', 'two','three']})
	return data.to_json(orient='records')