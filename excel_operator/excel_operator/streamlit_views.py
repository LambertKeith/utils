import os
import streamlit as st
import pandas as pd
from PIL import Image
from excel_operator.result_utils import delete_all_files_in_directory, find_csv_files, find_png_files, read_csv_files_to_dataframe, result_info

def main():
    source_data_folder = 'source_data'
    st.title('上传 Excel 文件')
    #上传文件框
    delete_all_files_in_directory(source_data_folder)
    uploaded_file = st.file_uploader("选择文件", type=['xlsx', 'xls'])
    if uploaded_file is not None:
        #将上传的文件放入数据源目录
        file_path = os.path.join(source_data_folder, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        #显示读入的数据
        try:
            df = pd.read_csv(file_path, encoding='utf-8')
            st.table(df.head(10))
        except:
            print("编码错误")

    input_text = st.text_input('输入分析需求')
    if st.button('确认'):
        #清理原来的文件
        delete_all_files_in_directory('result_data')
        st.write(f'您输入的文本是: {input_text}')
        #获取结果
        result = result_info(file_path, input_text)
        print(result)
        #判断是否位df格式
        if isinstance(result[0], pd.DataFrame):
            print('这是df')
            st.table(result[0])
        elif result[0] != None:
            st.write(result[0])

        if result[1] != []:
            #获取png列表
            png_list = find_png_files('result_data')
            #获取csv列表
            csv_list = find_csv_files('result_data')
            for i in png_list:
                image = Image.open(i)
                st.image(image)
            if csv_list != []:
                st.table(read_csv_files_to_dataframe('result_data'))
                
