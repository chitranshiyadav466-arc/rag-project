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

    
    api_key = request.headers.get("x-api-key")

    if api_key != MY_SECRET_KEY:
        return jsonify({"error": "Unauthorized"}), 401

   
    if not data or "message" not in data:
        return jsonify({"error": "Message is required"}), 400

    user_msg = data["message"]

    return jsonify({"reply": f"You said: {user_msg}"})