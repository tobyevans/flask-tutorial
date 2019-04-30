from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy 
import pandas as pd
import json
import config



app = Flask(__name__)
# Set debug status
if config.ENVIRONMENT == 'development':
    app.config["DEBUG"] = True
else:
    app.config["DEBUG"] = False

# Set db config
for key, value in config.DB[config.ENVIRONMENT].items():
    app.config[key] = value
db = SQLAlchemy(app)


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
    json_data = request.get_json(force=True)
    print(json_data)
    for k,v in json_data.items():
        new_mongoose = Mongoose(mon=k,goose=v)
        db.session.add(new_mongoose)
        db.session.commit()
    return jsonify(request.get_json(force=True))


class Mongoose(db.Model):
    __tablename__ = "Mongoose"
    id = db.Column(db.Integer, primary_key=True)
    mon = db.Column(db.String(80), unique=True, nullable=False)
    goose = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Mongoose %r>' % self.mon 
