import streamlit as st

from llm_utils.llm_utils import base_chat, llm_chat


def main():
    st.set_page_config(page_title="文本格式转换器")
    st.title('文本格式转换器')
    col1, col2 = st.columns(2)
    col1.header('开始转换')
    # 一个输入框-格式
    input_text = col1.text_area("输入格式以及要求")
    col1.write("常用格式有：json，列表，元组，标号，也可以手动输入格式")

    # 两个文本框-1是内容，2是生成内容
    text_area1 = col1.text_area("要转换的内容", height=200)
    show_text = ''
    run_button = col1.button("转换")
    if run_button:
        if input_text != '' and text_area1 != '':
            show_text = base_chat(input_text, text_area1)
            print(show_text)
        else:
            col1.warning("格式和文本都要输哦~")

    #print(text_area1)
    text_area2 = col1.text_area("当当当~当", show_text, height=500)

    col2.header('示例')
    video_file = open('data/video1.mp4', 'rb')
    video_bytes = video_file.read()

    col2.video(video_bytes)


