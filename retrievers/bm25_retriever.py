from rank_bm25 import BM25Okapi


class BM25Retriever:
    def __init__(self, chunks):
        self.__chunks = chunks
        self.__tokenized_corpus = [chunk.split() for chunk in chunks]
        self.__model = BM25Okapi(self.__tokenized_corpus)

    def retrieve(self, query, top_n=5):
        query_tokens = query.split()
        return self.__model.get_top_n(query_tokens, self.__chunks, n=top_n)
