# Questions (RAG with LLM)

This project is a **retrieval-augmented generation (RAG)** system that uses **Large Language Models (LLM)** for answering questions based on the knowledge base of Agatha Christie's book **"Caribbean Mystery"**.

## Project Overview

### **Data Source**
For training the model, the text from Agatha Christie's book **"Caribbean Mystery"** was used. The text was chunked into segments that are used for information retrieval and answering questions.

### **Chunking**
Each chunk contains a fragment of the book, approximately **500 characters** long, in the key-value format, where the **key** is the sequential number and the **value** is the text fragment from the book.

### **LLM**
The answers are generated using the **groq/llama3-8b-8192** model, which ensures high-quality text generation for answering questions.

### **Retriever**
Two methods are used for retrieving relevant information:
1. **BM25** for basic keyword-based search using word frequency in the document.
2. **Semantic embeddings** using a model from the **sentence-transformers** library to find semantic similarity.

### **Reranker**
N/A (Not Implemented).

### **Citations**
The application provides context for each answer. However, it currently does not provide specific citations for the source of the retrieved data.

### **UI**
The user interface is built with **Gradio**, providing an easy way to interact with the application. There are two main options to choose from for the retrieval method: **BM25** and **Semantic Search**.

**Note:** This project requires Python **3.10** or later.

## Installation

To run the project locally, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/b1yarema/rag_question_answering.git
cd rag_question_answering
```
   
2. Set up the environment:
```bash
python3 -m venv /venv
```
Then activate it:
- On macOS source /venv/bin/activate
- On Windows .venv/Scripts/activate


3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create file .env with content of .env.example and fill 
```
GROQ_API_KEY
```

5. Run the application:
```bash
python main.py
```

This will launch the Gradio interface in your browser, allowing you to interact with the model.