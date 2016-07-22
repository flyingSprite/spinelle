# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from spinelle.items import HotNewsItem


class HuanqiuSpider(scrapy.Spider):
    name = 'huanqiu'
    allowed_domains = ['huanqiu.com']
    start_urls = (
        'http://www.huanqiu.com/',
    )
    website = '环球时报'
    website_url = 'http://www.huanqiu.com'

    def parse(self, response):
        sel = Selector(response=response)
        sites = sel.xpath('//div[@class="firNews"]/ul/div/li')
        items = []
        for site in sites:
            a_links = site.xpath('.//a')
            for a_lint in a_links:
                huanqiu_item = HotNewsItem(self.website, self.website_url)
                huanqiu_item['href'] = a_lint.xpath('@href').extract()[0]
                huanqiu_item['name'] = a_lint.xpath('text()').extract()[0]
                items.append(huanqiu_item)
        return items
