import os
import shutil
import tkinter as tk

from tkinter import filedialog
import comtypes.client
import traceback

def save_file(file_path, label, label_frame):
    print('转化中')
    label.destroy()
    label = tk.Label(label_frame, text="转化中。。。")
    label.pack()
    # 检查文件扩展名是否是.docx
    if not file_path.lower().endswith(".docx"):
        print("仅支持.docx格式的Word文件转换为PDF。")
        label.destroy()
        label = tk.Label(label_frame, text="仅支持.docx格式的Word文件转换为PDF。")
        label.pack()
        return

    # 获取文件名和输出PDF的路径
    file_name = os.path.basename(file_path)
    file_name = file_name.split('.')[0]
    pdf_file_path = get_desktop_path()+ '\\' + f"{file_name}.pdf"
    print(pdf_file_path, file_path)
    # 初始化comtypes客户端
    word = comtypes.client.CreateObject("Word.Application")
    try:
        # 打开Word文档
        doc = word.Documents.Open(file_path)
        # 保存为PDF
        wd_format_pdf = 17  # 使用17来表示PDF格式
        doc.SaveAs(pdf_file_path, FileFormat=wd_format_pdf)
        # 关闭Word文档
        doc.Close()
        print(f"文件已成功转换为PDF：{pdf_file_path}")
        label.destroy()
        label = tk.Label(label_frame, text="完成！您可以在桌面上找到转化成功的文件")
        label.pack()
    except Exception as e:
        label.destroy()
        label = tk.Label(label_frame, text="转换失败")
        label.pack()
        print(f"转换失败：{str(e)}")
        traceback.print_exc(e)
    finally:
        # 退出Word应用程序
        word.Quit()


def get_desktop_path():
    # 获取当前用户的桌面路径
    user_desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    return user_desktop

def on_drop(event):
    file_path = event.data
    save_file(file_path)

def browse_file(label, label_frame):
    file_path = filedialog.askopenfilename()
    if file_path:
        save_file(file_path, label, label_frame)

def center_window(window, width, height):
    # 获取屏幕的宽度和高度
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # 计算窗口的位置
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # 设置窗口的位置
    window.geometry(f"{width}x{height}+{x}+{y}")

def main():
    # 创建主窗口
    root = tk.Tk()
    #root.geometry("300x70")
    center_window(root, 300, 70)
    root.title("变成pdf")
    label_frame = tk.Frame(root)
    label_frame.pack()
    label = tk.Label(label_frame, text="这个工具可以帮你把word转化为pdf，仅支持.docx格式")
    label.pack()

    # 按钮
    button_frame = tk.Frame(root)
    button_frame.pack()
    browse_button = tk.Button(button_frame, text="选择文件", command=lambda: browse_file(label, label_frame))
    browse_button.pack()


    root.mainloop()
