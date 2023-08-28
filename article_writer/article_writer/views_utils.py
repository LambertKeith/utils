import json

#-----读取提示词json文件------
#读取侧边栏中类目列表
def get_first_level_keys(json_file_path='data/prompts.json'):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        first_level_keys = list(data.keys())
    return first_level_keys


#读取分类目列表
def get_second_level_keys(first_level_key, json_file_path='data/prompts.json'):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        second_level_keys = list(data.get(first_level_key, {}).keys())
    return second_level_keys


#读取提示词
def get_value(first_level_key, second_level_key, json_file_path='data/prompts.json'):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        value = data.get(first_level_key, {}).get(second_level_key)
    return value



#-----读取附加信息-----
#获取json值
def get_json_data_addinfo(file_path='data/additional_info.json'):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON in '{file_path}'.")
        return None    


#获取json一级键列表
def get_first_level_keys_addinfo(json_file_path='data/additional_info.json'):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        first_level_keys = list(data.keys())
    return first_level_keys




#----提示词组合-----
#提示信息调度函数
def prompts_manage(key_list):
    #如果是主要内容返回0
    if get_value(key_list[0], key_list[1])["提示组成"] == '主要内容':
        return 0
    else:
        return 1


#提示词组合函数
def combination_prompts(key_list, prompts_info):
    prompt = get_value(key_list[0], key_list[1])["提示词"]
    #根据调度函数的功能选择组合类型
    if prompts_manage(key_list) == 0:
        prompt += f'{prompts_info[0]}。'
    else:
        prompt += f'你的身份是{prompts_info[0]}，这篇文章的读者或者听者是{prompts_info[1]}，文章的主要内容关于{prompts_info[2]}。'
    return prompt


#添加附加信息
def add_info_to_prompt(addinfo, prompt):
    #获取附加信息类目
    add_list = get_first_level_keys_addinfo()