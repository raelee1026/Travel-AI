import csv
import json
import os

# Define file paths
DATA_DIR = "data_taiwan"
INPUT_FILE = os.path.join(DATA_DIR, "taiwan_attraction.csv")
OUTPUT_FILE = os.path.join(DATA_DIR, "cleaned_taiwan_attraction.json")

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Load dataset from CSV
cleaned_data = []
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cleaned_data.append({
            "title": row.get("Title", "No Title"),
            "content": row.get("Content", "No Content"),
            "region": row.get("Region-en", "No Region")
        })
    # for i, row in enumerate(reader):
    #     if i >= 10: break
    #     cleaned_data.append({
    #         "title": row.get("Title", "No Title"),
    #         "content": row.get("Content", "No Content"),
    #         "region": row.get("Region-en", "No Region")
    #     })

# Save extracted data as JSON
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(cleaned_data, f, indent=4, ensure_ascii=False)

# Display first 3 records as a check
print("Extracted and cleaned dataset saved to", OUTPUT_FILE)
for entry in cleaned_data[:3]:
    print(f"Title: {entry['title']}\nContent: {entry['content']}\nRegion: {entry['region']}\n---")

