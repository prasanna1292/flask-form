from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage
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
        <strong>Mobile:</strong> {last_entry.get('mobile', 'N/A')}<br>
        <strong>Email:</strong> {last_entry.get('email', 'N/A')}<br>
        <strong>Roll Number:</strong> {last_entry.get('rollno', 'N/A')}<br>
        <strong>Branch:</strong> {last_entry.get('branch', 'N/A')}<br>
        <strong>Message:</strong> {last_entry.get('message', 'N/A')}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)
