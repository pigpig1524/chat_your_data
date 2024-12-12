from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
import openai
import streamlit as st

class Agent:
    def __init__(self, index) -> None:
        openai.api_key = st.secrets['OPENAI_API_KEY']
        Settings.llm = OpenAI(
            model = st.secrets['CHAT_MODEL'], 
            # stream = True,
            temperature = 0.2
        )
        self.query_engine = index.as_query_engine()
        self.chat_engine = index.as_chat_engine(
            chat_mode = 'context',
            system_prompt = "You are a helpful assistant tasked to answer the user's question about input data or general questions. If the question is about input data, always search via your index. Please kindly inform if you can't find any matched data"
        )

    def run(self, user_input: str):
        # return self.query_engine.query(user_input)
        return self.chat_engine.chat(user_input)