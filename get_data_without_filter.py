from datetime import datetime
from scraping.config import set_config
from scraping.connect import execute_srcaping
from scraping.keyword_filter import find_keyword, find_without_keyword


if __name__ == '__main__':
    data = execute_srcaping(set_config())
    pos = find_keyword(data).drop_duplicates()
    neg = find_without_keyword(data).drop_duplicates()

    now = datetime.now().strftime("%m%d%Y%H%M%S")
    pos.to_csv('./scrap_file/pos_{0}_{1}.csv'.format(now, len(pos)), index= False, encoding= 'utf-8-sig')
    neg.to_csv('./scrap_file/neg_{0}_{1}.csv'.format(now, len(neg)), index= False, encoding= 'utf-8-sig')

