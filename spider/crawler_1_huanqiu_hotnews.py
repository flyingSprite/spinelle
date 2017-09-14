
from scrapy.utils.project import get_project_settings
from scrapy.crawler import CrawlerProcess

from spinelle.spiders.huanqiu import HuanqiuSpider

# See https://github.com/sebdah/scrapy-mongodb/commit/4723d7af5c2a6867e51e84d75061e0b2ac148084
SETTINGS = get_project_settings()


class HuanqiuCrawler(object):

    def __init__(self):
        self.crawler_process = CrawlerProcess(settings=SETTINGS)
        self.crawler_process.crawl(HuanqiuSpider)

    def start(self):
        self.crawler_process.start()


crawler = HuanqiuCrawler()
crawler.start()

