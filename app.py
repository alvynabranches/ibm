import os
import json
import logging
from flask import Flask, jsonify, request

app = Flask(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file = os.path.join(os.path.dirname(__file__), 'data.json')
data = json.load(open(file)) if os.path.isfile(file) else []

@app.route("/", methods=['GET'])
def index():
    return jsonify({"data": data}), 200

@app.route("/", methods=['POST'])
def create():
    try:
        params = json.loads(request.data.decode('utf-8'))
    except Exception as e:
        logger.error(e)
        return jsonify({"status": "error", "message": "provide valid json data"}), 400
    if params is None or len(params) == 0:
        logger.error("provid valid json data")
        return jsonify({"status": "error", "message": "provide valid json data"}), 400
    
    print(type(params))
    if type(data) == dict:
        data.append(params)
    elif type(data) == list:
        data.extend(params)
    else:
        return jsonify({"status": "error", "message": "provide valid json data"}), 400
    json.dump(data, open(file, 'w'))
    return jsonify({"status": "successfully created!", "data": params}), 201

if __name__ == '__main__':
    app.run(os.environ.get("HOST", "0.0.0.0"), os.environ.get("PORT", 5000), False if str(os.environ.get("DEBUG")).lower() == "false" else True)
    