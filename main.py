from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/games')
def games():
    with open('GameCrawler/data.json') as f:
        return json.load(f)

@app.route('/')
def index():
    return 'Hello World'

