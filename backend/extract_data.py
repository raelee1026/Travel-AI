import json
import os

# Define file paths
DATA_DIR = "data"
INPUT_FILE = os.path.join(DATA_DIR, "tourism_wikipedia.json")
OUTPUT_FILE = os.path.join(DATA_DIR, "cleaned_tourism_wikipedia.json")

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Load dataset from JSON
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

# Extract title and content
cleaned_data = [
    {"title": row["row"].get("Title", "No Title"), "content": row["row"].get("Content", "No Content")}
    for row in raw_data
]

# Save extracted data as JSON
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(cleaned_data, f, indent=4, ensure_ascii=False)

# Display first 3 records as a check
print("Extracted and cleaned dataset saved to", OUTPUT_FILE)
n = 0
for entry in cleaned_data[:3]:
    print(f"Title: {entry['title']}\nContent: {entry['content']}\n---")
