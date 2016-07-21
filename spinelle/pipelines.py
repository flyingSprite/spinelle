# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
from conf.config import MISSION_MESSAGE


class SpinellePipeline(object):
    def process_item(self, item, spider):
        return item


class HuanqiuPipeline(object):

    def process_item(self, item, spider):
        item['no'] = MISSION_MESSAGE
        item['website'] = 'huanqiu'
        item['timestamp'] = int(time.time())
        print item
        return item
