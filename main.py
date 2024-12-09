import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

from retrievers.bm25_retriever import initialize_bm25, retrieve_with_bm25
from retrievers.semantic_retriever import initialize_semantic_search_model, retrieve_with_semantic_search
from utils.chunk_utils import prepare_chunks
from llm.llm_model import load_groq_model, generate_answer_with_groq

if __name__ == '__main__':
    # Get file paths from environment variables
    raw_file = os.getenv('PATH_TO_RAW_FILE')
    chunk_file = os.getenv('PATH_TO_CHUNK_FILE')

    # Prepare the chunks
    chunks = prepare_chunks(raw_file, chunk_file)

    # Initialize the retrievers
    bm25 = initialize_bm25(chunks)
    semantic_model = initialize_semantic_search_model()

    # Load the Groq model
    model = load_groq_model()

    # Command-line interface
    while True:
        query = input("Enter your query (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        method = input("Choose retrieval method ('bm25' or 'semantic'): ")

        # Retrieve relevant chunks
        if method == 'bm25':
            retrieved_chunks = retrieve_with_bm25(query, bm25, chunks)
        elif method == 'semantic':
            retrieved_chunks = retrieve_with_semantic_search(query, semantic_model, chunks)
        else:
            print("Invalid method! Try again.")
            continue

        # Generate an answer using the Groq model
        answer = generate_answer_with_groq(query, retrieved_chunks, model)
        print(f"Answer: {answer}")
