import time
import streamlit as st
from article_writer.views_utils import combination_prompts, get_first_level_keys, get_second_level_keys, prompts_manage

from llm_utils.llm_utils import base_chat
from PIL import Image

head_image = Image.open('data/pic/head_pic.png')

def main():
    st.set_page_config(page_title="✍️文章生成器", page_icon="🌟")
    #侧边栏
    with st.sidebar:
        st.title('写作类别')
        artical_type_list = get_first_level_keys()
        artical_type = st.radio('', artical_type_list)

    st.image(head_image, use_column_width=True)
    st.title("📝文章生成器🤔")    
    #写作小类

    artical_type2_list = get_second_level_keys(artical_type)
    artical_type2 = st.radio('选择文种', artical_type2_list, horizontal=True)
    #获取提示窗体类别
    print(prompts_manage([artical_type, artical_type2]))
    prompt_info = []
    if prompts_manage([artical_type, artical_type2]) == 0:
        prompt_info = view_prompt_0()
    else:
        prompt_info = view_prompt_1()
    answer = ''

    #点击生成
    create = st.button('生成')
    if create:
        if prompt_info != []:
            with st.spinner('生成中。。。'):
                answer = base_chat(combination_prompts([artical_type, artical_type2], prompt_info))
                st.write('',answer)
        else:
            st.info('请输入必要的提示信息')
                #st.info(combination_prompts([artical_type, artical_type2], prompt_info))



#只填入主要内容的窗体
def view_prompt_0():
    main_info = ''
    main_info = st.text_area('告诉AI你想写什么')
    if main_info != '':
        return [main_info]
    else:
        return[]


#涉及到角色的窗体
def view_prompt_1():
    you = ''
    reader = ''
    main_info = ''
    col1, col2 = st.columns(2)
    you = col1.text_input('你的身份')
    reader = col2.text_input('写给谁')
    main_info = st.text_area('告诉AI你想写什么')

    if '' in (you, reader, main_info):
        return []
    else:
        return [you, reader, main_info]
    #return [you, reader, main_info]


#附加信息
def add_info_view():
    
    pass