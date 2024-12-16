import streamlit as st

def init():
    if 'language' not in st.session_state:
        st.session_state['language'] = 'Tiếng Việt'
    if 'files' not in st.session_state:
        st.session_state.files = None
    if 'link_file' not in st.session_state:
        st.session_state.link_file = None
    if 'index' not in st.session_state:
        st.session_state.index = None
    if 'data_saved_success' not in st.session_state:
        st.session_state['data_saved_success'] = False
