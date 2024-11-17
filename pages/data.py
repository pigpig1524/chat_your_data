import streamlit as st
import pdfplumber # for pdf extract
import io
import pandas as pd
from docx import Document
import uuid
from utils.chunking import Chunker
from utils.indexing import Indexer
from config import LOGO


# Page settings
st.sidebar.header('Chat with your data')
st.sidebar.markdown("Using LLM and the RAG system.")
st.logo(LOGO, size='large')


# User upload data
st.header('Tải lên dữ liệu của bạn')
uploaded_files = st.file_uploader(
    label='Chọn file để tải lên', 
    type=['pdf', 'docx', 'doc'], 
    accept_multiple_files=True
)
st.session_state.files=uploaded_files


if st.session_state.files:
    files_name = pd.Series([x.name for x in st.session_state.files])
    st.dataframe(
        data=files_name,
        hide_index=True
    )

if uploaded_files is not None:
    all_data = ''
    for uploaded_file in uploaded_files:
        # print(uploaded_file.type)
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
            
    
    if all_data:
        st.success('Data processed successfully!')
        st.session_state.data_saved_success = True

        st.subheader("Chunking")
        chunker = Chunker()
        nodes = None
        try:
            nodes = chunker.chunk(text=all_data)
            st.success('Chunked successfully!')
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
