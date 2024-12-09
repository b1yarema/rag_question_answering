import os
from dotenv import load_dotenv

load_dotenv()

from retrievers.bm25_retriever import BM25Retriever
from retrievers.semantic_retriever import SemanticRetriever
from utils.chunk_utils import prepare_chunks
from llm.groq_client import GroqClient
from ui.gradio_app import GradioApp


if __name__ == "__main__":
    raw_file = os.getenv('PATH_TO_RAW_FILE')
    chunk_file = os.getenv('PATH_TO_CHUNK_FILE')
    chunks = prepare_chunks(raw_file, chunk_file)

    bm25 = BM25Retriever(chunks)
    semantic_model = SemanticRetriever(chunks)

    model = GroqClient(os.getenv('GROQ_API_KEY'), bm25, semantic_model)

    app = GradioApp(model)
    app.run()