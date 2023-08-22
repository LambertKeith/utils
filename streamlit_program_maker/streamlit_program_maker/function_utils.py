
#创建程序主入口
import os


def generate_main_file(name):
    file_name = f"{name}_main.py"
    content = f"from {name}.{name}_views import main\n\nif __name__ == '__main__':\n    main()"

    with open(file_name, "w") as file:
        file.write(content)


#创建项目相关文件夹
def generate_folder(name):
    try:
        os.mkdir(name)
        print(f"文件夹 '{name}' 创建成功！")
    except FileExistsError:
        print(f"文件夹 '{name}' 已经存在。")


#编写页面视图
def generate_streamlit_file(name):
    file_name = f"{name}/{name}_views.py"
    content = f"""import streamlit as st

def main():
    st.set_page_config(page_title="{name} 界面", page_icon="🌟")
    st.title("{name} Streamlit 界面")
    st.write("这是一个简单的Streamlit界面。")


"""

    with open(file_name, "w", encoding='utf-8') as file:
        file.write(content)