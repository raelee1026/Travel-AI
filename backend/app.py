import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from rag_pipeline import generate_response  # Import RAG pipeline function

# Load Environment Variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Error: GEMINI_API_KEY is missing in .env file!")

# Flask App Setup
app = Flask(__name__)
CORS(app)

# Gemini API Endpoint
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateText?key={API_KEY}"

@app.route("/api/gemini", methods=["POST"])
def gemini_chat():
    """ Handle user query, run RAG pipeline, and get AI response. """
    try:
        # Get User Input from Request
        data = request.get_json()
        user_input = data.get("input", "")

        if not user_input:
            return jsonify({"error": "Input text is required"}), 400

        # Run RAG Pipeline to get Contextual Response
        ai_response = generate_response(user_input)

        # Return AI-generated Response
        return jsonify({"query": user_input, "response": ai_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def home():
    """ Health check endpoint. """
    return "AI Travel Planner Backend is running!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
