import streamlit as st

def init():
    if 'files' not in st.session_state:
        st.session_state.files = None
    if 'index' not in st.session_state:
        st.session_state.index = None
    if 'data_saved_success' not in st.session_state:
        st.session_state['data_saved_success'] = False