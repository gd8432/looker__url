from flask import Flask, request, jsonify
from function import looker_url
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def test_api():
    # Get parameters from the URL
    External_user_id = request.args.get('External_user_id')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    
    # Check if all required parameters are provided
    if not External_user_id or not first_name or not last_name:
        return jsonify({"error": "Missing parameters"}), 500

    result = looker_url(External_user_id,first_name,last_name)

    return jsonify({"result": result}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
