import requests
import time
import json
import os

# Define constants
TOTAL_ROWS = 5000  # Number of rows to fetch
BATCH_SIZE = 100  # Number of rows per request
DATA_DIR = "data"
DATA_FILE = os.path.join(DATA_DIR, "tourism_wikipedia.json")

# Ensure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Function to fetch data in batches
def fetch_huggingface_data(offset, batch_size):
    url = f"https://datasets-server.huggingface.co/rows?dataset=Binaryy%2Ftourism-wikipedia&config=default&split=train&offset={offset}&length={batch_size}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("rows", [])  # Extract dataset rows
    else:
        print(f"API request failed at offset {offset}. Status code: {response.status_code}")
        return []

# Fetch data in batches
data = []
total_batches = TOTAL_ROWS // BATCH_SIZE  # 5000/100 = 50 batches

for i in range(total_batches):
    offset = i * BATCH_SIZE
    batch_data = fetch_huggingface_data(offset, BATCH_SIZE)
    
    if not batch_data:
        break  # Stop if API fails

    data.extend(batch_data)
    print(f"Fetched {len(batch_data)} rows (Total: {len(data)})")
    
    time.sleep(1)  # Avoid rate limits

# Save data as JSON
with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print(f"\nSuccessfully downloaded {len(data)} rows and saved to {DATA_FILE}")
