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


class HotNewsItem(scrapy.Item):

    no = scrapy.Field()
    href = scrapy.Field()
    name = scrapy.Field()
    website = scrapy.Field()
    websiteUrl = scrapy.Field()
    type = scrapy.Field()
    timestamp = scrapy.Field()

    def __init__(self, website, website_url):
        super(HotNewsItem, self).__init__()
        self['type'] = 'hotnews'
        self['website'] = website
        self['websiteUrl'] = website_url
