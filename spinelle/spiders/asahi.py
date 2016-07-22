# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from spinelle.items import HotNewsItem


class AsahiSpider(scrapy.Spider):
    name = 'asahi'
    allowed_domains = ['asahi.com']
    start_urls = (
        'http://www.asahi.com/',
    )
    website = '朝日新聞'
    website_url = 'http://www.asahi.com'

    def parse(self, response):
        sel = Selector(response=response)
        sites = sel.xpath('//div[contains(@class, "TopNewsArea")]')
        a_links = sites.xpath('.//a')
        items = []
        for a_link in a_links:
            asahi_item = HotNewsItem(self.website, self.website_url)
            asahi_item['href'] = a_link.xpath('@href').extract()[0]
            try:
                asahi_item['name'] = a_link.xpath('text()').extract()[0]
            except IndexError:
                asahi_item['name'] = a_link.xpath('span/text()').extract()[0]
            items.append(asahi_item)
        return items
