import chromadb
import json
import os
from langchain_huggingface import HuggingFaceEmbeddings


# Define file paths
DATA_DIR = "data"
INPUT_FILE = os.path.join(DATA_DIR, "cleaned_tourism_wikipedia.json")

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Load dataset
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    tourism_data = json.load(f)

# Limit dataset to first 5000 entries
tourism_data = tourism_data[:5000]

# Initialize embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Initialize ChromaDB with Persistent Storage
CHROMA_DB_PATH = "chroma_db"
chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
collection = chroma_client.get_or_create_collection(name="tourism")

# Get existing document IDs to prevent duplicates
existing_ids = set(collection.get()["ids"]) if collection.count() > 0 else set()

# Insert Data into ChromaDB
for idx, entry in enumerate(tourism_data):
    doc_id = str(idx)  # Ensure ID is a string

    # Skip duplicate IDs
    if doc_id in existing_ids:
        continue

    # Ensure Content is not None
    if not entry["content"] or entry["content"].strip() == "":
        continue

    # Generate embedding
    embedding = embedding_model.embed_documents([entry["content"]])[0]

    # Insert into ChromaDB
    collection.add(
        ids=[doc_id],
        documents=[entry["content"]],
        metadatas=[{"title": entry["title"]}],
    )

print(f"Successfully stored {collection.count()} embeddings in ChromaDB at {CHROMA_DB_PATH}.")
