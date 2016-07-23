# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from spinelle.items import HotNewsItem


class SankeiSpider(scrapy.Spider):
    name = "sankei"
    allowed_domains = ["sankei.com"]
    start_urls = (
        'http://www.sankei.com/',
    )
    website = '産経新聞'
    website_url = 'http://www.sankei.com'

    def parse(self, response):
        items = []
        sel = Selector(response=response)
        sites = sel.xpath('//section[@class="modToplist"]/ul')
        a_links = sites.xpath('.//a')
        for a_link in a_links:
            sankei_item = HotNewsItem(self.website, self.website_url)
            href = a_link.xpath('@href').extract()[0]
            href = 'http://www.sankei.com' + href[1: len(href)]
            sankei_item['name'] = a_link.xpath('text()').extract()[0]
            sankei_item['href'] = href
            items.append(sankei_item)
        return items
