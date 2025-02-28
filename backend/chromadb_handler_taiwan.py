import chromadb
from langchain.embeddings import HuggingFaceEmbeddings
import os

# Define ChromaDB Path and Collection for Taiwan
CHROMA_DB_PATH = "taiwan_chroma_db"
COLLECTION_NAME = "tourism"

# Initialize embedding model (same as used for storage)
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Initialize ChromaDB with Persistent Storage
chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
collection = chroma_client.get_collection(name=COLLECTION_NAME)

# Function to Embed User Query
def embed_query_taiwan(query):
    """ Convert the user query into an embedding vector. """
    return embedding_model.embed_query(query)

# Function to Retrieve Top N Relevant Documents for Taiwan
def retrieve_top_n_taiwan(query, n=3):
    """
    Perform semantic search in ChromaDB and retrieve top N relevant documents for Taiwan.
    Supports both Chinese and English queries.
    """
    # Generate query embedding
    query_embedding = embed_query_taiwan(query)
    
    # Perform semantic search
    search_results = collection.query(query_embeddings=[query_embedding], n_results=n)
    retrieved_docs = search_results.get("documents", [[]])[0]  # Top N documents
    
    # Combine documents into context
    context = format_context_taiwan(retrieved_docs)
    
    return context

# Function to Format Retrieved Context for Gemini
def format_context_taiwan(retrieved_docs):
    """ Combine retrieved documents into a context string for Gemini. """
    formatted_docs = []
    for doc in retrieved_docs:
        # Extracting title, region, and content
        title = doc.get("title", "No Title")
        region = doc.get("region", "No Region")
        content = doc.get("content", "No Content")
        
        # Formatting the document
        formatted_doc = f"### {title} ({region})\n{content}"
        formatted_docs.append(formatted_doc)
    
    return "\n\n".join(formatted_docs)

# Function to Check if Query is Chinese or English
# def detect_language(query):
#     """ Check if the query is in Chinese or English. """
#     if any("\u4e00" <= char <= "\u9fff" for char in query):
#         return "zh"  # Chinese
#     else:
#         return "en"  # English

# # Main Function to Handle Taiwan-specific Retrieval
# def taiwan_retrieve_handler(query, n=3):
#     """
#     Main function to handle Taiwan-specific ChromaDB retrieval.
#     Auto-detects language and retrieves relevant context.
#     """
#     # Detect query language
#     lang = detect_language(query)
    
#     # Retrieve relevant documents
#     context = retrieve_top_n(query, n=n)
    
#     # Return formatted context
#     return context

print("Taiwan ChromaDB Handler Initialized. Ready for Retrieval.")

