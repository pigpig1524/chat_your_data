import streamlit as st

LOGO = 'https://www.fit.hcmus.edu.vn/assets/img/logos/fit-logo.png'
NO_CHUNKING = "No Chunking"
CHUNK = 'chunk'
GEMINI = 'gemini'
OPENAI = 'openai'
ONLINE_LLM = 'online_llm'
LOCAL_LLM = 'local_llm'
EN = 'en'
ENGLISH = "English"
VIETNAMESE = "Vietnamese"
VI = 'vi'
NONE = 'none'
USER = 'user'
ASSISTANT = 'assistant'
DEFAULT_LOCAL_LLM = 'hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF'
DB = 'DB'
OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']
GREETING='Xin chào! Tôi có thể giúp gì cho bạn?'