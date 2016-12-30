
from pymongo import MongoClient, ReadPreference

from conf import config


'''
Doc: http://api.mongodb.com/python/current/
'''


class MongoService(object):

    def __init__(self):
        url = 'mongodb://' + config.USERNAME + ':' + config.PASSWORD + '@' + config.HOST + '/' + config.DATABASE
        # client = MongoClient("mongodb://stone01:stone_654321@www.duastone.com/solution", 27017)
        client = MongoClient(url, config.PORT)
        self.db = client.solution

    def collection(self, collection_name):
        return self.db.get_collection(collection_name, read_preference=ReadPreference.SECONDARY)

    @staticmethod
    def upsert(collection, item, query, field):
        o = collection.find_one(query)
        if o:
            collection.update_one(query, {"$set": {field: item[field]}})
        else:
            collection.insert_one(item)
