from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
import openai
import streamlit as st

class Agent:
    def __init__(self, index) -> None:
        openai.api_key = st.secrets['OPENAI_API_KEY']
        Settings.llm = OpenAI(
            model = st.secrets['CHAT_MODEL'], 
            temperature = 0.2
        )
        self.query_engine = index.as_query_engine()

    def run(self, user_input: str):
        return self.query_engine.query(user_input)