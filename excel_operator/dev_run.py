import llm_utils.llm_utils as utils

def test1():
    answer = utils.llm_quary("source_data\Seasons_Stats.csv", '请你将场均得分前10的球员筛选出来，并用plt绘制条状图，')
    print(answer)

if __name__ == '__main__':
    test1()