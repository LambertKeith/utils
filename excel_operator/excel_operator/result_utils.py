
import pandas as pd
import os
from llm_utils.llm_utils import llm_quary


def result_info(csv_path, prompt):
    directory_path ='result_data'
    #获得回答
    answer = llm_quary(csv_path, prompt)
    #print(answer)
    #获取生成结果
    file_list = []
    file_list = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    # 构建输出列表
    output_list = [answer, file_list]

    return output_list
    #[None, ['result_data\\top_10_players.csv', 'result_data\\top_10_players.png']]


#清理结果文件夹
def delete_all_files_in_directory(directory_path):
    try:
        file_list = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        for file_name in file_list:
            file_path = os.path.join(directory_path, file_name)
            os.remove(file_path)
        print("所有文件已成功删除。")
    except Exception as e:
        print(f"删除文件时出现错误：{e}")


#检查是否存在png
def find_png_files(directory_path):
    # 确保指定的路径存在且是一个目录
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        return "Error: Invalid directory path."

    # 保存 PNG 图片路径的列表
    png_file_paths = []

    # 遍历目录下的文件
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(".png"):
            file_path = os.path.join(directory_path, filename)
            png_file_paths.append(file_path)

    return png_file_paths


#查找csv文件
def find_csv_files(directory_path):
    # 确保指定的路径存在且是一个目录
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        return "Error: Invalid directory path."

    # 保存 CSV 文件路径的列表
    csv_file_paths = []

    # 遍历目录下的文件
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(".csv"):
            file_path = os.path.join(directory_path, filename)
            csv_file_paths.append(file_path)

    return csv_file_paths


def read_csv_files_to_dataframe(directory_path):
    # 确保指定的路径存在且是一个目录
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        return "Error: Invalid directory path."

    # 读取 CSV 文件并保存到 DataFrame
    df = pd.DataFrame()

    # 遍历目录下的文件
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(".csv"):
            file_path = os.path.join(directory_path, filename)
            try:
                data = pd.read_csv(file_path)
                df = df.append(data, ignore_index=True)
            except Exception as e:
                print(f"Error reading file {filename}: {e}")

    return df


#
#判断文件夹是否存在，若不存在就新建
def create_directory_if_not_exists(directory_path):
    if not os.path.exists(directory_path):
        try:
            os.makedirs(directory_path)
            print(f"文件夹 '{directory_path}' 已创建。")
        except Exception as e:
            print(f"创建文件夹 '{directory_path}' 失败：{e}")
    else:
        print(f"文件夹 '{directory_path}' 已存在。")