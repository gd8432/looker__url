from flask import Flask, request, jsonify
from function import looker_url
import os

app = Flask(__name__)


@app.route('/')
def main():
	return ' HELLO WORLD '

@app.route('/looker', methods=['GET'])
def test_api():
    # Get parameters from the URL
    external_user_id = request.args.get('email')
    first_name = request.args.get('name')
    last_name = request.args.get('surname')
    
    # Check if all required parameters are provided
    if not external_user_id or not first_name or not last_name:
        return jsonify({"error": "Missing parameters"}), 500

    try :
        result = looker_url(external_user_id,first_name,last_name)

        return jsonify({"result": result}), 200
    
    except Exception as e:
    
        return jsonify({"error": e}), 500


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
