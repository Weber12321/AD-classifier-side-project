import pandas as pd
from tqdm import tqdm


def read_keyword():
    with open('./scraping/scrap_keyword.txt', 'r') as f:
        keyword = [line for line in f.read().splitlines()]
        return keyword


def find_keyword(data):
    keyword= read_keyword()
    data['text'] = data.title + data.content
    column_names = ['id', 's_id', 's_area_id', 'p_type', 'title',
                    'content', 'content_type', 'post_time', 'page_url', 'text']
    df = pd.DataFrame(columns = column_names)
    # save = []
    for i in tqdm(range(len(data['text'].astype(str)))):
        for word in keyword:
            if word in data['text'].iloc[i]:
                df = df.append(data.iloc[i], ignore_index= True)
            else:
                continue

    return df

def find_without_keyword(data):
    keyword= read_keyword()
    data['text'] = data.title + data.content
    column_names = ['id', 's_id', 's_area_id', 'p_type', 'title',
                    'content', 'content_type', 'post_time', 'page_url', 'text']
    df = pd.DataFrame(columns = column_names)
    # save = []
    for i in tqdm(range(len(data['text'].astype(str)))):
        if any([word in data['text'].iloc[i] for word in keyword]):
            continue
        else:
            df = df.append(data.iloc[i], ignore_index= True)

    return df
