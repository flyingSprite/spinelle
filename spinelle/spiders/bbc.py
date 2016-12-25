"""Crawl www.bbc.com site."""
import scrapy
import logging
from scrapy.selector import Selector
from spinelle.items import HotNewsItem


class BbcSpider(scrapy.Spider):
    """Class BbcSpider."""

    name = "bbc"
    allowed_domains = ["bbc.com"]
    start_urls = (
        'http://www.bbc.com/news',
    )
    website = 'BBC'
    website_url = 'http://www.bbc.com/'

    def parse(self, response):
        """Parse html content."""
        items = []
        sel = Selector(response=response)
        sites = sel.xpath('//div[@id="comp-top-stories-2"]')
        a_links = sites.xpath('.//a[@class="title-link"]')

        a_links_other = sites.xpath('.//a[@class="links-list__link"]')
        a_links.extend(a_links_other)

        logging.info(a_links.extract())
        logging.info(len(a_links.extract()))

        for a_link in a_links:
            bbc_item = HotNewsItem(self.website, self.website_url)
            href = a_link.xpath('@href').extract()[0]
            arr_name = a_link.xpath('.//text()').extract()

            if len(arr_name) == 5:
                name = arr_name[2]
            elif len(arr_name) == 3:
                name = arr_name[2]
            else:
                name = arr_name[0]
            logging.info(name.strip())
            bbc_item['href'] = 'http://www.bbc.com' + href
            bbc_item['name'] = name
            items.append(bbc_item)
        return items
