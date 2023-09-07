import streamlit as st

def main():
    st.set_page_config(page_title="design_your_dishes 界面", page_icon="🌟")
    st.title("同行菜谱")

    # 定义变量
    label1_content = "菜谱"
    label2_content = "水果"
    label3_content = "采购计划"

    # 创建按钮和标签
    if st.button('按钮1',use_container_width=True):
        st.write('你点击了按钮1')
    st.write(label1_content)

    if st.button('按钮2', use_container_width=True):
        st.write('你点击了按钮2')
    st.write(label2_content)

    st.write(label3_content)

