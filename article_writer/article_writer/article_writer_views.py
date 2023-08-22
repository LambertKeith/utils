import streamlit as st

from llm_utils.llm_utils import base_chat

def main():
    st.set_page_config(page_title="文章生成器", page_icon="🌟")
    st.title("文章生成器")
    #st.write("这是一个简单的Streamlit界面。")
    info = st.text_area("写作领域")

    select_style_col, button_style_col = st.columns(2)
    style_list = ['专业型', '休闲的', '搞怪']
    style = select_style_col.radio('写作风格', options=style_list, horizontal=True)
    button_style = button_style_col.button('自主添加')
    #选择格式
    artical_type = ['博客', '段落', '电子邮件', '演讲稿']
    a_type = st.radio('格式', options=artical_type, horizontal=True)
    lenth_list = ['100', '200', '400', '600']
    lenth = st.radio('长度', options=lenth_list, horizontal=True)
    txt = ''
    write = st.button('生成', use_container_width=True)
    if write:
        prompt = [info, style, a_type, lenth]
        txt = base_chat(prompt)
        
    artical = st.text_area("文章", txt, height=500)

