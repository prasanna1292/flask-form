from flask import Flask, request, jsonify

app = Flask(__name__)

# Store received data in memory (temporary)
received_data = []

@app.route('/receive', methods=['POST'])
def receive_data():
    data = request.get_json()
    if data:
        received_data.append(data)
        return jsonify({"message": "Data received successfully!"}), 200
    return jsonify({"error": "Invalid data"}), 400

@app.route('/display', methods=['GET'])
def display_data():
    if not received_data:
        return "<h1>No data received yet.</h1>"

    last_entry = received_data[-1]

    return f"""
        <h1>Received Data</h1>
        <p><strong>Name:</strong> {last_entry.get('name', 'N/A')}<br> 
        <strong>Email:</strong> {last_entry.get('email', 'N/A')}</p>
    """

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Set port dynamically
    app.run(debug=False, host="0.0.0.0", port=port)
