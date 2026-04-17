from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

MY_SECRET_KEY = "rag12345"

@app.route("/")
def home():
    return "API is running"

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json

    # Flexible API key check
    api_key = request.headers.get("x-api-key")
    if api_key and api_key != MY_SECRET_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    if not data:
        return jsonify({"error": "No data received"}), 400

    # Handle BOTH formats
    if "message" in data:
        user_msg = data["message"]

    elif "messages" in data:
        user_msg = data["messages"][-1]["content"]

    else:
        return jsonify({"error": "Invalid request format"}), 400

    return jsonify({
        "reply": f"You said: {user_msg}"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)