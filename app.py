import streamlit as st
from config import LOGO

if 'data_saved_success' not in st.session_state:
    st.session_state['data_saved_success'] = False


chatbot = st.Page(page='pages/chatbot.py', title='Chat bot', icon=':material/support_agent:')
data = st.Page(page='pages/data.py', title='Your data', icon=':material/upload_file:')
guide = st.Page(page='pages/guide.py', title='Guidance', icon=':material/info:', default=True)

pg = st.navigation(
    pages=[guide, data, chatbot],
    position='sidebar'
)
pg.run()