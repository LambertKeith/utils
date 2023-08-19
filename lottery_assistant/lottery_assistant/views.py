import random
import streamlit as st
import pandas as pd

from llm_utils.llm_utils import base_chat
from lottery_assistant.views_util import convert_to_strings


def main():

    st.set_page_config(page_title="彩票选号")
    st.title("彩票选号")
    # 创建一个空的数据框
    data = pd.DataFrame(columns=['red1', 'red2', 'red3', 'red4', 'red5', 'red6', 'blue'])
    numbers = ''
    # 添加按钮
    if st.button('选号'):
        # 生成随机数据
        red_numbers = random.sample(range(1, 34), 6)
        blue = random.randint(1, 16)
        

        new_row = {
            'red1': red_numbers[0],
            'red2': red_numbers[1],
            'red3': red_numbers[2],
            'red4': red_numbers[3],
            'red5': red_numbers[4],
            'red6': red_numbers[5],
            'blue': blue
        }
        # 将新行添加到数据框
        data = data.append(new_row, ignore_index=True)
        red_numbers.append(blue)
        print(red_numbers)
        numbers = convert_to_strings(red_numbers)
        #st.success('已添加新数据')
        
        
    # 显示表格
    st.write('为您选择的号码：')
    st.dataframe(data)
    if numbers != '':
        st.write(base_chat(numbers))


    


