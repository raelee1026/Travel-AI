# **AI Travel Planner**
This project is an AI-powered travel recommendation application that uses a **RAG (Retrieval-Augmented Generation) pipeline** combined with **Gemini API** to provide travel suggestions and answers to user queries.

---

## [**Presentation Slide**](https://docs.google.com/presentation/d/1PYV7bg0mPHk4-wT7c6qeDQx_GKEGewhp5bxypEsul24/edit?usp=sharing)


## **Project Structure**

```
ai-travel-planner/
│
├── backend/                   # Backend for RAG + Gemini API
│   ├── app.py                 # Main backend server using Flask
│   ├── chromadb_handler.py    # ChromaDB integration for semantic search
│   ├── embeddings.py          # Handles embedding generation and storage
│   ├── rag_pipeline.py        # Retrieval-Augmented Generation pipeline
│   ├── requirements.txt       # Python dependencies
│   ├── check_embeddings.py    # Script to check embeddings
│   ├── debug_app.py           # Debugging application
│   ├── extract_data.py        # Data extraction script
│   ├── fetch_data.py           # Script to fetch data
│
└── frontend/                  # Vite + React Frontend for user interactions
    ├── src/
    │   └── components/        # React components for chat and UI
    ├── package.json           # Node.js dependencies
    └── public/                # Public assets (e.g., index.html, images, and other static files)
```

---

## **Prerequisites**

### **Backend:**

- **Python 3.7 or higher**
- **Pip** (Python package manager)
- **Virtual Environment (optional but recommended)**

### **Frontend:**

- **Node.js** (v14 or higher recommended)
- **npm** (Node package manager)
- **Vite** for React development

---

## **Setup Instructions**

### **1. Clone the Repository**

```bash
git clone https://github.com/raelee1026/ai-travel-planner.git
cd ai-travel-planner
```

---

### **2. Backend Setup**

1. Navigate to the backend directory:

   ```bash
   cd backend
   ```

2. **Create and activate a virtual environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For MacOS / Linux
   .\venv\Scripts\activate   # For Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**

   - Create a `.env` file in the `backend` directory.
   - Add your **Gemini API Key**:
     ```
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

5. **Start the Backend Server:**

   ```bash
   python3 app.py
   ```

6. **Backend Server** will run at:

   ```
   http://127.0.0.1:5000
   ```

---

### **3. Frontend Setup (Vite + React)**

1. Navigate to the frontend directory:

   ```bash
   cd ../frontend
   ```

2. **Install dependencies:**

   ```bash
   npm install
   ```

3. **Start the Vite Development Server:**

   ```bash
   npm run dev
   ```

4. **Frontend will be accessible at:**

   ```
   http://localhost:5173/
   ```

---

## **Usage**

- Open your browser and go to **[http://localhost:5173](http://localhost:5173)**
- Enter your travel-related query in the chatbox.
- The AI will provide relevant travel recommendations using the RAG + Gemini API pipeline.

---

## **Troubleshooting**

- **API Key Error:** Ensure `GEMINI_API_KEY` is correctly set in the `.env` file.
- **Module Not Found:** Double-check if dependencies are installed:
  - Backend: `pip install -r requirements.txt`
  - Frontend: `npm install`
- **Port Conflicts:** Ensure no other services are running on port `5000` or `5173`.

---

## **Credits**

- **Google Gemini API** for advanced language generation.
- **ChromaDB** for efficient vector storage and semantic retrieval.
- **LangChain** for embedding and language model integration.
- **Vite + React** for frontend development.
- **Flask** for backend development.

---

## **License**

This project is licensed under the **MIT License**. Feel free to use and modify it for your own purposes.


