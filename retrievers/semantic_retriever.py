from sentence_transformers import SentenceTransformer, util


class SemanticRetriever:
    def __init__(self, chunks, model_name='all-MiniLM-L6-v2'):
        self.__chunks = chunks
        self.__model = SentenceTransformer(model_name)
        self.__chunk_embeddings = self.__model.encode(self.__chunks, convert_to_tensor=True)

    def retrieve(self, query, top_n=5):
        query_embedding = self.__model.encode(query, convert_to_tensor=True)
        scores = util.semantic_search(query_embedding, self.__chunk_embeddings, top_k=top_n)

        return [self.__chunks[result['corpus_id']] for result in scores[0]]