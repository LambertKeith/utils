import yaml


def load_config():
    file = open(r"health_coach/llm_utils/config/llm_config2.yaml", 'r', encoding="utf-8")
    file_data = file.read()
    file.close()

    # 将字符串转化为字典或列表
    data = yaml.load(file_data, Loader=yaml.FullLoader)
    return data['app']

def load_prompt(key):
    file = open(r"health_coach/llm_utils/config/prompt.yaml", 'r', encoding="utf-8")
    file_data = file.read()
    file.close()

    # 将字符串转化为字典或列表
    data = yaml.load(file_data, Loader=yaml.FullLoader)
    return data[key]