# -*- coding: utf-8 -*-
"""Scrapy Item Classes."""

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from conf.settings import MISSION_MESSAGE


class SpinelleItem(scrapy.Item):
    """Class SpinelleItem start."""

    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class HotNewsItem(scrapy.Item):
    """Class HotNewsItem start."""

    _id = scrapy.Field()
    no = scrapy.Field()
    href = scrapy.Field()
    name = scrapy.Field()
    website = scrapy.Field()
    websiteUrl = scrapy.Field()
    type = scrapy.Field()
    startTimestamp = scrapy.Field()
    amendTimestamp = scrapy.Field()

    def __init__(self, website, website_url):
        """__init__."""
        super(HotNewsItem, self).__init__()
        self['no'] = MISSION_MESSAGE
        self['type'] = 'hotnews'
        self['website'] = website
        self['websiteUrl'] = website_url
        self['startTimestamp'] = MISSION_MESSAGE
        self['amendTimestamp'] = MISSION_MESSAGE


class CnPluginsItem(scrapy.Item):
    """Class CnPlugins start."""

    href = scrapy.Field()
    pic = scrapy.Field()
    title = scrapy.Field()
    detail_info = scrapy.Field()
    download_href = scrapy.Field()
    author_href = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    note = scrapy.Field()
