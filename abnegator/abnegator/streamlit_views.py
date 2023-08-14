import streamlit as st

from llm_utils.llm_utils import base_chat, llm_chat



def main():
    st.title('拒绝者')
    # 创建一个聊天界面
    with st.chat_message("assistant"):
        st.write("我会拒绝或者反驳你说的一切")

    # 显示聊天输入框
    prompt = st.chat_input("说点什么")
    if prompt:
        with st.chat_message("user"):
            st.write(prompt)
        answer = base_chat(prompt)
        with st.chat_message("assistant"):
            st.write(answer)