import sys

from scrapy.conf import settings
from scrapy.crawler import CrawlerProcess

from conf.settings import MISSION_MESSAGE
from core.aliyun.aliyun_cms import run
from spinelle.spiders.asahi import AsahiSpider
from spinelle.spiders.huanqiu import HuanqiuSpider
from spinelle.spiders.sankei import SankeiSpider
from common.mongo.mongo import MongoService


class CrawlService(object):

    def __init__(self):
        self.mongoService = MongoService()
        self.crawlProcess = CrawlerProcess(settings=settings)
        self.collection = self.mongoService.collection('crawl')

    def process(self):
        self.crawlProcess.crawl(AsahiSpider)
        self.crawlProcess.crawl(SankeiSpider)
        self.crawlProcess.crawl(HuanqiuSpider)

    def start(self):
        self.process()
        self.crawlProcess.start()

    def __del__(self):
        crawl_record = {
            'type': 'hotnews',
            'timestamp': MISSION_MESSAGE,
            'log': 'Crawl hot news.'
        }
        self.collection.insert_one(crawl_record)


class Service(object):
    service = None

    def __init__(self):
        pass

    def start_crawl(self):
        self.service = CrawlService()
        self.service.start()

    def start_aliyun_cms(self):
        run()


if __name__ == '__main__':
    service = Service()
    length = len(sys.argv)
    if length == 1:
        service.start_crawl()
    elif length == 2:
        command = sys.argv[1]
        if command == 'crawl':
            service.start_crawl()
        elif command == 'aliyun':
            service.start_aliyun_cms()
    else:
        pass

