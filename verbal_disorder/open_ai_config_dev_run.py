from . import open_ai_config

def test1():
    openai_key = open_ai_config.get_api_key()
    openai_base = open_ai_config.get_api_base() 
    print("openai_key: ", openai_key) 
    print("openai_base: ", openai_base)  

def dev_run():
    test1()  