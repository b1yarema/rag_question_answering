from groq import Groq


class GroqClient:
    def __init__(self, api_key, bm25, semantic_model = None):
        self.__client = Groq(api_key=api_key)
        self.__bm25 = bm25
        self.__semantic_model = semantic_model

    def __generate_answer(self, query, retrieved_chunks):
        context = " ".join(retrieved_chunks)
        prompt = f"Answer the following question: {query}\nContext: {context}"

        chat_completion = self.__client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="llama3-8b-8192",
        )

        answer = chat_completion.choices[0].message.content
        return answer

    def get_answer(self, query, method):
        if not query:
            return "Please provide a query."

        # Retrieve relevant chunks
        if method == 'bm25':
            retrieved_chunks = self.__bm25.retrieve(query)
        elif method == 'semantic':
            retrieved_chunks = self.__semantic_model.retrieve(query)
        else:
            return "Invalid retrieval method."

        # Generate an answer using the Groq model
        answer = self.__generate_answer(query, retrieved_chunks)
        return f"**Retrieved Context:**\n{retrieved_chunks}\n\n**Answer:**\n{answer}"