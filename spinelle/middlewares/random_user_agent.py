
from faker import Faker


class RandomUserAgent(object):

    def __init__(self):
        self.faker = Faker()

    @classmethod
    def from_crawler(cls, crawler):
        """scrpay from_crawler

        :param crawler:
        :return: RandomUserAgent class instance
        """
        _ = crawler
        return cls()

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', self.faker.user_agent())
