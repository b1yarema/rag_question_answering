from rank_bm25 import BM25Okapi

def initialize_bm25(chunks):
    tokenized_corpus = [chunk.split() for chunk in chunks]
    return BM25Okapi(tokenized_corpus)

def retrieve_with_bm25(query, bm25, chunks, top_n=5):
    query_tokens = query.split()
    return bm25.get_top_n(query_tokens, chunks, n=top_n)
