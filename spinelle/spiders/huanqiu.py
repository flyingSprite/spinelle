# -*- coding: utf-8 -*-
"""Crawl www.huanqiu.com site."""
import scrapy
from scrapy.selector import Selector
from spinelle.items import HotNewsItem


class HuanqiuSpider(scrapy.Spider):
    """Class HuanqiuSpider Start."""

    name = 'huanqiu'
    allowed_domains = ['huanqiu.com']
    start_urls = (
        'http://www.huanqiu.com/',
    )
    website = '环球时报'
    website_url = 'http://www.huanqiu.com'

    def parse(self, response):
        """ Parse Html Content
        Keyword arguments:
        :param response -- HTTP Response
        """
        sel = Selector(response=response)
        hotnews_content = sel.xpath('//div[@class="firNews"]/ul')
        sites = hotnews_content.xpath('.//a')
        items = []
        for a_link in sites:
            huanqiu_item = HotNewsItem(self.website, self.website_url)
            news_name = a_link.xpath('text()').extract()[0]
            if news_name != u'图解' and news_name != u'解读':
                huanqiu_item['href'] = a_link.xpath('@href').extract()[0]
                huanqiu_item['name'] = news_name
                items.append(huanqiu_item)
                print(huanqiu_item)
        return items
