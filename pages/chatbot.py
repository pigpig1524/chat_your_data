import streamlit as st # type: ignore
from config import LOGO, GREETING
from utils.agent import Agent

def init_msg():
    if "messages" not in st.session_state:
        st.session_state.messages = [{'role': 'assistant', 'content': GREETING}]


# Page settings
st.sidebar.title('Q&A Data Assistant')
st.sidebar.header('Nhóm tác giả')
st.sidebar.markdown("""    
    Văn Hiếu Học
                    
    Phạm Minh Thy
""")

st.logo(LOGO, size='large')


if not st.session_state.index:
    st.warning('Vui lòng tải lên dữ liệu!')
else:
    agent = Agent(st.session_state.index)
    if 'message' not in st.session_state:
        init_msg()

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_input := st.chat_input("Your message:"):
        # Display user message in chat message container

        with st.chat_message("user"):
            st.markdown(user_input)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})

        response = agent.run(user_input)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            # st.write_stream(response)
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

