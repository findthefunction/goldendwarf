from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri='mongodb://localhost:27017/cryto_data')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def data():
    items =  mongo.db.items.find_one()
    return render_template('index.html', items = items)

if '__main__' == __name__:
    app.run(debug=True)