from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage (temporary, resets when server restarts)
received_data = []

@app.route('/receive', methods=['POST'])
def receive_data():
    data = request.get_json()
    if data:
        received_data.append(data)  # Store in memory
        return jsonify({"message": "Data received successfully!"}), 200
    return jsonify({"error": "Invalid data"}), 400

@app.route('/display', methods=['GET'])
def display_data():
    if not received_data:
        return "<h1>No data received yet.</h1>"

    last_entry = received_data[-1]

    return f"""
        <h1>Received Data</h1>
        <p>Name: {last_entry.get('name', 'N/A')}<br> 
        Email: {last_entry.get('email', 'N/A')}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
