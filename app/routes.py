from flask import Blueprint, request, jsonify
from .game_logic import shuffle_positions

api = Blueprint('api', __name__)

@api.route('/start', methods=['POST'])
def start_game():
    positions = shuffle_positions()
    return jsonify({"positions": positions})

@api.route('/guess', methods=['GET'])
def guess():
    data = request.json
    guess = data.get('guess')
    correct_position = data.get('correct_position')
    if guess == correct_position:
        return jsonify({"result": "correct"})
    return jsonify({"result": "wrong"})
