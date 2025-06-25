from flask import request, jsonify
from app import app

@app.route('/recipe', methods=['POST'])
def recipe():
    req = request.get_json()
    ingredients = req["ingredients"]
    string_list = None
    for x in ingredients:
        string_list += x
        string_list 