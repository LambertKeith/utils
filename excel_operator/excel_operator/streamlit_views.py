import streamlit as st
import pandas as pd

def main():
    st.title('上传 Excel 文件')
    #上传文件框
    uploaded_file = st.file_uploader("选择文件", type=['xlsx', 'xls'])
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        st.write(df.head(10))

    input_text = st.text_input('输入分析需求')
    if st.button('确认'):
        st.write(f'您输入的文本是: {input_text}')
