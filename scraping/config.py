import os
import argparse


def set_config():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default= os.getenv('HOST'), help= 'host address')
    parser.add_argument('--user', default= os.getenv('DB_USER_ID'), help= 'user id')
    parser.add_argument('--password', default= os.getenv('DB_USER_PWD'), help= 'user password')
    parser.add_argument('--sql', type= str,
                        default= 'SELECT id, s_id, s_area_id, p_type, title, content, content_type, post_time, page_url \
                        FROM forum_data.ts_page_content ORDER BY post_time DESC LIMIT 1000', help= 'query command')

    args = parser.parse_args()

    return args
