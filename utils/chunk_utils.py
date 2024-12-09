import os
import json

def load_and_chunk_document(file_path, chunk_size=500):
    """
    Reads a document from the file system and splits it into smaller chunks.
    :param file_path: Path to the document file.
    :param chunk_size: Maximum size of each chunk (number of characters).
    :return: List of text chunks.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

def save_chunks(chunks, output_file):
    """
    Saves chunks to a JSON file with assigned IDs.
    :param chunks: List of text chunks.
    :param output_file: Path to save the JSON file.
    """
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    chunk_data = [{"id": idx, "text": chunk} for idx, chunk in enumerate(chunks)]
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(chunk_data, file, ensure_ascii=False, indent=2)

def load_chunks(chunk_file):
    """
    Loads chunks from a JSON file.
    :param chunk_file: Path to the JSON file.
    :return: List of text chunks.
    """
    with open(chunk_file, 'r', encoding='utf-8') as file:
        return [chunk["text"] for chunk in json.load(file)]

def prepare_chunks(raw_file, chunk_file, chunk_size=500):
    """
    Prepares chunks by checking if the chunk file exists. If not, creates chunks from the raw file.
    :param raw_file: Path to the original text file.
    :param chunk_file: Path to the JSON chunk file.
    :param chunk_size: Maximum size of each chunk (number of characters).
    :return: List of text chunks.
    """
    if not os.path.exists(chunk_file):
        print(f"Chunks file '{chunk_file}' not found. Creating it from '{raw_file}'...")
        chunks = load_and_chunk_document(raw_file, chunk_size)
        save_chunks(chunks, chunk_file)
        print(f"Document split into {len(chunks)} chunks and saved to '{chunk_file}'.")
    else:
        print(f"Chunks file '{chunk_file}' found. Loading...")
        chunks = load_chunks(chunk_file)
    return chunks
