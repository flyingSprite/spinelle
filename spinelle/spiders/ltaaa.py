
# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

from spinelle.items import LtaaaItem


class ListSpider(scrapy.Spider):
    name = "ltaaa"
    allowed_domains = ["ltaaa.com"]
    start_urls = (
        'http://www.ltaaa.com/wtfy.html',
    )
    default_url = "http://www.ltaaa.com"
    count = 0
    spider_index = 0

    """
    <code>
    <li>
        <div class="dtop">
            <img src="http://img.ltaaa.com/data/flag/15.gif">
            <a href="/wtfy/19313.html" target="_blank">德国人印度行第二章：河流的尊严</a>
        </div>
        <div class="dbody">
            <img src="http://img.ltaaa.com/uploadfile/thumb/2016/04/01/1459504304903.jpg">
            <p>“清洁恒河行动”会让恒河重新清澈。“印度制造”将会吸引国际企业。“数字印度”将会让印度村通网。
            穆迪总理希望将印度这个发展中国家打造成世界顶尖国家。我追寻着他的许诺开始了在印度的旅程。</p>
            <span class="p1"><i class="icon-time"></i> 2016-04-01</span>
            <span class="p2"><i class="icon-user"></i>
                <a href="http://share.ltaaa.com/UMTQzMTM5" target="_blank" class="bule1">奥恰恰</a>
            </span>
            <span><i class="icon-search"></i> 8973</span>
            <span><i class="icon-time"></i> 18</span>
        </div>
        <div class="clear"></div>
    </li>
    </code>
    """

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="wlist"]/li')

        for site in sites:
            try:
                item = LtaaaItem()

                dtop = site.xpath('.//div[@class="dtop"]')[0]

                flag = dtop.xpath('.//img/@src')
                title = dtop.xpath('.//a/text()')
                url = dtop.xpath('.//a/@href')

                item['flag'] = flag.extract()[0]
                item['title'] = title.extract()[0]
                article_url = self.default_url + url.extract()[0]
                item['url'] = article_url

                dbody = site.xpath('.//div[@class="dbody"]')[0]
                pic = dbody.xpath('.//img/@src')
                content = dbody.xpath('.//p/text()')

                item['pic'] = pic.extract()[0]
                item['content'] = content.extract()[0]

                infos = dbody.xpath('.//span/text()').extract()

                if len(infos) == 4:
                    item['create_date'] = infos[0]
                    item['search_times'] = infos[2]
                    item['comments'] = infos[3]

                author_content = dbody.xpath('.//span[@class="p2"]')
                author_href = author_content.xpath('.//a/@href')
                author_name = author_content.xpath('.//a/text()')

                item['author_href'] = author_href.extract()[0]
                item['author_name'] = author_name.extract()[0]

                item['spider_index'] = self.spider_index

                # Redirect to detail page. to get detail information
                yield scrapy.Request(
                    url=article_url,
                    meta={'item': item},
                    callback=self.parse_detail,
                    dont_filter=True
                )

                # print(item)

            except Exception as e:
                print(e)

    @staticmethod
    def parse_detail(response):
        # div = response.xpath('//div[contains(@class, "post-title")]')
        item = response.meta['item']
        yield item
