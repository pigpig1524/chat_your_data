import streamlit as st # type: ignore
from config import LOGO

st.sidebar.title('Q&A Data Assistant')
# st.sidebar.write('Immediately get your data insights')

st.sidebar.header('Nhóm tác giả')
st.sidebar.markdown("""                    
    Văn Hiếu Học
                    
    Phạm Minh Thy
""")

# st.session_state['language'] = st.sidebar.selectbox('Chọn ngôn ngữ', ('Tiếng Việt', 'English'))

st.logo(LOGO, size='large')

st.title('Hướng dẫn sử dụng')
st.warning('Hiện tại, dữ liệu chỉ lưu giữ trong một phiên (Khi tải lại trang sẽ mất)')

st.header('Bước 1: Upload data')
st.markdown("""
    * Truy cập vào thẻ `Dữ liệu`
    * Tải lên dữ liệu: hiện chỉ hỗ trợ file PDF, DOCX/DOC
    * Quá trình xử lý dữ liệu sẽ được ghi ra màn hình $\\rightarrow$ Cuối cùng nhấn `Lưu dữ liệu`
""")

st.header('Bước 2: Chat thôi!')
st.markdown("""
Chuyển sang thẻ `Chat bot` và tiến hành hỏi đáp với data của bạn!
""")

# st.warning('Hiện tại các chức năng thêm, xóa data đang được dev!')