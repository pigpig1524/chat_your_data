import streamlit as st # type: ignore
from config import LOGO

st.sidebar.header('Chat with your data')
st.sidebar.markdown("""
**Nhóm tác giả**
                    
    Văn Hiếu Học
    Phạm Minh Thy
""")

st.session_state['language'] = st.sidebar.selectbox('Chọn ngôn ngữ', ('Tiếng Việt', 'English'))

st.logo(LOGO, size='large')

st.title('Hướng dẫn sử dụng')
st.warning('Hiện tại, data chỉ lưu giữ trong một session (Khi refresh sẽ mất data) --> Update code sau')

st.header('Bước 1: Upload data')
st.markdown("""
    * Truy cập vào thẻ `Your data`
    * Upload data: hiện hỗ trợ file PDF, DOCX/DOC
    * Quá trình xử lý data sẽ được log ra màn hình --> Cuối cùng nhấn `Save data`
""")

st.header('Bước 2: Chat thôi nào!')
st.markdown("""
Chuyển sang thẻ `Chat bot` và tiến hành hỏi đáp với data của bạn!
""")

st.warning('Hiện tại các chức năng thêm, xóa data đang được dev!')