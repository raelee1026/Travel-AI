import chromadb

# Reload ChromaDB with stored data
chroma_client = chromadb.PersistentClient(path="chroma_db")
collection = chroma_client.get_collection(name="tourism")

# Check stored document count
print(f"Total stored documents: {collection.count()}")
