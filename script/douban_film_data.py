# -*- coding: utf-8 -*-

import requests
from urllib import urlencode


def start():
    page_limit = 20
    for i in range(0, 10):
        crawl(page_limit, page_limit * i)


def crawl(page_limit=20, page_start=0):
    payload = {
        'type': 'movie',
        'tag': '热门',
        'sort': 'recommend',
        'page_limit': page_limit,
        'page_start': page_start
    }
    r = requests.get('https://movie.douban.com/j/search_subjects', params=payload)
    print r.url
    print r.json()

start()
