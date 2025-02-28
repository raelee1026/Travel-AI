import os
import json
import re
import requests
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

CONVERSATION_HISTORY_FILE = "conversation_history.json"

# Gemini API Endpoint
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash-lite:generateText?key={API_KEY}"
# GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${API_KEY}"

def load_conversation_history():
    """load conversation history from json file"""
    if os.path.exists(CONVERSATION_HISTORY_FILE):
        with open(CONVERSATION_HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# save conversation history in json file
def save_conversation_history(history):
    """save conversation history to json file"""
    with open(CONVERSATION_HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)

@app.route("/api/gemini", methods=["POST"])
def gemini_chat():
    """ Handle user query, run RAG pipeline, and get AI response. """
    try:
        # Get User Input from Request
        data = request.get_json()
        user_input = data.get("input", "")

        if not user_input:
            return jsonify({"error": "Input text is required"}), 400
        
        conversation_history = load_conversation_history()

        history_prompt = "\n".join(conversation_history[-2:])  # Get last 2 turns of conversation history
        prompt = f"""
        You are a travel agent AI. Continue the conversation considering the context below:

        {history_prompt}

        User: {user_input}
        AI:"""

        # Run RAG Pipeline to get Contextual Response
        # ai_response = generate_response(user_input)
        ai_response = generate_response(prompt)

        conversation_history.append(f"User: {user_input}")
        conversation_history.append(f"AI: {ai_response}")

        # limit conversation history to 20
        if len(conversation_history) > 20:
            conversation_history = conversation_history[-20:]

        # Save Conversation History
        save_conversation_history(conversation_history)

        # Return AI-generated Response
        return jsonify({"query": user_input, "response": ai_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def parse_itinerary(response_text):
    """ Parse Gemini response into structured JSON format. """
    itinerary = []
    day_pattern = re.compile(r"Day (\d+):(.+?)(?=Day \d+:|$)", re.DOTALL)
    matches = day_pattern.findall(response_text)
    
    for day, places_text in matches:
        # Clean up and split places by lines or commas
        places = [place.strip() for place in re.split(r"[\n,]", places_text) if place.strip()]
        itinerary.append({
            "day": int(day),
            "places": places
        })
    
    return itinerary

@app.route("/api/gemini-taiwan", methods=["POST"])
def gemini_chat_taiwan():
    """ Handle user query, send to Gemini API, and return structured JSON response. """
    try:
        # Get User Input from Request
        data = request.get_json()
        user_input = data.get("input", "")

        if not user_input:
            return jsonify({"status": "error", "message": "Input text is required"}), 400
        
        # Prepare Request Payload for Gemini API
        payload = {
            "model": "Gemini-v1",
            "prompt": f"Create a detailed Taiwan travel itinerary for the following query:\n\n{user_input}\n\nFormat each day as 'Day X: place1, place2, place3...'.",
            "max_tokens": 500,
            "temperature": 0.7
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        # Send Request to Gemini API
        response = requests.post(GEMINI_API_URL, json=payload, headers=headers)

        # Check if Request was Successful
        if response.status_code == 200:
            api_response = response.json()
            gemini_text = api_response.get("choices", [{}])[0].get("text", "")

            # Parse Gemini Response into Structured JSON
            itinerary = parse_itinerary(gemini_text)
            number_of_days = len(itinerary)
            
            # Format Response in JSON Format
            return jsonify({
                "status": "success",
                "number_of_days": number_of_days,
                "itinerary": itinerary
            })
        else:
            return jsonify({
                "status": "error",
                "message": f"Gemini API request failed with status code {response.status_code}"
            }), 500

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/", methods=["GET"])
def home():
    """ Health check endpoint. """
    return "AI Travel Planner Backend is running!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
