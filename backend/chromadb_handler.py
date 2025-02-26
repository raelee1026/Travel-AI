import chromadb
from langchain.embeddings import HuggingFaceEmbeddings
import os

# Define ChromaDB Path
CHROMA_DB_PATH = "chroma_db"
COLLECTION_NAME = "tourism"

# Initialize embedding model (same as used for storage)
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Initialize ChromaDB with Persistent Storage
chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
collection = chroma_client.get_collection(name=COLLECTION_NAME)


# Function to Embed User Query
def embed_query(query):
    """ Convert the user query into an embedding vector. """
    return embedding_model.embed_query(query)

# Function to Retrieve Top N Relevant Documents
# def retrieve_top_n(query_embedding, n=3):
#     """ Perform semantic search in ChromaDB and retrieve top N relevant documents. """
#     search_results = collection.query(query_texts=[query_embedding], n_results=n)
#     retrieved_docs = search_results.get("documents", [[]])[0]  # Top N documents
#     return retrieved_docs

def retrieve_top_n(query, n=3):
    """ Perform semantic search in ChromaDB and retrieve top N relevant documents. """
    search_results = collection.query(query_texts=[query], n_results=n)
    retrieved_docs = search_results.get("documents", [[]])[0]  # Top N documents
    return retrieved_docs


# Function to Format Retrieved Context for Gemini
def format_context(retrieved_docs):
    """ Combine retrieved documents into a context string for Gemini. """
    return "\n".join(retrieved_docs)

print("ChromaDB Handler Initialized. Ready for Retrieval.")
