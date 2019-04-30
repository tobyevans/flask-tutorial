from flask import Flask, jsonify, request
import pandas as pd
import json

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello():
    return "I haz mad hacker skillz!"

@app.route("/api", methods = ["GET", "POST"])
def api():
	if request.method == "GET":
		print("I iz getting data")
		data = pd.DataFrame({'words':['one', 'two','three']})
		return data.to_json(orient='records')

	print("I iz posting data")
	print(request.get_json(force=True))
	print(request.form)
	return jsonify(request.get_json(force=True))


