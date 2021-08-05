import argparse
import logging
import os
import pymysql.cursors
import pandas as pd
from time import time
from datetime import datetime


parser = argparse.ArgumentParser()
parser.add_argument('--host', default= os.getenv('HOST'), help= 'host address')
parser.add_argument('--user', default= os.getenv('DB_USER_ID'), help= 'user id')
parser.add_argument('--password', default= os.getenv('DB_USER_PWD'), help= 'user password')
parser.add_argument('--sql', type= str,
                    default= 'SELECT id, s_id, s_area_id, p_type, title, content, content_type, post_time, page_url \
                    FROM forum_data.ts_page_content ORDER BY post_time DESC LIMIT 10', help= 'query command')

args = parser.parse_args()

def connect_database(db, args):
    try:
        config = {
            'host': args.host,
            'user': args.user,
            'password': args.password,
            'db':db,
            'charset':'utf8mb4',
            'cursorclass':pymysql.cursors.DictCursor,
        }
        connection = pymysql.connect(**config)

        logging.info('Successfully connect to database')

        return connection
    except:
        logging.error('Fail to connect to database.')

def to_dataframe(data):
    return pd.DataFrame.from_dict(data)

if __name__ == "__main__":
    start_time = time()
    func = connect_database
    sql_cmd = args.sql
    with func('forum_data', args).cursor() as cursor:
        now = datetime.now().strftime("%m%d%Y%H%M%S")
        cursor.execute(sql_cmd)
        result = to_dataframe(cursor.fetchall()).drop_duplicates()
        result.to_pickle('./scrap_file/{0}_{1}.pkl'.format(now, len(result)))
        func('forum_data', args).close()
