def convert_to_strings(input_list):
    # 创建一个新的列表，用于存储转换后的字符串
    string_list = []
    
    # 遍历输入列表中的每个元素
    for item in input_list:
        # 将元素转换为字符串并添加到新的列表中
        string_list.append(str(item))
    
    return string_list