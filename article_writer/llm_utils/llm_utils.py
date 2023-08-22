
import getpass
import os
import openai
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from llm_utils.read_config import load_config



config = load_config() 
#os.environ["https_proxy"] = "http://localhost:7890"
os.environ["OPENAI_API_BASE"] = config['openai_base']
os.environ["OPENAI_API_KEY"] = config['openai_api_key']


def base_chat(info):
    openai.api_key = config['openai_api_key']
    openai.api_base = config['openai_base']
    prompt = f"请你扮演一个作家，写作领域或者写作的主题为<{info[0]}>，你必须学习相关的内容，确保你了解该领域或者主题；文章的语气或者风格为{info[1]}，文章格式为{info[2]},请你关注针对该格式的写作技巧和着重点，并在文章中体现；字数为{info[3]}字，请开始你的写作"
    print(prompt)
    # gpt-3.5-turbo-0301     
    completion = openai.ChatCompletion.create(
      model='gpt-3.5-turbo-0301', 
      messages=[
        {"role": "user", "content":prompt}
      ]
    )

    #print(completion)    
    
    #print("completion.usage", completion.usage) 
    print(completion.choices[0].message['content'])  
    return completion.choices[0].message['content']