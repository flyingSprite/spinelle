# -*- coding: utf-8 -*-
"""Scrapy www.cnplugins.com site."""
# import json
import scrapy
from scrapy.selector import Selector
from spinelle.items import CnPluginsItem


class CnpluginsSpider(scrapy.Spider):
    """Class CnpluginsSpider start."""

    name = "cnplugins"
    allowed_domains = ["cnplugins.com"]
    start_urls = (
        'http://www.cnplugins.com/devtool/',
    )

    devtool_home_link = 'http://www.cnplugins.com/devtool/'

    def __init__(self):
        """__init__."""
        super(CnpluginsSpider, self).__init__()
        # self.start_urls = list()
        # for num in range(1, 172):
        #     url =
        # 'http://www.cnplugins.com/devtool/devtool-%s.html' % str(num)
        #     self.start_urls.append(url)

    def parse(self, response):
        """Parse Start."""
        print 'Start Crawl cnplugins content.'
        item = self.parse_content(response)
        return item

    def parse_content(self, response):
        """Parse html content."""
        sel = Selector(response=response)
        article_content = sel.xpath('//article[@class="arcbox"]')
        for content in article_content:
            item = self.parse_article_content(content)
            if item:
                yield scrapy.http.Request(
                    url=item['href'],
                    meta={'item': item},
                    callback=self.inter_plugin_detail_page,
                    dont_filter=False
                )

    def parse_article_content(self, article_content):
        """Parse one CnPlugins plugin content."""
        item = CnPluginsItem()
        content_thumb = article_content.xpath('.//div[@class="thumb"]')

        if content_thumb and len(content_thumb) > 0:

            content_thbum_link = content_thumb.xpath('.//a')
            if content_thbum_link and len(content_thbum_link) > 0:
                plugin_href = content_thbum_link.xpath('@href')[0].extract()
                item['href'] = plugin_href

            content_thbum_img = content_thumb.xpath('.//img')
            if content_thbum_img and len(content_thbum_img) > 0:
                plugin_pic = content_thbum_img.xpath('@src')[0].extract()
                plugin_title = content_thbum_img.xpath('@alt')[0].extract()
                item['pic'] = plugin_pic
                item['title'] = plugin_title

        content_span = article_content.xpath('.//p/span')
        if content_span and len(content_span) >= 2:
            plugin_author_href = content_span \
                .xpath('.//a/@href').extract()[0]
            plugin_author = content_span.xpath('.//a/text()').extract()[0]
            plugin_date = content_span[1].xpath('.//text()').extract()[0]
            item['author_href'] = plugin_author_href
            item['author'] = plugin_author
            item['date'] = plugin_date

        content_note = article_content.xpath('.//p[@class="note"]')
        if content_note and len(content_note) > 0:
            content_note_detail = content_note.xpath('.//text()').extract()
            plugin_note = ' '.join(content_note_detail).strip()
            item['note'] = plugin_note
        return item

    def parse_pager_content(self, pager_content):
        """To parse the next page."""
        content_links = pager_content.xpath('.//a')
        if content_links and len(content_links) >= 3:
            next_link = None
            if content_links[2].xpath('.//text()').extract()[0] == u'下一页':
                next_link = content_links[2].xpath('.//@href').extract()[0]
            elif content_links[1].xpath('.//text()').extract()[0] == u'下一页':
                next_link = content_links[1].xpath('.//@href').extract()[0]

            if next_link is not None:
                next_link_full = self.devtool_home_link + next_link
                self.request_next(url=next_link_full)

    def inter_plugin_detail_page(self, response):
        """Inter into plugin detail page."""
        item = response.meta['item']
        sel = Selector(response)

        download_content = sel.xpath('.//a[@class="dbtn"]')
        if download_content and len(download_content) > 0:
            download_href = download_content.xpath('@href').extract()[0]
            item['download_href'] = download_href
        return item
