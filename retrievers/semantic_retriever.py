from sentence_transformers import SentenceTransformer, util

def initialize_semantic_search_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

def retrieve_with_semantic_search(query, model, chunks, top_n=5):
    query_embedding = model.encode(query, convert_to_tensor=True)
    chunk_embeddings = model.encode(chunks, convert_to_tensor=True)
    scores = util.semantic_search(query_embedding, chunk_embeddings, top_k=top_n)
    return [chunks[result['corpus_id']] for result in scores[0]]
