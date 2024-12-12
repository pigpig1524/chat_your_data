import streamlit as st # type: ignore
from utils.init_state import init
from config import LOGO

init()

chatbot = st.Page(page='pages/chatbot.py', title='Chat bot', icon=':material/support_agent:')
data = st.Page(page='pages/data.py', title='Dữ liệu', icon=':material/upload_file:')
guide = st.Page(page='pages/guide.py', title='Hướng dẫn', icon=':material/info:', default=True)

pg = st.navigation(
    pages=[guide, data, chatbot],
    position='sidebar'
)
pg.run()