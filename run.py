

from scrapy.conf import settings
from scrapy.crawler import Crawler, CrawlerProcess
from spinelle.spiders.asahi import AsahiSpider
from spinelle.spiders.sankei import SankeiSpider
from spinelle.spiders.huanqiu import HuanqiuSpider


from conf.settings import MISSION_MESSAGE
from utility.mongo import MongoService


class Process(object):

    def __init__(self):
        service = MongoService()
        self.crawlProcess = CrawlerProcess(settings=settings)
        self.collection = service.collection('crawl')

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


process = Process()
process.start()
