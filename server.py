from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return 'welcome'

@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/<id>/')
def read(id):
    return 'read :' +id

app.run(debug=True)