
from article_writer.views_utils import get_first_level_keys, get_second_level_keys, get_value


if __name__ == '__main__':
    print(get_value('data/prompts.json', '日常', '小红书'))