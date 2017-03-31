
import json
import time
import requests

from common.mongo.mongo import MongoService
from common.utility.image_downloader import get_image


class HuabanDrawcrowdTask(object):
    cookies = dict(
        sid='B3aOonIXtRYDEPoV5uVfqfkyXbA.G7oIUoxfpshMgB4OVvCxEIKKVH5Nk3cImmPvxBaxqOA'
    )

    headers = {
        'X-Request': 'JSON',
        'X-Requested-With': 'XMLHttpRequest',
    }

    def __init__(self):
        self.name = 'huaban_drawcrowd'
        self.counter = 0
        self.mongoService = MongoService()
        self.collection = self.mongoService.collection(self.name)

    def request_json_list(self, start_pin_id):
        self.counter += 1
        print(f'request counter: {self.counter}')
        time.sleep(0.3)
        request_url = f'http://huaban.com/from/drawcrowd.com?max={str(start_pin_id)}&limit=20&wfl=1'
        response = requests.get(request_url, headers=self.headers, cookies=self.cookies)
        result = response.text
        self.analysis_json(json.loads(result))

    def analysis_json(self, json_result):
        response_list = json_result.get('pins')

        for item in response_list:
            self.save_item(self.parse_item(item))

        if len(response_list) > 0:
            last_item = response_list[len(response_list) - 1]
            last_pin_id = last_item['pin_id'] if 'pin_id' in last_item else None
            if last_pin_id:
                self.request_json_list(last_pin_id)

    @staticmethod
    def parse_item(item):
        if item:
            parse_item = dict()
            if 'file' in item and 'key' in item['file']:
                parse_item['img_hash'] = item['file']['key']
            if 'user' in item:
                parse_item['username'] = item['user']['username'] \
                    if 'username' in item['user'] else ''
                parse_item['urlname'] = item['user']['urlname'] \
                    if 'urlname' in item['user'] else ''
            parse_item['raw_text'] = item['raw_text'] if 'raw_text' in item else ''
            parse_item['load_time'] = round(time.time() * 1000)
            return parse_item
        return None

    def save_item(self, parse_item):
        if parse_item and 'img_hash' in parse_item:
            self.collection.insert_one(parse_item)

    def start(self, pin_id=1079920040):
        pin_id = pin_id if pin_id else 1079920040
        self.request_json_list(pin_id)

    def find(self, limit=10):
        query_results = self.collection.find().limit(limit)
        for item in query_results:
            self.counter += 1
            if 'img_hash' in item:
                print(item['img_hash'])
                get_image(item['img_hash'])
            print(self.counter)

huaban = HuabanDrawcrowdTask()
# huaban.start()
huaban.find(1000)
