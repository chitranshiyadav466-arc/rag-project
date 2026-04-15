from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "API is running 🚀"

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json

    if not data or "message" not in data:
        return jsonify({"error": "Message is required"}), 400

    user_msg = data.get("message")

    return jsonify({
        "reply": f"You said: {user_msg}"
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)