import os
import json
import logging
from flask import Flask, jsonify, request


# Flask application
app = Flask(__name__)


# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# File to store data
file = os.path.join(os.path.dirname(__file__), 'data.json')
data = json.load(open(file)) if os.path.isfile(file) else []


# GET Request for getting data
@app.route("/", methods=['GET'])
def index():
    return jsonify({"data": data}), 200


# POST Request for adding data to list (json file)
@app.route("/", methods=['POST'])
def create():
    try:
        params = json.loads(request.data.decode('utf-8'))
    except Exception as e:
        # Will return 400 if not passed valid json data
        logger.error(e)
        return jsonify({"status": "error", "message": "provide valid json data"}), 400
    if params is None or len(params) == 0:
        # Will return 400 status if not passed valid json data
        logger.error("provid valid json data")
        return jsonify({"status": "error", "message": "provide valid json data"}), 400
    
    # If data type is dictionary than it will append to the list or if it is list than it will extend
    if type(params) == dict:
        data.append(params)
    elif type(params) == list:
        data.extend(params)
    else:
        # If it is not a list or dictionary then it will return a error message
        return jsonify({"status": "error", "message": "provide valid json data"}), 400
    
    # Write to file if the data is valid json data
    json.dump(data, open(file, 'w'))
    
    # Return 201 status
    return jsonify({"status": "successfully created!", "data": params}), 201

if __name__ == '__main__':
    app.run(os.environ.get("HOST", "0.0.0.0"), os.environ.get("PORT", 5000), False if str(os.environ.get("DEBUG")).lower() == "false" else True)
    