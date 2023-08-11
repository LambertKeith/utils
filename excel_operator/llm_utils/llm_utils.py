
import os
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from llm_utils.read_config import load_config


config = load_config() 
os.environ["https_proxy"] = "http://localhost:7890"

def llm_quary(csv_path, prompt):
    #os.environ["https_proxy"] = "https://localhost:7890"
    print(csv_path)
    df = pd.read_csv(csv_path, encoding='gbk')
    
    OPENAI_API_KEY = config['openai_api_key']
    llm = OpenAI(api_token=OPENAI_API_KEY)

    pandas_ai = PandasAI(llm)
    response = pandas_ai.run(df, prompt=prompt+'。回答的同时请生成图片以及处理之后的表格，将图片和表格保存至result_data目录下，生成图片时需要保证中文字符可以显示')
    return response
