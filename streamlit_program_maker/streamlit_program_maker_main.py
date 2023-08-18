import tkinter as tk
from tkinter import messagebox
from streamlit_program_maker.function_utils import generate_folder, generate_main_file, generate_streamlit_file
from streamlit_program_maker.views_utils import show_messagebox



#按钮控制   
def button_manage():
    input_text = entry.get()
    print(input_text)
    #如果输入的项目名不为空则进行下一步
    if input_text != '':
        #生成项目文件夹
        generate_folder(input_text)
        #生成项目入口
        generate_main_file(input_text)
        #生成页面
        generate_streamlit_file(input_text)
    else:
        show_messagebox("提示", "项目名为空")


# 创建主窗口
root = tk.Tk()
root.title("生成器")

# 获取屏幕宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 计算窗口宽度和高度
window_width = 300
window_height = 200

# 计算窗口在屏幕中的坐标
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# 设置窗口在屏幕中的位置
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# 创建标签
label = tk.Label(root, text="请输入文本:")
label.pack(pady=10)

# 创建输入框
entry = tk.Entry(root)
entry.pack(pady=5)


# 创建按钮
button = tk.Button(root, text="生成", command=button_manage)
button.pack(pady=10)

output_label = tk.Label(root, text='输入项目名，在本应用同级目录下生成项目框架')
output_label.pack()

# 启动主循环
root.mainloop()



