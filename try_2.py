import streamlit as st
import gdown
import io
from io import BytesIO
from docx import Document # type: ignore

all_data = ''

st.header('Tải lên dữ liệu từ kho lưu trữ trực tuyến')
with st.form('link_upload'):
    link = st.text_input('Dán link công khai (public link) đến tệp dữ liệu của bạn')
    submit = st.form_submit_button('Submit my picks')

if submit:
    st.write('Submitted link:', link)
    link_file = BytesIO()
    gdown.download(url=link, output=link_file, fuzzy=True)
    # st.write(t)
    # st.session_state.files.append(FileIO(file=t))

    doc = Document(link_file)
    docx_text = [para.text for para in doc.paragraphs if para.text]

    for text in docx_text:
        all_data += f"{text}\n"

    st.write(all_data)