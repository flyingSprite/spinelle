# -*- coding: utf-8 -*-

import requests
from common.mongo.mongo import MongoService

from tasks.basic_task import BasicTask


class DoubanMovieTask(BasicTask):

    def __init__(self):
        self.name = 'douban_movie_list'
        self.url = 'https://movie.douban.com/j/search_subjects'
        self.page_limit = 20
        self.mongoService = MongoService()
        self.collection = self.mongoService.collection(self.name)

    def spider_start_list(self):
        return self.collection.find(dict())

    def upsert_saw_people_number(
            self,
            url,
            has_saw_people,
            has_saw_people_url,
            want_to_see_people,
            want_to_see_people_url
    ):
        self.collection.find_one_and_update(
            filter={'url': url},
            update={
                '$set': {
                    'has_saw_people': has_saw_people,
                    'has_saw_people_url': has_saw_people_url,
                    'want_to_see_people': want_to_see_people,
                    'want_to_see_people_url': want_to_see_people_url
                }
            }
        )

    def crawl(self, page_limit=20, page_start=0):
        payload = {
            'type': 'movie',
            'tag': '热门',
            'sort': 'recommend',
            'page_limit': page_limit,
            'page_start': page_start
        }
        r = requests.get(self.url, params=payload)
        result = r.json()
        if result and result.get('subjects', None) and len(result.get('subjects', list())) > 0:
            self.insert_multi_subjects(result.get('subjects', list()))
            return True
        else:
            return False

    def insert_multi_subjects(self, subjects=list()):
        for subject in subjects:
            self.collection.insert_one(subject)

    def start_task(self):
        index = 0
        can_crawl_data = True
        while can_crawl_data:
            can_crawl_data = self.crawl(self.page_limit, self.page_limit * index)
            index += 1


class DoubanUser(object):

    def __init__(self):
        self.name = 'douban_user'
        self.mongoService = MongoService()
        self.collection = self.mongoService.collection(self.name)

    def insert_douban_user(self, user):
        self.collection.insert_one(user)
