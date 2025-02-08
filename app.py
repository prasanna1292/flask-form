from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "data.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_data(data):
    received_data = load_data()
    received_data.append(data)  # Append new data
    with open(DATA_FILE, "w") as file:
        json.dump(received_data, file)


@app.route('/receive', methods=['POST'])
def receive_data():
    data = request.get_json()
    if data:
        save_data(data)
        return jsonify({"message": "Data received successfully!"}), 200
    return jsonify({"error": "Invalid data"}), 400


@app.route('/display', methods=['GET'])
def display_data():
    received_data = load_data()

    if not received_data:
        return "<h1>No data received yet.</h1>"

    # Get the last received entry
    last_entry = received_data[-1]

    result = "<h1>Received Data</h1>"
    result += f"<p>Name: {last_entry.get('name', 'N/A')}<br> Email: {last_entry.get('email', 'N/A')}</p>"

    return result

if __name__ == '__main__':
    app.run(debug=True)
