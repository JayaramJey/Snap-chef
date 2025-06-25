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

@app.route('/detect', methods=['POST']) 
def detect(): 
    # Get uploaded image file from request
    # returns None if image not found
    image_file = request.files.get('image') 
    
    if image_file: 
        # mock list
        ingrediants = ['eggs', 'yogurt', 'broccoli', 'carrot'] 
        return jsonify({"ingrediants": ingrediants})
    else: 
        return jsonify({"error": "No Image uploaded"}), 400