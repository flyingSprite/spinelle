# -*- coding: utf-8 -*-
from scrapy import signals
from scrapy import Spider
from scrapy import Selector


class DoubanCommentSpider(Spider):
    name = "douban_comment"
    allowed_domains = ["douban.com"]
    start_urls = ['https://movie.douban.com/subject/26685451/collections']

    def __init__(self):
        super(DoubanCommentSpider, self).__init__()

    def parse(self, response):
        sel = Selector(response=response)
        comment_tables = sel.xpath('//div[@class="sub_ins"]/table')
        print len(comment_tables.extract())
        for comment_table in comment_tables:
            user_info = dict()
            comment_user_img_ele = comment_table.xpath('.//img')
            if comment_user_img_ele:
                comment_user_img = comment_user_img_ele.xpath('@src')
                user_info['img'] = comment_user_img.extract()[0]

            comment_username = comment_table.xpath('.//div[@class="pl2"]/a')
            if comment_username:
                username_str = comment_username.xpath('text()').extract()[0]
                user_info['name'] = username_str.strip()

                comment_user_addr = comment_username.xpath('.//span')
                if comment_user_addr:
                    user_addr_str = comment_user_addr.xpath('text()').extract()[0]
                    user_info['address'] = user_addr_str.strip()[1:-1]

            comment_date = comment_table.xpath('.//p[@class="pl"]')
            if comment_date:
                user_info['date'] = comment_date.xpath('text()').extract()[0].strip()

            comment_content = comment_table.xpath('.//tr/td/p')
            if len(comment_content) == 2:
                p_values = comment_content.xpath('text()').extract()
                user_info['comment_content'] = p_values[len(p_values) - 1]

            print user_info

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        instance = super(DoubanCommentSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(instance.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(instance.spider_closed, signal=signals.spider_closed)
        return instance

    @staticmethod
    def spider_opened():
        print 'Opened this spider.'

    @staticmethod
    def spider_closed():
        print 'Closed this spider.'
