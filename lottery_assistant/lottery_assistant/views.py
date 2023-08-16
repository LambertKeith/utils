import random
import streamlit as st
import pandas as pd


def main():

    st.set_page_config(page_title="彩票选号")
    st.title("彩票选号")
    # 创建一个空的数据框
    data = pd.DataFrame(columns=['red1', 'red2', 'red3', 'red4', 'red5', 'red6', 'blue'])

    # 添加按钮
    if st.button('选号'):
        # 生成随机数据
        new_row = {
            'red1': random.randint(1, 33),
            'red2': random.randint(1, 33),
            'red3': random.randint(1, 33),
            'red4': random.randint(1, 33),
            'red5': random.randint(1, 33),
            'red6': random.randint(1, 33),
            'blue': random.randint(1, 16)
        }
        # 将新行添加到数据框
        data = data.append(new_row, ignore_index=True)

        st.success('已添加新数据')

    # 显示表格
    st.write('数据表格：')
    st.dataframe(data)


