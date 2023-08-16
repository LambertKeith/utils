import streamlit as st

from llm_utils.llm_utils import base_chat

def main():
    st.set_page_config(page_title="语病检查员")
    st.title("语病检查员")
    result = ''
    input_text = st.text_input("输入文本")
    if st.button("检查", use_container_width=True):
        if input_text != '':
            result = base_chat(input_text)
        else:
            st.warning("请先输入需要检查的句子")
    st.text_area("检查报告",result, height=300)
