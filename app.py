import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Enable logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/receive', methods=['POST'])
def receive_data():
    try:
        data = request.get_json()
        if not data:
            raise ValueError("Invalid data received")
        return jsonify({"message": "Data received successfully!"}), 200
    except Exception as e:
        app.logger.error(f"Error processing request: {e}")
        return jsonify({"error": str(e)}), 500  # Return a proper error message

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
