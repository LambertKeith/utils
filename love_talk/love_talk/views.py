import streamlit as st

from llm_utils import llm_utils

def main():
    st.set_page_config(page_title="love_talk", page_icon="🌟")

    st.title("💓土味情话💕 ")

    button = st.button("生成")
    if button:
        result = llm_utils.base_chat()
        st.text_area("情话",result, height=400)
        


