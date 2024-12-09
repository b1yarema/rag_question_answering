import streamlit as st
from retrievers.bm25_retriever import initialize_bm25, retrieve_with_bm25
from retrievers.semantic_retriever import initialize_semantic_search_model, retrieve_with_semantic_search
from llm.llm_model import load_llm, generate_answer
from utils.chunk_utils import prepare_chunks

# Streamlit App
st.title("RAG Question Answering")

# Prepare chunks
raw_file = 'data/Karibska_Tayemnicya.txt'
chunk_file = 'data/chunks.json'
chunks = prepare_chunks(raw_file, chunk_file)

# Initialize components
bm25 = initialize_bm25(chunks)
semantic_model = initialize_semantic_search_model()
llm = load_llm()

query = st.text_input("Enter your query:")
method = st.selectbox("Choose retrieval method:", ['bm25', 'semantic'])

if st.button("Get Answer"):
    if method == 'bm25':
        retrieved_chunks = retrieve_with_bm25(query, bm25, chunks)
    elif method == 'semantic':
        retrieved_chunks = retrieve_with_semantic_search(query, semantic_model, chunks)
    else:
        st.error("Invalid method!")
        st.stop()

    answer = generate_answer(query, retrieved_chunks, llm)
    st.success(f"Answer: {answer}")
