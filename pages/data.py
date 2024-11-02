import streamlit as st
# import pandas as pd
import pdfplumber # for pdf extract
import io
from docx import Document
import uuid
# from sentence_transformers import SentenceTransformer
from utils.chunking import Chunker
from utils.indexing import Indexer
from config import LOGO, NO_CHUNKING, EN, VI, NONE, USER, ASSISTANT, ENGLISH, VIETNAMESE, ONLINE_LLM, LOCAL_LLM, GEMINI, DEFAULT_LOCAL_LLM, OPENAI, DB


heders = [
    '1. Select your language',
    'Data settings'
]

# Page settings
st.sidebar.header('Chat with your data')
st.sidebar.markdown("Using LLM and the RAG system.")
st.logo(LOGO)


# User upload data
st.header(heders[1])
uploaded_files = st.file_uploader(
    label='Upload your file', 
    type=['pdf', 'docx', 'doc'], 
    accept_multiple_files=True
)


if uploaded_files is not None:
    all_data = ''
    
    for uploaded_file in uploaded_files:
        print(uploaded_file.type)
        # Determine file type and read accordingly

        if uploaded_file.name.endswith(".pdf"):
            with pdfplumber.open(io.BytesIO(uploaded_file.read())) as pdf:
                for page in pdf.pages:
                    all_data += f"{page.extract_text()}\n"

        elif uploaded_file.name.endswith(".docx") or uploaded_file.name.endswith(".doc"):
            # Extract text from DOCX
            doc = Document(io.BytesIO(uploaded_file.read()))
            docx_text = [para.text for para in doc.paragraphs if para.text]

            for text in docx_text:
                all_data += f"{text}\n"
        else:
            st.error("Unsupported file format.")
            
    # st.session_state.data_saved_success = True
    if all_data:
        st.success('Data processed successfully!')

        st.subheader("Chunking")
        chunker = Chunker()
        nodes = None
        try:
            nodes = chunker.chunk(text=all_data)
            st.success('Chunked successfully!')
            # st.write(nodes)
        except:
            st.error('Chunk failed')
    
        if nodes:
            st.subheader('Indexing')
            indexer = Indexer()
            try:
                index = indexer.index(nodes)
                st.success('Index successfully')
                save = st.button('Save data')
                if save:
                    st.success('saved!')
                    st.session_state.data_saved_success = True
                    st.session_state['index'] = index
            except:
                st.error('Index failed')

