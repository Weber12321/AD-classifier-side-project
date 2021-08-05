import pandas as pd
from tqdm import tqdm


def read_keyword():
    with open('keyword.txt', 'r') as f:
        keyword = [line for line in f.read().splitlines()]
        return keyword


def find_keyword(data):
    keyword= read_keyword()
    data['text'] = data.title + data.content
    save = []
    for id, item in tqdm(zip(data['id'],data['text'].astype(str))):
        for word in keyword:
            if word not in item:
                save.append([id, item])

    return save

def find_without_keyword(data):
    keyword= read_keyword()
    data['text'] = data.title + data.content
    save = []
    for id, item in tqdm(zip(data['id'],data['text'].astype(str))):
        if any([word in item for word in keyword]):
            continue
        else:
            save.append([id, item])

    return save
