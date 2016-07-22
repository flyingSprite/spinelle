# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
import sys
import io
from conf.config import MISSION_MESSAGE
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')


class SpinellePipeline(object):
    def process_item(self, item, spider):
        return item


class HotNewsPipeline(object):

    def process_item(self, item, spider):
        item['no'] = MISSION_MESSAGE
        item['timestamp'] = int(time.time())
        print item
        return item
