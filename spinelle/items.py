# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpinelleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class HuanqiuItem(scrapy.Item):
    no = scrapy.Field()
    href = scrapy.Field()
    name = scrapy.Field()
    website = scrapy.Field()
    timestamp = scrapy.Field()
