from flask import Flask, jsonify
from flask_cors import CORS
from src.calls import *

app = Flask(__name__)
CORS(app)

@app.route('/get_data')
def get_data():
    dexNumber = get_dex_number()
    nameColorGenArray = get_pokemon_info(dexNumber)
    selectedGuess = Pokemon(pokemon_constructor(nameColorGenArray[0], nameColorGenArray[1], nameColorGenArray[2]))
    data = { "name": selectedGuess.answer, "hint_list" : selectedGuess.hintList, "gen": selectedGuess.gen }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)  # Ensure debug mode is on
