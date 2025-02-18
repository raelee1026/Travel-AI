import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Error: GEMINI_API_KEY is missing in .env file!")

GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={API_KEY}"

app = Flask(__name__)
CORS(app) 

@app.route("/api/gemini", methods=["POST"])
def gemini_chat():
    try:
        data = request.get_json()
        user_input = data.get("input", "")

        if not user_input:
            return jsonify({"error": "Input text is required"}), 400

        payload = {
            "contents": [{"parts": [{"text": user_input}]}]
        }

        headers = {"Content-Type": "application/json"}
        response = requests.post(GEMINI_API_URL, json=payload, headers=headers)

        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
