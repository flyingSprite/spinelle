# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.selector import Selector

from tasks.douban_film_data import DoubanMovieTask


class DoubanMovieSpider(scrapy.Spider):
    name = "douban_movie"
    allowed_domains = ["douban.com"]
    start_urls = list()

    def __init__(self):
        super(DoubanMovieSpider, self).__init__()
        self.douban_movie_task = DoubanMovieTask()
        douban_movie_list = self.douban_movie_task.spider_start_list()
        for index, douban_movie in enumerate(douban_movie_list):
            if douban_movie.get('url', None):
                self.start_urls.append(douban_movie.get('url', ''))

    def parse(self, response):
        print response.url
        sel = Selector(response=response)
        subject_interest = sel.xpath('//div[@class="subject-others-interests-ft"]')
        has_saw_people_url = response.url + 'collections/'
        want_to_see_people_url = response.url + 'wishes/'
        has_saw_people = 0
        want_to_see_people = 0

        try:
            subject_interest_value = subject_interest.extract()[0]
            has_saw_people_r = re.findall(u'>(\d+?)人看过<', subject_interest_value)
            want_to_see_people_r = re.findall(u'>(\d+?)人想看<', subject_interest_value)

            has_saw_people = int(has_saw_people_r[0]) if len(has_saw_people_r) > 0 else 0
            want_to_see_people = int(want_to_see_people_r[0]) \
                if len(want_to_see_people_r) > 0 else 0
            print has_saw_people, want_to_see_people
        except IndexError:
            pass

        self.douban_movie_task.upsert_saw_people_number(
            response.url,
            has_saw_people,
            has_saw_people_url,
            want_to_see_people,
            want_to_see_people_url
        )
