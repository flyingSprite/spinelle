
from pymongo import MongoClient, ReadPreference

from conf import config


"""
Doc: http://api.mongodb.com/python/current/
"""


class MongoService(object):

    def __init__(self):
        url = f'mongodb://{config.USERNAME}:{config.PASSWORD}@{config.HOST}/{config.DATABASE}'
        client = MongoClient(url, config.PORT)
        self.db = client.podou

    def collection(self, collection_name):
        """Get Mongodb collection by collection Name
        :param collection_name: Collection Name
        :return: pymongo collection instance
        """
        return self.db.get_collection(collection_name, read_preference=ReadPreference.SECONDARY)

    @staticmethod
    def upsert(collection, item, query, field):
        o = collection.find_one(query)
        if o:
            collection.update_one(query, {'$set': {field: item[field]}})
        else:
            collection.insert_one(item)
