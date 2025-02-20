import os
import google.generativeai as genai
from google import genai
from chromadb_handler import embed_query, retrieve_top_n, format_context
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Check if API Key is loaded
if not API_KEY:
    raise ValueError("Error: GEMINI_API_KEY is missing in .env file!")

# Configure Gemini API
# genai.configure(api_key=API_KEY)

# Function to Format Prompt for Gemini API
def format_prompt(query, retrieved_context):
    """ Combine user query with retrieved context for Gemini prompt. """
    return f"""
    You are a travel agent AI. A user asked:
    **User Query:** "{query}"

    Based on the following travel information, provide a concise and relevant response:

    {retrieved_context}
    """

# Function to Generate AI Response Using RAG
def generate_response(query):
    """ RAG pipeline: Embed query, retrieve context, and call Gemini. """
    # Embed the user query
    query_embedding = embed_query(query)

    # Retrieve relevant documents from ChromaDB
    retrieved_docs = retrieve_top_n(query, n=3) # Top 3 relevant documents
    print("retrieved_docs", retrieved_docs)

    # Format retrieved context
    retrieved_context = format_context(retrieved_docs)
    print("retrieved_context", retrieved_context)

    # Format prompt for Gemini
    prompt = format_prompt(query, retrieved_context)
    print("prompt", prompt)

    # Call Gemini API

    client = genai.Client(api_key=API_KEY)
    response = client.models.generate_content(
        model='gemini-2.0-flash', contents=prompt
    )
    print("response:" ,response.text)


    # Return AI-generated response
    return response.text

print("RAG Pipeline Initialized. Ready for AI Responses.")
