# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.selector import Selector
from spinelle.items import HotNewsItem


class CnnSpider(scrapy.Spider):
    name = "cnn"
    allowed_domains = ["cnn.com"]
    start_urls = (
        'http://edition.cnn.com/',
    )
    website = 'CNN'
    website_url = 'http://edition.cnn.com/'

    def parse(self, response):
        sel = Selector(response=response)
        # logging.info(sel.extract())
        top_news = sel.xpath('//h3[@data-analytics="_list-hierarchical-piped_article_"]')[0]
        top_news_link = top_news.xpath('a')[0]

        print top_news_link.xpath('@href').extract()
        print top_news_link.xpath('span/text()').extract()

        cnn_item = HotNewsItem(self.website, self.website_url)
        cnn_item['href'] = '' + top_news_link.xpath('@href').extract()[0]
        cnn_item['name'] = top_news_link.xpath('span/text()').extract()[0]

        return cnn_item
