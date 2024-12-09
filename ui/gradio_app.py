import gradio as gr


class GradioApp:
    def __init__(self, model):
        self.__model = model
        self.__interface = self.__create_interface()

    def __create_interface(self):
        interface = gr.Interface(
            fn=self.__model.get_answer,
            inputs=[
                gr.Textbox(lines=2, placeholder="Enter your query here...", label="Query"),
                gr.Radio(["bm25", "semantic"], label="Retrieval Method"),
            ],
            outputs="text",
            title="RAG Question Answering with Groq",
            description="A retrieval-augmented generation (RAG) system that uses BM25 to retrieve chunks and generates answers using the Groq LLM model.",
        )
        return interface

    def run(self):
        """
        Launch the Gradio app.
        """
        self.__interface.launch()
