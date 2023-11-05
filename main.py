from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

with open('GameCrawler/GameCrawler/data.json') as f:
    data = json.load(f)
@app.route('/games', methods=['GET'])
def get_games():
        return jsonify(data)

@app.route('/games/<int:id>', methods=['GET'])
def get_game(id):
    game = next((game for game in data if game['id'] == id), None)
    if game:
        return jsonify(game)
    else:
        return jsonify({'message': 'Game not found'}), 404

# @app.route('/games')
# def games():
#     with open('GameCrawler/data.json') as f:
#         return json.load(f)

@app.route('/')
def index():
    return 'Hello World'
