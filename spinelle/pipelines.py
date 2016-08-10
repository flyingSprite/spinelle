# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from utility.mongo import MongoService


# class SpinellePipeline(object):
#     def process_item(self, item, spider):
#         return item


class HotNewsPipeline(object):

    collection = None

    def __init__(self):
        self.service = MongoService()
        self.collection = self.service.collection('hotnews')

    def process_item(self, item, spider):
        # Overlook spider argument
        _ = spider
        self.save(item)
        return item

    def save(self, item):
        self.service.upsert(
            self.collection,
            item,
            {'href': item['href']},
            'amendTimestamp'
        )
