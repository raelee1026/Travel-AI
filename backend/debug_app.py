from flask import Flask, request, jsonify
from rag_pipeline import generate_response

app = Flask(__name__)

# Health Check Endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK', 'message': 'RAG Pipeline is running!'}), 200

# Debug Endpoint for Testing Query
@app.route('/debug-query', methods=['POST'])
def debug_query():
    query_data = request.get_json()
    query = query_data.get('query')
    if not query:
        return jsonify({'error': 'No query provided'}), 400

    # Debug: Print the input query
    print(f"[DEBUG] User Query: {query}")

    # Generate AI Response
    response = generate_response(query)

    # Debug: Print the generated response
    print(f"[DEBUG] AI Response: {response}")

    return jsonify({'query': query, 'response': response}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
