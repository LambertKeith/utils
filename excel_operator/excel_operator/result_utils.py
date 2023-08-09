

import os
from llm_utils.llm_utils import llm_quary


def result_info(csv_path, prompt):
    directory_path ='result_data'
    #获得回答
    answer = llm_quary(csv_path, prompt)
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
