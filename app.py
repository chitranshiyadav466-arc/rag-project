from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MY_SECRET_KEY = "rag12345"

@app.route("/")
def home():
    return "API is running "

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json

    # Check API key
    api_key = request.headers.get("x-api-key")
    if api_key != MY_SECRET_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    # Validate input
    if not data or "message" not in data:
        return jsonify({"error": "Message is required"}), 400

    user_msg = data.get("message")

    return jsonify({
        "reply": f"You said: {user_msg}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)