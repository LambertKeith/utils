from excel_operator.result_utils import find_csv_files, find_png_files, result_info
import llm_utils.llm_utils as utils

def test1():
    answer = utils.llm_quary("source_data\Seasons_Stats.csv", '请你将场均得分前10的球员筛选出来，并用plt绘制条状图，并将图片和处理之后的表格保存到本地/result_data/目录下')
    print(answer)

def test2():
    data = result_info("source_data\Seasons_Stats.csv", '请你将场均得分前10的球员筛选出来，并用plt绘制条状图，并将图片和处理之后的表格保存到本地/result_data/目录下')
    print(data)

def test3():
    print(find_csv_files('result_data'))
    
if __name__ == '__main__':
    test3()