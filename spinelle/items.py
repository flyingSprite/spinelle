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
    stype = scrapy.Field()

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
        self['stype'] = 'ltaaa'
        self['no'] = MISSION_MESSAGE
        self['type'] = 'hotnews'
        self['website'] = website
        self['websiteUrl'] = website_url
        self['startTimestamp'] = MISSION_MESSAGE
        self['amendTimestamp'] = MISSION_MESSAGE


class CnPluginsItem(scrapy.Item):
    """Class CnPlugins start."""
    stype = scrapy.Field()

    href = scrapy.Field()
    pic = scrapy.Field()
    title = scrapy.Field()
    detail_info = scrapy.Field()
    download_href = scrapy.Field()
    author_href = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    note = scrapy.Field()

    def __init__(self):
        """__init__."""
        super(CnPluginsItem, self).__init__()
        self['stype'] = 'ltaaa'


class LtaaaItem(scrapy.Item):
    """Item for Ltaaa website"""
    stype = scrapy.Field()

    _id = scrapy.Field()
    flag = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()

    pic = scrapy.Field()
    content = scrapy.Field()

    create_date = scrapy.Field()
    search_times = scrapy.Field()
    comments = scrapy.Field()

    author_href = scrapy.Field()
    author_name = scrapy.Field()

    spider_index = scrapy.Field()

    def __init__(self):
        """__init__."""
        super(LtaaaItem, self).__init__()
        self['stype'] = 'ltaaa'


