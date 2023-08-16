import yaml, platform, os   

config_file_name = "openai_key.yml"

def_windows_config_dir = r"c:/config"
def_linux_config_dir = r"/config"

config_filepath = ""
if platform.system() == "Windows":
    config_filepath = def_windows_config_dir + "/" + config_file_name
else:
    config_filepath = os.environ['HOME'] + def_linux_config_dir + "/" + config_file_name

file = open(config_filepath, 'r', encoding="utf-8")
file_data = file.read()
file.close()

# 将字符串转化为字典或列表
data = yaml.load(file_data, Loader=yaml.FullLoader) 

def get_api_key():
    return data['api_key'] 

def get_api_base():
    return data['api_base']