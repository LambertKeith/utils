import streamlit as st

from llm_utils.llm_utils import llm_chat



def main():
    #st.set_page_config(page_title="广告生成器", layout='wide')
    st.set_page_config(page_title="广告策划师")

    st.title('广告策划师')


    st.write('我是您的广告策划师，请告诉我您的需要，为您设计适合的广告词')
    prompt = st.text_input('请输入')
    print("pr", prompt)
    if prompt != '':
        write_ad = llm_chat(prompt)
        st.write(write_ad)

