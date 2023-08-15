import requests
from bs4 import BeautifulSoup

def get_win_data():


    url = 'http://www.cwl.gov.cn/kjxx/ssq/kjgg/' # 您提供的网页 URL
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.select_one('div.table_ssq > table.ssq_table > tbody') # 找到指定位置的表格
    print(table)
    rows = table.find_all('tr')

    for row in rows:
        cols = row.select('td > div.qiu') # 找到每一行中所有的 div.qiu 元素
        cols = [col.text.strip() for col in cols]
        print(cols) # 打印每一行的数据

