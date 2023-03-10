from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return str(random.random())

app.run(debug=True)